Title: DRY vs Coupling in Production Code
Date: 2015-07-01
Author: Shaun Finglas
Tags: tutorial, programming
Slug: 2015/06/dry-vs-coupling-in-production-code

[Duplication in tests can be a good
thing](http://blog.shaunfinglas.co.uk/2015/04/randomly-generated-values-in-tests.html).
The same can be said for production code as well in some cases. No. I'm
not going mad. I probably wouldn't believe this if you showed me this
several years ago either. More experience has shown me that loose
coupling is often more desirable than removing duplication. In other
words, the more duplication you remove, the more coupling you introduce
inadvertently.

Duplication of logic is bad and will always be the case. I am not
debating this. You should only have one logical place for any domain
logic. As always follow the DRY principle. However just because two
pieces of code look the same, does not mean there is duplication.

##### Example

A system from my past had two places where an address was required for
display and serialization. Billing and Delivery addresses.

<script src="https://gist.github.com/Finglas/d8d327e65dc0620cb372.js"></script>
My gut reaction was to introduce a common address model that could be
used for serialization and display. After all this screams of
duplication. However a billing address and delivery address are two
conceptually different things despite appearing identical.

Given time the needs of the billing functionality may very well differ
from the needs of the delivery domain. Duplication of models/contracts
is weak duplication. There is no logic here.

In DDD each bounded context will have different needs. As it turned out
the Billing Address began to have specific billing related functionality
added such as "IsDefaultAddress" and "IsSameAsDelivery". At this point
the two models are very different. This was a problem.

<script src="https://gist.github.com/Finglas/f5606f1f8a68f7caef78.js"></script>
Sharing via a common library would have removed the total lines of code
but increase the number of dependencies. The Address is now coupled to a
single form meaning updates and new requirements are harder. Versioning
and packaging are now a concern. Any updates would need to be
coordinated across teams. Udi Dahan has warned about this previously in
what is summarized as "[Beware the
Share](http://programmer.97things.oreilly.com/wiki/index.php/Beware_the_Share)".

##### Inheritance?

This example makes inheritance look like a good fit. While the use of
inheritance when applied correctly is not a bad thing, this scenario is
not appropriate. Inheritance is one of the strongest forms of coupling.
Applying inheritance across a type that we don't own is risky for the
reasons detailed previously. Now change is not only harder, it would
potentially be a breaking change. How would we model a delivery address
with multiple addresses? Why should both the billing and delivery domain
use the same terminology for its fields? If we accept that both
addresses are conceptually different despite looking identical at
present, we can side step these issues.

##### What to Share?

-   Domain types should be shared. Using the previous example a
    PostalCode would make a good type to share. The functionality here
    is identical regardless of the type of address. PostalCode would
    likely have logic associated with the type which would not make
    sense to duplicate or implement in each sub system.
-   Shared functionality that must be consistent makes a good candidate
    also. Examples such as UI widgets including headers and footers.
-   Crossing cutting concerns such as logging, security and
    configuration can be shared when appropriate. A downside to this is
    you now force your consumers to take specific dependency versions
    which may or may not be acceptable.

##### Shared Kernel

DDD has the concept of a Shared Kernel. The dictionary definition of a
kernel is "*the central or most important part of something*". Shared
Kernel's make sense to share the common functionality previously. The
name "common" is poorly thought out however. Most codebases will have a
common or utility library but by there very nature these will grow into
large components.

The reason for this growth is everything is common across applications.
All applications need some sort of data access, so stick it in the
common library. All applications need some sort of serialization
mechanisms, so stick it in the common library. All applications need
some sort of web technology, so stick it in the common library. You
should be able to see where this is going.

##### Conclusion

As always when dealing with duplication apply the [Rule of
Three](http://c2.com/cgi/wiki?RuleOfThree) where appropriate. If you
really must create a shared component, a small, concise library is
better than a library that handles multiple concerns. This will allow
consumers to adopt a "*plug 'n play*" approach with which components
they require. Even then, try to fight removing duplication unless you
can be really sure there is a good reason to increase coupling. That
reuse you are striving for might not even come to fruition.