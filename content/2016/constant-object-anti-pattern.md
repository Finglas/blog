Title: Constant Object Anti Pattern
Date: 2016-10-01
Author: Shaun Finglas
Tags: tutorial, programming
Slug: 2016/10/constant-object-anti-pattern

Most constants are used to remove magic numbers or variables that lack
context. A classic example would be code littered with the number 7.
What does this refer to exactly? If this was replaced with DaysInWeek or
similar, much clarity is provided. You can determine that code
performing offsets would be adding days, rather than a mysterious number
seven.

Sadly a common pattern which uses constants is the use of a single
constant file or object.

<script src="https://gist.github.com/Finglas/5a54e173296d81dcbdbfb8016f162150.js"></script>
The beauty of constants is clarity, and the obvious fact such variables
are fixed. When a constant container is used, constants are simply
lumped together. These can grow in size and often become a dumping
ground for all values within the application.

A disadvantage of this pattern is the actual value is hidden. While a
friendly variable name is great, there will come a time where you will
want to know the actual value. This forces you to navigate, if only to
peek at the value within the constant object. A solution is to simple
perform a refactor to move the variable closer to use. If this is within
a single method, let the constant live within the method. If a class,
let the constant live at a field level. Finally if the constant is used
across multiple classes, find a shared home and rely on a well thought
out namespace.

A similar issue regarding constants is the use of configuration files or
similar to set the values. While the const keyword is dropped in this
case, the object performs the same role. A public key, followed by a
value that is used. [The anti pattern in this case is treating all
values as requiring
configuration](http://blog.shaunfinglas.co.uk/2016/04/x-of-configuration-is-never-used.html).
Unless you need to change such values at runtime or based on deployment
models, inline constants are much preferred. Literal values, mainly
strings can often be left inline with limited downsides also. For
example, a fixed, relative file path is much better left inline. If you
are worried about lack of context, then the use of named arguments can
help.

<script src="https://gist.github.com/Finglas/16d8dd7c759a182b4eafb132d7f8fd78.js"></script>
Lessons
-------

-   Keep constants local to methods, or classes.
-   Avoid constant objects or files as these will become bloated and
    lack context.
-   Only introduce configuration for aspects that need or will change.
    Defer second guessing.
-   Use named arguments to add context for inline variables.