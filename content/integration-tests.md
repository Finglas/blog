Title: Integration Tests
Date: 2015-07-21 18:22
Author: Shaun Finglas
Tags: integration-testing, testing, http://schemas.google.com/blogger/2008/kind#post, unit-testing
Slug: integration-tests

It is well documented you need a balance between different categories of
automated tests. The split is usually in the form.

-   70% unit
-   20% integration
-   10% acceptance

While unit tests make up the majority of tests, there is a limit to
their effectiveness. As soon as you leave the system boundary you need
integration tests. Examples of when integration tests are required is
code that interacts with databases, web services or the file system.

These integration tests should not test logic, this is a mistake. They
will become brittle and slow to execute otherwise. Instead of checking
domain logic, test at a lower level. Go as low as you can without
leaking implementation details of the subject under test. By going as
low as possible you will radically reduce the number of integration
tests required. Less tests means easier maintenance. Less tests also
means faster tests.

#### Example

Assuming a SQL database, invoke the repository and test as lightly as
possible. Do not indirectly test this repository by invoking the code
higher levels in the stack. Avoid concerning yourself with what is
happening behind the scenes. Simply test that you can insert a record,
and retrieve the newly inserted record. Any other code that is involved
at higher levels can suffice at a unit level.

Assertions should be loose enough to verify that the code is working,
but not asserting basic correctness. In other words prefer assertions
that check for the presence of results, rather than what those results
look like. If the value is of concern, convert into a fast, isolated
unit test.

#### Integration Tests are a Scam

The term *Integrated Tests* is my preference given that [integration
tests are a
scam](http://blog.thecodewhisperer.com/2010/10/16/integrated-tests-are-a-scam/).
This slight change in terminology helps keep these tests focused. Rather
than spiraling out of control, they are small in number and simply
verify that "*something is working*". This is done by pushing all tests
of logic to the unit level.

The key point here is that integration tests are required. Strongly
resist the urge to write all tests at the integrated level. Likewise do
not fall into the trap that thinking all tests must be done at the unit
level. The key here is balance.

There is a fatal flaw with integration tests however. They can be wrong.
Given tests at a unit level will stub out anything that is out of
process, how do you stop such tests falling out of sync with the real
implementation? This is where [Contract
Tests](http://blog.shaunfinglas.co.uk/2015/07/the-benefits-of-contract-testing.html)
come into play.

</p>

