Title: You Still Need Manual Tests
Date: 2015-07-28 20:48
Author: Shaun Finglas
Tags: http://schemas.google.com/blogger/2008/kind#post, acceptance-testing, unit-testing
Slug: you-still-need-manual-tests

This blog has numerous examples of why unit,
[integration](http://blog.shaunfinglas.co.uk/2015/07/integration-tests.html)and
[contract](http://blog.shaunfinglas.co.uk/2015/07/the-benefits-of-contract-testing.html)testing
is essential. However you still need manual tests. It is foolish to
believe that all testing can be covered by automated tests despite the
bias in this area.

#### Why?

-   Manual tests can catch anything you may have missed at an automation
    level.
-   Manual tests can be unique. Use exploratory testing to try
    *different* scenarios.
-   Manual tests that fail become automated tests, so they can never
    regress.
-   Manual tests exercise the full stack. Many areas such as DI
    conventions, logging, and other framework related configuration are
    better suited to manual verification.
-   UI changes require visual verification - automation is near
    impossible here.

#### More Than Just Functionality

Over the years, manual testing has caught numerous bugs, issues or
things I've just plain missed. When you are deep in a problem it can be
hard to see the wood for the tress. A second party manually testing
provides an unbiased check of your code for a second time.

The key with manual tests is to ensure any issue is converted into an
automated test. This offsets the fact that manual testing is expensive
both in terms of time and cost. By doing so any regressions will be
prevented.

QA includes more than functional testing. Security, performance and
usability to name a few are equally important. Do not avoid the manual
test step. Automated tests are only as good as the tests themselves.
Embrace manual and automated testing for the best of both worlds.

</p>

