Title: Three Steps to Code Quality via TDD
Date: 2014-12-01
Author: Shaun Finglas
Tags: 3-steps-code-quality, tdd
Slug: 2014/12/three-steps-to-code-quality-via-tdd

Common complaints and problems that I've both encountered and hear other
developers raise when it comes to the practice of Test Driven
Development are:

-   Impossible to refactor without all the tests breaking
-   Minor changes require hours of changes to test code
-   Test setup is huge, slow to write and difficult to understand
-   The use of test doubles (mocks, stubs and fakes is confusing)

Over the next three posts I will demonstrate three easy steps that can
resolve the problems above. In turn this will allow developers to gain
one of the benefits that TDD promises - the ability to refactor your
code mercifully in order to improve code quality.

#### Steps

1.  [Stop Making Everything
    Public](http://blog.shaunfinglas.co.uk/2014/12/stop-making-everything-public.html)
2.  [Limit the Amount of Dependencies you
    Use](http://blog.shaunfinglas.co.uk/2014/12/limit-amount-of-dependencies-you-use.html)
3.  [A Unit is Not Always a Method or
    Class](http://blog.shaunfinglas.co.uk/2014/12/a-unit-is-not-always-method-or-class.html)

Code quality is a tricky subject and highly subjective, however if you
follow the three guidelines above you should have the ability to
radically change implementation details and therefore improve code
quality when needed.