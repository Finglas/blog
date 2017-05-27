Title: Achieving more Isolated Unit Testing
Date: 2014-08-10 14:13
Author: Shaun Finglas
Tags: best-practices, http://schemas.google.com/blogger/2008/kind#post, tdd, unit-testing
Slug: achieving-more-isolated-unit-testing

*Good* unit tests should be:

-   fast
-   independent
-   well focused
-   *isolated*

If your unit tests are slow, you're not gonna run them as often as you
should. Therefore one of the main benefits of unit testing is lost - the
lack of instant feedback.

Each of your unit tests should be independent. The order in which you
run your tests should not matter. By keeping your tests focused you
should be able to refactor, add new code and not have the majority of
your tests fail. If you change class A, you would expect class A's tests
to fail at worst. If other tests outside of this scope fail, your tests
are not focused enough. This lack of focus leads on to isolation.

Tests should be isolated from other dependencies. Dependencies such as
other classes should not affect each other, providing the contract
between the code is maintained. Likewise the file system, the web and
databases should not be involved anywhere with your unit tests. If any
of these dependencies come into play, you're not unit testing.

At Codeweavers we have around **ten thousand tests**, with unit tests
accounting for the majority of these tests. Naturally this means every
now and then we take time to do a bit of house keeping regarding our
tests.

One thing we noticed was that some of our tests were taking longer to
run than other tests. They were taking anywhere from one to ten seconds.
Ten seconds for a unit test is a huge time. During this period we could
have run hundreds of other tests! As for why these tests took so long to
run? Easy. They were not unit tests. Code had been added that broke that
layer of isolation. Some tests were hitting real web services for
example.

In order to be fully isolated I proposed a simply solution. **Unplug the
network cable**. Any tests that failed would not be unit tests. This
gave us one of two options:

-   Refactor the code - remove or stub the dependencies
-   Promote the tests to integration/regression tests (only run prior to
    check in)

You can take this idea one step further. Next time you run your tests
try running them from a different location. Any tests that fail are
relying on relative/hardcoded paths and will need attention.

After performing this task on our codebase we had some failures. The
nice thing about solving these failures is that our tests now run a lot
faster. Our slowest tests are now end to end regression tests which are
only run prior to check in or by our CI server. We've also made sure
that from a disaster recover point of view, we can continue developing
locally even if our CI server is not present.

So take the experiment. Unplug your computer from the network. How many
of your "unit tests" fail?

</p>

