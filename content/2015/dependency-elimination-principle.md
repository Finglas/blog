Title: Dependency Elimination Principle
Date: 2015-03-01
Author: Shaun Finglas
Tags: abstractions-series, tutorial
Slug: 2015/03/dependency-elimination-principle

This is the third, and final part of my series on abstractions.

-   Part 1 -
    [Abstractions](http://blog.shaunfinglas.co.uk/2015/02/abstractions.html)
-   Part 2 - [Reused Abstraction
    Principle](http://blog.shaunfinglas.co.uk/2015/03/reused-abstraction-principle.html)

------------------------------------------------------------------------

I've wrote about what [good dependencies are before, and the benefits if
you can limit and remove them where
possible](http://blog.shaunfinglas.co.uk/2014/12/limit-amount-of-dependencies-you-use.html).

You can take this idea further though, by applying concepts from
functional programming such as "*depend on values rather than
dependencies*".

A wise colleague started me down this path of passing values, rather
than dependencies on collaborators after we repeatedly found ourselves
depending on implementation details. This meant our high level domain
logic was tightly coupled to low level implementation details.

[Brian Geihsler](https://twitter.com/briangeihsler) reminded me of this
concept with an [excellent demonstration of this in
practice](http://qualityisspeed.blogspot.co.uk/2015/02/the-dependency-elimination-principle-a-canonical-example.html)
and has allowed me to put a name to this practice.

Additionally [J.B. Rainsberger's example is with a virtual
clock](http://blog.thecodewhisperer.com/2013/11/23/beyond-mock-objects/),
another common dependency we often need. In this case, ask for the time,
not how you get the time. The example also highlights another common
problem with conventions when using a framework or library.

<script src="https://gist.github.com/Finglas/ca5bbde5a06f6c7c627b.js"></script>
Here we can handle commands but only those that match the signature of
taking a single command, and returning no response. In order to apply
the Dependency Elimination Principle (DEP) and remove the clock wrapper
we can introduce an overload. Our tests will be expressed using the
overload, while the production code will make use of the standard
method. If the class in question has a relevant set of interfaces, the
overload would be omitted from this to ensure that consumers have a
clean, focused API to consume.

<script src="https://gist.github.com/Finglas/9fe933e771fad1c3a693.js"></script>
When the DEP is applied to other dependencies such as configuration
details, flexibility is achieved by the ability to provide these values
from any source. As a side effect, coupling has been reduced, while also
removing an unnecessary abstraction from the codebase.

Try to apply the DEP where possible. Remove as many dependencies as
possible for flexible, maintainable code. Not all dependencies can be
eliminated, but unless the dependency is a valid abstraction it may be
worth considering removing or reducing use.