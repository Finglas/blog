Title: Acceptance Testing need not use the Full Stack
Date: 2015-02-10 20:15
Author: Shaun Finglas
Tags: best-practices, http://schemas.google.com/blogger/2008/kind#post, acceptance-testing, retro
Slug: acceptance-testing-need-not-use-the-full-stack

-   Joined a team with thousands of unit tests (\~10k)
-   But bugs still got through our QA process
-   How could this be?
-   Team had a small number of full end to end live service tests
-   So my answer was to just increase the number of these
-   Surely this would solve our problem?
-   Not quite
-   The maintenance of these tests were a great burden
-   Each day many tests would fail, but nothing would be "broken".
-   Data would have changed in the DB
-   The UI could have changed
-   The browser could have been slightly slower
-   And so on

#### Solution

-   Delete the majority of live service tests - limit the tests to the
    core user journey through the application
-   As long as the pages load up, without an error we shouldn't care
-   Stopped testing logic or behaviour - made the tests loose, e.g. as
    long as value is not null or empty we are OK, we don't actually care
    what the value is.
-   Made use of [contract
    testing](http://martinfowler.com/bliki/IntegrationContractTest.html)
    to substitute boundaries with in memory fakes, e.g. persistent
    storage. This allowed fast, stable acceptance tests to be run
    against the system without the brittle nature described above.

##### Benefits

-   Small handful of live service tests (using real DB, UI) caught the
    majority of the serious flaws that snuck through
-   Future bugs were missing unit tests thanks to contract testing
-   Faster to write
-   Easier to debug
-   Faster to execute!

The key point was the use of contract testing. Without contract testing,
writing automated acceptance tests is a pretty awful process.

Data requires setup and tear down. Any data changes can break your tests
and the UI is often in flux.

By substituting the UI layer, or the DB access with fakes such as a
console view, or in memory hash table, your tests can still cover the
whole stack, but in a more stable, bite size manner. You simply test
your real view or data access separately to prove they work, and can in
fact be swapped out thanks to the [Liskov Substitution Principle
(LSP](http://en.wikipedia.org/wiki/Liskov_substitution_principle)) by
running the same suite of tests against your fakes!

I'll be expanding on how and what contract testing is in a future post.

</p>

