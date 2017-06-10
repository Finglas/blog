Title: Guard Clauses and Assertions
Date: 2015-02-01
Author: Shaun Finglas
Tags: code-quality, tutorial
Slug: 2015/02/guard-clauses-and-assertions

Two simple techniques to increase code quality, resilience, and ease
debugging scenarios is to use guard clauses effectively and ensure that
assertions are used liberally.

#### Guard Clauses

-   Any public method should perform guard clauses to ensure pre
    conditions are met.
-   Ensures the code's invariants are not broken.
-   Throw exceptions, because these are exceptional issues.
-   Developer and user assistance as it is possible for these clauses to
    fail at runtime.

<script src="https://gist.github.com/Finglas/5b784bd2782d1478fa40.js"></script>
Here we enforce that any `PersonalDetails` instance has a forename and
surname. A forename must also be at least one character long. As long as
these conditions are met, we finally assign the values internally. Guard
clauses should also be used on dependencies that are services, checking
that a service is not a null instance for example.

#### Assertions

-   Used within private methods/functions where required.
-   Should be used for situations that should never happen, e.g the
    presence of a bug or invalid scenario.
-   Developer only assistance, the user should never see these ideally
    because automated/manual testing should have detected them.
-   Usually removed for release builds, though open to debate, best to
    judge on context. Is it better for the program to crash and inform
    the user, or carry on in an invalid state?
-   Great for documenting assumptions, e.g. code a level above ensures
    object is in a certain state.

<script src="https://gist.github.com/Finglas/2a59051e9c3d566185f1.js"></script>
While this method is private, we have essentially stated that we take no
responsibility for validating that a name has been provided. This is the
concern of another part of the code (the constructor in this case).
However this simple assert statement means that if the method is used in
a different manner, it will fail spectacularly at runtime. This will
point at the incorrect use of the method and allow the developer to make
the required changes.

##### Summary

Code quality will improve because less invalid scenarios should be
allowed to happen. Due to clauses and assertions always being present
they go hand in hand with automated tests, often catching scenarios that
automated tests may miss. Debugging is easier because the stack trace
points you at the source of the problem, rather than an initial problem
hidden in layers of exceptions caused by invalid state. While applying
clauses and assertions increases lines of code, they are easy to
implement, and the return on investment is high. There are no excuses
not to use them.