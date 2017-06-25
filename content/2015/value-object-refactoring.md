Title: Value Object Refactoring
Date: 2015-02-03 20:36
Author: Shaun Finglas
Tags:  programming, tutorial
Slug: 2015/02/value-object-refactoring

After extract method or extract class introducing a value object is one
of the most powerful refactorings available. A value object encapsulates
a value or concept within your domain. While the term is more formally
known from Domain Driven Design, DDD is not a pre-requresite for use.
Introducing a value object can be applied to any code base.

Some excellent examples of value objects would include `CustomerId`,
`Money`, `OrderId` and `PhoneNumber`. These could all be identified as
integers, strings or decimal numbers, but doing so would lead to a
series of downsides.

Making use of primitive data types to express concepts within an
application is a code smell known as primitive obsession. Replacing
primitives with value objects is the solution to this smell.

#### Primitive Obsession

-   Duplication will be thrown throughout the codebase. Both in the form
    of simple guard clauses, or core domain logic.
-   More tests are required. This ties into the duplication above.
-   Your domain lends itself towards an anaemic model, full of utility
    classes that operate upon state.

#### Solution

<script src="https://gist.github.com/Finglas/e36d0ffc473d1dc12088.js"></script>
The implementation of `PersonalDetails` would be straight forward to
begin with.

<script src="https://gist.github.com/Finglas/5a37ae3fe12211d2b527.js"></script>
Over time areas of logic can slowly migrate and move towards the class.
In most IDE's, simply wrapping a primitive type as the first step can be
carried out in a few keystrokes.

The constructor performs basic validation on a technical level. Once
complete we can carry out any domain logic. Likewise the behaviour
attached to this object (hidden for beravity) would include various
domain specific logic. For example, when changing surnames any leading
or trailing whitespace is removed.

One recommendation would be to expose the underlying primitive. In this
example `ToString` has been overridden to return the string value that
is being used. This should be a read only operation idealy, and enables
the object to play nicely with third parties. Such use cases for this
would be serialization, or writing the value to a persistent store.

Equality (and hashcode in this case) should also be implemented. This is
because the nature of value objects allows them to be equal to other
instances that share the same value, despite being different references
in memory. The beauty of this is that value objects can be used as
needed, no need for injection or other patterns.

#### Benefits

-   Removes duplication. Only the object in question will be the source
    of truth.
-   Less tests need to be written. As the duplication has been removed,
    only one test per behaviour is required. Rather than duplicating
    checks for validation or formatting this can be contained to the
    object. As the rest of the system deals with our value object, we
    don't have to worry about dealing with an invalid representation.
-   In statically typed languages you can lean on the compiler. It's
    impossible to supply anything other than PersonalDetails when we ask
    for an instance. Even for dynamic languages, the stack trace
    presented upon error would be far more useful than had a primitive
    type been provided.
-   The surface area of mis-configuring arguments is smaller also.
    Previously we would accept two strings that are order dependant. Now
    this configuration has been reduced to a few areas.
-   Using the example above, we can now rely on class pre-conditions to
    simplify our expectations when working with this type. Given any
    instance of `PersonalDetails` we can be sure that the forename and
    surname are never null or empty, and that each personal details
    instance will have a forename of at least one character long. A
    simple string can never guarantee such conditions.
-   Making value objects public generally makes sense. This provides an
    excellent seam for testing and integration.
-   The introduction of a value object plays nicely with my [three basic
    steps to code
    quality](https://blog.shaunfinglas.co.uk/2014/12/three-steps-to-code-quality-via-tdd.html).