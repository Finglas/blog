Title: Given When Then Scenarios vs Test Fixtures
Date: 2016-06-07 06:49
Author: Shaun Finglas
Tags: testing, http://schemas.google.com/blogger/2008/kind#post, unit-testing
Slug: given-when-then-scenarios-vs-test-fixtures

There are two common ways of writing automated tests which apply from
unit to acceptance tests. These are typically known as test fixtures and
Given-When-Then scenarios.

#### Test Fixture

-   Traditional method of writing tests.
-   The common JUnit/NUnit approach. Other languages have very similar
    concepts.
-   Single test fixture with multiple tests.
-   Test fixture is usually named after the subject under test.
-   Can grow large with many test cases.
-   Works well with data driven tests.
-   Suited to [solitary
    tests](http://blog.shaunfinglas.co.uk/2014/12/a-unit-is-not-always-method-or-class.html)
    such as integration tests where GWT syntax would be verbose or hard
    to include.

#### Example

<script src="https://gist.github.com/Finglas/7748cf098415494c99ecaa0777eacacd.js"></script>
#### Given-When-Then

-   Behaviour driven approach (BDD style).
-   Made popular by tools such as RSpec.
-   Single test fixture per behaviour.
-   Test fixtures named after the functionality being tested.
-   Often nested within other test fixtures.
-   Smaller test fixtures but more verbose due to fixture per
    functionality.
-   Easy to see why a test failed due to naming convention - assertion
    message is optional.
-   Suited to [sociable
    tests](http://blog.shaunfinglas.co.uk/2014/12/a-unit-is-not-always-method-or-class.html)
    where the focus is on behaviour.
-   `Given` forms the pre-condition of the test.
-   `When` performs the action.
-   `Then` includes one or more related assertions.
-   GWT can be difficult to name in some cases, often more thought and
    discussion can be required around good naming conventions.
-   Can act as useful documentation on how the code is meant to
    function.

#### Example

<script src="https://gist.github.com/Finglas/8d5b8fbc789acbe829d06312559a5d3a.js"></script>
#### Lessons

-   No single way of writing automated tests is better.
-   Favour single test fixtures for integration tests.
-   The core of your tests can use GWT style.
-   Mix and match where appropriate however.
-   Your choice of tooling and language may influence your approach.

</p>

