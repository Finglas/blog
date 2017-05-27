Title: Write Assertions First
Date: 2016-03-01 08:09
Author: Shaun Finglas
Tags: testing, http://schemas.google.com/blogger/2008/kind#post, tdd, unit-testing
Slug: write-assertions-first

Writing a test as part of the TDD process is simple.

1.  Arrange
2.  Act
3.  Assert

Many individuals recommend the process be reversed. Write assertions
first. Then write the steps to perform the action. Followed by the
required setup to complete the action.

1.  Arrange
2.  Act
3.  Assert

#### Simplicity

You will write just enough of the test to do the job. Its not far from
doing TDD on the test itself. Using staticily compiled languages you
would see compile time errors while performing this step. As you are
writing the test in reverse this is normal and expected. Most text
editors or IDE's can ease this process.

Implement just enough of the test to do your job. The opposite of this
is large, copy/paste tests that require lines of setup code that can
safely be removed or reduced.

#### Meaning

You end up naming variables with more meaning. With a traditional
approach variables can lack true, descriptive names. They are often
called `result` or similar. By working in reverse you force yourself to
think of what you are asserting upon. This forces better names out in
the process. An example would be `orderTotals` if the purpose of the
assertion was to check if the total of an order was as expected.

Writing assertions first can feel awkward but the benefits of this
change are well worth the initial slowdown.

</p>

