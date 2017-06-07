Title: Limit the Amount of Dependencies you Use
Date: 2014-12-01
Author: Shaun Finglas
Tags: 3-steps-code-quality, tdd
Slug: 2014/12/limit-amount-of-dependencies-you-use

Part two of my [Three Steps to Code Quality via
TDD](http://blog.shaunfinglas.co.uk/2014/12/three-steps-to-code-quality-via-tdd.html)
series and ties very closely into step one, limiting the visibility of
your classes.

-   Part 1 - [Stop Making Everything
    Public](http://blog.shaunfinglas.co.uk/2014/12/stop-making-everything-public.html)
-   Part 3 - [A Unit is Not Always a Method or
    Class](http://blog.shaunfinglas.co.uk/2014/12/a-unit-is-not-always-method-or-class.html)

------------------------------------------------------------------------

The more dependencies you use the more your tests are coupled to
implementation.

Consider the constructor below.

<script src="https://gist.github.com/Finglas/78bf9d35ef691f642d29.js"></script>
Code like this is common and difficult to work with. Each dependency you
inject requires a mock, stub or fake when writing tests. This couples
the implementation to the test despite the use of interfaces or abstract
base classes.

Every public dependency here increases the resistance for change. If I
was to remove the builder and replace with some equivalent code to
construct a `Bar` instance, the test would fail despite being
functionally equivalent. This is wrong.

[A constructor is part of the public API of an object even though this
is not detailed as part of
interfaces](http://blog.ploeh.dk/2011/02/28/Interfacesareaccessmodifiers/)
in languages such as C\#/Java. Every collaborator that is provided by a
constructor should have a reason for being exposed as part of the the
public API.

#### What Are Good Dependencies?

Good dependencies are things that are out of your control or process
such as:

-   Databases (repositories, queries)
-   Web Services
-   Third Parties
-   Strategies (anything that needs to change dynamically)

As part three of the series will detail - isolate your tests from these
sorts of dependencies, don't isolate your code from itself.

##### Doesn't this mean you end up with God classes?

No. As step one detailed - small, well focused classes are a good thing.
They just should remain as implementation details.