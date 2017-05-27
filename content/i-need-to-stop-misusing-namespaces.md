Title: I Need to Stop Misusing Namespaces
Date: 2015-04-23 18:51
Author: Shaun Finglas
Tags: best-practices, http://schemas.google.com/blogger/2008/kind#post, programming, development
Slug: i-need-to-stop-misusing-namespaces

At the recent [NSBCon](https://skillsmatter.com/conferences/6198-nsbcon)
one interesting question that came about was how to structure a project.
The panel consisting of various speakers had no answer, after all this
is dependant upon the project in question. Therefore there is no right
or wrong answer.

However one point they were in unison about was splitting the domain and
technical implementation of a project apart by the correct use of in
namespaces.

This is not the first time I've come across this, but I find myself
breaking this principle on a regular basis. For example a typical
project I work on looks like the following.

<script src="https://gist.github.com/Finglas/0b32973c8a339f283c60.js"></script>
#### Problems

-   The namespace reflects a technical implementation detail, and not
    the problem domain.
-   Using Foo as an example, here the namespace is duplicated within the
    name of the types, which in turn defeats the point of namespaces.
-   Another issue is that the types can be much longer than they need to
    be, which is often a criticism of enterprise software development,
    when the names of objects roll off the screen because they contain
    so many patterns or conventions.

#### Solution

Use namespaces for related domain responsibilities. In turn, group
together the objects and types that are used together.

An example of a better solution therefore would be:

<script src="https://gist.github.com/Finglas/b29e133fad03dd9430a7.js"></script>
##### Benefits

-   Things that change at the same rate, would live logically next to
    things that also need changes. In other words if I update the
    FooViewModel, chances are I'll need to update views or controllers.
-   Less typing if you don't suffer a namespace clash!
-   You can still prefix the namespace where required, e.g.
    Foo.Controller if you have a clash or prefer the readability.
-   Shorter type names!

While this is the ideal way of structuring our applications it's not
always possible. Some coding conventions actually encourage the first
example, and depending on the configurability of certain frameworks this
may prove difficult. That aside, I'll be making a strong push towards
structuring my projects correctly going forwards.

</p>

