Title: The QA Test Matrix
Date: 2017-04-03 06:55
Author: Shaun Finglas
Tags: testing, http://schemas.google.com/blogger/2008/kind#post
Slug: the-qa-test-matrix

Historically teams I've worked with have taken a few varying approaches
when designing tests against acceptance criteria. One is to have the
business define the feature, while the team help define the acceptance
criteria. Ultimately the business gets the final say if they agree, and
further acceptance criteria is either added or removed. The strength of
this approach is everyone is involved with the process so nothing is
missed or misunderstood. The biggest flaw with this style is that the
documentation produced is often verbose, using wordy Given-When-Then
scenarios. Using this plan a test plan is then created, mapping tests to
acceptance criteria.

An alternative approach is have the business define both the feature and
acceptance criteria while the team come up with a corresponding test
strategy. This more technical approach allows for a separation of
testing activities and test categories. Finally the test plan is
replayed back to the business and correlated against acceptance
criteria. A negative of this approach is not everyone is involved with
the task at the same time. This means there can be some disconnect with
what the business is actually asking for. Both approaches work though
they can yield mixed results on a case by case basis.

#### The QA Matrix

I've recently been introduced to the concept of a testing/QA matrix,
which is a far more condensed and simplified solution. It has the
benefit of the whole team being engaged, while producing nothing more
than a simple table that can fit comfortably on a A4 page. The left hand
column includes each condition of acceptance, while the other columns
should have a mark to indicate the type of test that will cover this
functionality. An example is below.

         Unit Integration Acceptance Contract Manual
    COA   X
    COA           X                             X
    COA   X
    ...

The beauty of this matrix is that at a glance you can see where you
testing efforts lie. If too much occurs on the right of the matrix you
may need to re-consider and question your approach. Is there a way to
limit the more expensive style of tests and still gain confidence? Other
questions can arise around test coverage and whether higher level tests
are needed.

When producing this matrix the whole team including the business should
be involved. By having everyone together, decisions can be made quickly
with everyone in agreement. Additionally it allows debate and discussion
around how each feature should be tested.

For higher level tests these can be directly translated into automated
tests. While the lower level tests need to confirmed at a later date
once the code is complete.

Along side the QA matrix it may be worth while adding a simple diagram
of the components that will be involved such as web servers, databases
and so on. This can aid discussion and highlight hot spots for changes
or tests.

Finally for demonstration to the business the matrix can be used as a
form contract for signing off functionality. Once the feature is
complete it is simply a case of finding the corresponding tests,
confirming their existence and making a note of the commit that included
them.

</p>

