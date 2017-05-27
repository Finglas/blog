Title: Reused Abstraction Principle
Date: 2015-03-11 22:20
Author: Shaun Finglas
Tags: abstractions, http://schemas.google.com/blogger/2008/kind#post, abstractions-series, code-quality
Slug: reused-abstraction-principle

This is the second part of my series on abstractions.

-   Part 1 -
    [Abstractions](http://blog.shaunfinglas.co.uk/2015/02/abstractions.html)
-   Part 3 - [Dependency Elimination
    Principle](http://blog.shaunfinglas.co.uk/2015/03/dependency-elimination-principle.html)

------------------------------------------------------------------------

The Reused Abstraction Principle is a simple in concept in practice, but
oddly rarely followed in typical enterprise development. I myself have
been incredibly guilty of this in the past.

Most code bases have a 1:1 mapping of interfaces to implementations.
Usually this is the sign of TDD or automated testing being applied
badly. The majority of these interfaces are wrong. [1:1 mappings between
interfaces and implementations is a code
smell](http://blog.ploeh.dk/2010/12/02/Interfacesarenotabstractions/).

Such situations are usually the result of extracting an interface from
an implementation, rather than having the client drive behaviour.

These interfaces are also often bad abstractions, known as "leaky
abstractions". As [I've discussed previously, these abstractions tend to
offer nothing more than simple
indirection](http://blog.shaunfinglas.co.uk/2015/02/abstractions.html).

#### Example

Apply the "*rule of three*". If there is only ever one implementation,
then you don't need the interface/base class. If you do need to
introduce an interface, have the client provide it. Try to resist the
urge to extract from an implementation. Any stubs or testing
implementations should be treated as valid implementations, despite no
use within the production code directly.

<script src="https://gist.github.com/Finglas/53d16d4bcadaa6eda702.js"></script>
In the first example there is a 1:1 mapping. [This is clutter and
needless
indirection](http://www.codemanship.co.uk/parlezuml/blog/?postid=934).
As we have nothing to replace `FooService` with, the interface offers no
value. The second example shows multiple implementations of `IFoo`. Here
different implementations have unique responsibilities. We could use a
test stub, or use the decorator pattern whenever we use `IFoo`. The
abstraction is valuable.

[If you can introduce a composite or decorator this is probably a sign
of a good abstraction at
work](http://blog.ploeh.dk/2010/12/03/Towardsbetterabstractions/).
Likewise the ability to replace your implementation and have the code
still function is a good sign. Such an example would be `SqlRepository`
replaced with `MongoRepository` when `IRepository` is required.

Additionally just because you opt to use dependency injection, there is
no rule stating said dependency must be an interface or base class.

The final point is to [remember what good dependencies
are](http://blog.shaunfinglas.co.uk/2014/12/limit-amount-of-dependencies-you-use.html),
everything else can be an implementation detail leading to more flexible
and resilient code.

</p>

