Title: Stop Making Everything Public
Date: 2015-02-10 20:12
Author: Shaun Finglas
Tags: best-practices, http://schemas.google.com/blogger/2008/kind#post, 3-steps-code-quality, tdd
Slug: stop-making-everything-public

Part one of my [Three Steps to Code Quality via TDD
series](http://blog.shaunfinglas.co.uk/2014/12/three-steps-to-code-quality-via-tdd.html).

-   Part 2 - [Limit the Amount of Dependencies you
    Use](http://blog.shaunfinglas.co.uk/2014/12/limit-amount-of-dependencies-you-use.html)
-   Part 3 - [A Unit is Not Always a Method or
    Class](http://blog.shaunfinglas.co.uk/2014/12/a-unit-is-not-always-method-or-class.html)

------------------------------------------------------------------------

We always default to public class when creating a new class. Why? The
concept of visibility in OO languages appears very early on in
programming books, yet more often than not most of the classes we create
default to public visibility.

[@simonbrown](https://twitter.com/simonbrown) stated that each time you
make something public you need to make a donation to charity. In other
words we should think more about why the class we are making should be
visible to everyone. I really like this idea that the use of the public
keyword should be a well thought out decision.

Server side development has a part to play in the lack of concern given
to visibility issues. Library or framework developers on the other hand
must carefully consider what is part of the public API. Any changes made
after are considered breaking and require careful consideration. Yet in
the land of server side development this is see as a non issue. This is
wrong. If we treat our tests as consumers of our public API, constantly
updating them or modifying them should be a warning symbol.

Use internal or private classes for details and public classes for your
API. The beauty of this is that TDD drives your public API, which should
be fairly stable. Internally however you want the ability to refactor
without a suite of tests breaking, otherwise what is the point of
writing automated tests?

Implementation details are introduced as part of the refactor step.
Ideally they should never be introduced without a passing test in place,
as previously the simplest possible thing should have been done.

#### What Should be Public Then?

-   Application services (use cases) that adapters talk to.
-   Adapters - controllers, console application, presentation layer.
-   Domain concepts - money or customer for example
-   Strategies - things you need to inject, repositories, third parties

##### Doesn't this lead to god classes?

No. As part of the TDD cycle, when refactoring you can extract
implementation details. There is no reason why the public types should
suffer.

##### Doesn't this lead to large tests on the public types?

No. You'll use less test doubles (stubs, mocks, fakes) and in turn
reduce setup. For any logic that appears to be painful or common you can
introduce domain concepts which can and should be public. The tests can
be wrote at this level then. Just find the right test seam.

##### What is the benefit?

The ability to switch implementation details without breaking public
functionality. A whole world of refactoring options are available,
inline method, extract method, extract class, inline class, replace with
library and so forth. As long as the tests pass, you can be confident.

</p>

