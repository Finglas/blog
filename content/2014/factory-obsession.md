Title: Factory Obsession
Date: 2014-12-01
Author: Shaun Finglas
Tags: unit-testing, tutorial
Slug: 2014/12/factory-obsession

I have noticed a pattern over the years with developers of which I will
refer to as factory obsession. Everything is a factory or builder
object. To some, the use of `new` is **banned**.

------------------------------------------------------------------------

Consider a object that is responsible for some business logic and
finally saves the result to a persistent store.

<script src="https://gist.github.com/Finglas/8f4f9dba2320e3d5ad57.js"></script>
Message here is a value object, however the new can cause an odd fear
within developers. Therefore a factory is required. Or is it? How can we
test the repository is updated with the new message without reference
equality?

<script src="https://gist.github.com/Finglas/4b43d5af771b9d13701c.js"></script>
An example test in C\#, using the Mock framework with this newly
introduced factory would look like:

<script src="https://gist.github.com/Finglas/44cc9e70e2f9f5b47528.js"></script>
This fear of `new` is wrong.

-   Instantiating value types is a good thing.
-   Instantiating entities is a good thing.
-   Instantiating services can depend - if the service is expensive we
    don't want to create lots of instances on a whim.

Here the factory offers nothing but a more strongly coupled solution.

If we ignore the factory the test becomes easier to write. To do this
equality should be correctly implemented upon the message value type. I
have questioned this in the past but for correct Domain Driven Design
(DDD) semantics this is a good thing to follow.

<script src="https://gist.github.com/Finglas/91f346d41ba5055891c4.js"></script>
We can take this further though. If we ditch the factory idea all
together and replace the repository with a fake implementation we can
have an even cleaner test fixture. You would still need equality but the
design retains its flexibility.

<script src="https://gist.github.com/Finglas/a8513ecc8a7790d12ee2.js"></script>
Factories have their place, like all design patterns, however they
should be introduced as part of the refactor step in most cases. Hiding
the new keyword is not a goal. The fact that mocking frameworks default
to reference equality shouldn't force you to make a more complicated or
coupled solution to a problem.