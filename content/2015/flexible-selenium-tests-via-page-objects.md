Title: Flexible Selenium Tests via Page Objects
Date: 2015-03-29 10:01
Author: Shaun Finglas
Tags: selenium, testing, http://schemas.google.com/blogger/2008/kind#post
Slug: flexible-selenium-tests-via-page-objects

A fast, automated suite of unit and integration tests are not enough. At
some point you'll need to test your presentation logic. Ideally your
domain/business/game logic is stubbed so all you'll need to do at this
point is check that the presentation is complete. For example, does view
X load view Y? Does an error message appear when an error is raised?

With web sites and web applications the standard tool to use is the
excellent [Selenium](http://docs.seleniumhq.org/). The problem with UI
tests in Selenium is they are often slower to write. Not only this the
maintenance cost of such tests can often be much more expensive that
other styles of tests. If the cost of such tests is high, the likely
hood of developers writing UI tests is low. In my experience there are
three types of UI tests in use.

-   ### Low Level

    Here UI tests are wrote directly against Selenium. This low level
    approach means tests are scattered with assertions and UI details.
    For example element locators such as divs and ids will be used with
    methods on the Selenium driver in question. Despite this low level
    approach such tests are often quick and dirty to create. The
    downside to this style of test is that as the volume of tests
    increase, the cost of maintenance can become very costly. A simple
    UI change can cause a ripple that will cascade through many test
    cases.

    <script src="https://gist.github.com/Finglas/aae1cd850fc37403dbb8.js"></script>
-   ### Browser Abstraction

    The next level up from direct use of Selenium's driver is to create
    a facade around the browser or UI itself. For example rather than
    duplicating the steps to log in within each test you could create a
    method `PerfromLogin(...)` which each test could make use of.
    Another example would be abstracting messier details of UI
    automation such as clicking a button and waiting for an event. This
    style of test has the benefits of low level tests but gives some
    flexibility when it comes to maintenance. The downside with this
    facade approach is that UI changes can still cause havoc, as each
    test in question will be tied to the UI elements directly.

    <script src="https://gist.github.com/Finglas/1063a11c30bc3e7290d8.js"></script>
-   ### Page Objects

    Taking the browser abstraction to the next level, [page objects are
    an abstraction over the UI
    itself](http://code.google.com/p/selenium/wiki/PageObjects). These
    high level tests are wrote in terms of the domain, rather than
    implementation details. There is of course one place where each page
    object is bound to a UI element, but as each test uses an object,
    rather than element locators you only have to change one place when
    your UI changes. Unlike the previous two styles of tests, page
    objects incur the most amount of code, though for more than a
    handful of tests this style of UI acceptance test will pay for
    itself in no time.

    <script src="https://gist.github.com/Finglas/6d512240848359c12bc2.js"></script>
    With the above example the `LogInPage` object will be bound to UI
    locators. This will vary based on programming language, but using
    C\# as an example each property would have a specific attribute to
    link up each element. The domain specific methods such as `Username`
    will fill in the correct UI element with the provided value. By
    writing the objects in a fluent interface style, you can achieve QA
    friendly tests which are easy to debug when they go wrong.

A more fleshed out [example of the Page Object pattern can be found on
Github](https://github.com/Finglas/Playground/blob/master/PageObjects/PageObjects/PageObjects.cs).

Choose a style based on context. Given more than a handful of tests then
page objects are worth the extra cost, the ability to evolve your UI
while maintaining end to end tests is worth some additional complexity
at first.

</p>

