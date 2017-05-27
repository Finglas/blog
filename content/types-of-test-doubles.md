Title: Types of Test Doubles
Date: 2015-09-15 07:06
Author: Shaun Finglas
Tags: testing, http://schemas.google.com/blogger/2008/kind#post, unit-testing
Slug: types-of-test-doubles

*Mock* is an overloaded term in software development. Sadly this leads
to developers answering with "*mock it*" when a mock object may not be
the right solution. [Test
Doubles](http://xunitpatterns.com/Test%20Double.html) are a more general
term. I should try to use this naming more than I do at present - a goal
I aim to work towards. The result of choosing the wrong test double may
seem innocent but the effect will be a very different style of test
method, with increased coupling to implementation details. The following
definitions are ordered in terms of complexity and increased coupling.

#### Stubs

Provide canned responses. By their nature stubs would respond to
queries. Stubs allow you to test paths of the code that would be
otherwise difficult as they always provide the same answer.

#### Spies

Similar to a stub but with the addition that a spy records its actions.
When responding to a query or a command the spy keeps track of what
happened, how often and anything else relevant. The test can then
inspect the spy for the answer, deciding whether to pass or fail. Unlike
Mocks, spies play well with the Arrange-Act-Assert pattern. Spies let
you answer the question *has something happened* whereas Mocks tend to
lead you towards *how has something happened*.

#### Fakes

Fake objects tend to be used in higher level tests. These are fake
implementations of the object they are standing in for. A fake
repository would be implemented in a simple manner, instead opting for a
simple in memory hash table for its implementation. This allows tests to
be run with some confidence that the system will behave as expected.
Combined with [Contract
Tests](http://blog.shaunfinglas.co.uk/2015/07/the-benefits-of-contract-testing.html),
fakes can turbo charge the speed of your test execution while still
providing confidence.

#### Mocks

Similar to spies mocks are primarily in charge with recording what
happens. However while spies are silent in their nature relying on the
test to interrogate them, mocks differ by throwing exceptions if their
expectations are not met. Mocks natural partner is commands. Unlike
spies Mocks can struggle to fit into the Arrange-Act-Assert pattern. Of
all the test doubles Mocks are the most coupled to implementation
details so their use should be limited.

</p>

