Title: Randomly Generated Values in Tests
Date: 2015-04-09 19:20
Author: Shaun Finglas
Tags: testing, http://schemas.google.com/blogger/2008/kind#post, tdd, unit-testing
Slug: randomly-generated-values-in-tests

The use of randomly generated test data seems like a good thing at first
glance. Having worked with several teams that have used this concept I
generally discourage the practice. Consider a simple method that joins
together two strings. A test using random values may look like this.

<script src="https://gist.github.com/Finglas/a52ff8867d6af0757059.js"></script>
#### Problems

##### Harder to Read

While this is a toy example to demonstrate the problem, in more
realistic scenarios the lack of literal values harms the readability of
the tests. It is worth noting the lack of literals causes more lines of
code as anything that has importance needs to be stored in a variable or
field. My biggest concern is when assertions start to become complicated
or even worse, duplicate production code in order to pass. If we wish to
treat tests as examples, this is pretty poor.

##### Edge Cases

Generating a random string seems easy enough. Overtime the edge cases in
question start to ramp up. You have whitespace, special characters, new
lines, numbers and much more to worry about if you wish to do this
properly. The code to actually generate random values is often shared
via inheritance or composition, this makes changes tricky and dangerous
as you can inadvertently change more than one test when modifying this
common code. If the two inputs need to be different then you could
potentially generate the same string each time, leading to flaky tests
if you're not careful.

##### Psuedo Random

The random aspect of these tests can confuse developers. In the example
above, there is only ever one value for each variable. In other words
this test can run many times locally and pass, but fail when executed
elsewhere. There may be a subtle bug that is only found after the code
is declared complete. This issue often causes failures in the build, at
which developers declare "*it's just a random failure*" before
re-triggering the build because a value may be invalid for a specific
scenario.

##### Date/Times can be Tricky

Date/Times are hard enough as it is. Trying to randomly generate these
is not worth the hassle.

#### Solution

My recommendation is to rely on literal values or [value
objects](http://blog.shaunfinglas.co.uk/2015/02/value-object-refactoring.html)
where possible, these make the test much more readable and act like an
example or specification. Additionally their use allows the inline
variable refactor to take place, meaning shorter, conciser tests.

<script src="https://gist.github.com/Finglas/35666813e84b920420e3.js"></script>
##### Test Cases/Parameterized Tests

If you wish to test similar scenarios in one go then [test
cases](http://www.nunit.org/index.php?p=testCase&r=2.5) can help. This
is usually the case when you cannot name a test easily because the
functionality is the same as an existing test.

##### Bugs

The assumption that randomly generated tests catch bugs and cover more
ground is wrong. If you really do discover a bug after manual testing or
on a live system just write a new test exposing that bug and fix it.
Thinking you cover more scenarios by using random values is false.

##### Property Based Testing

I cannot comment on [Property Based
Testing](http://www.scalatest.org/user_guide/property_based_testing)
fully, but this is certainly an interesting area and does not suffer
from the issues above. Worth looking into.

##### DRY?

This solution certainly violates DRY. There is clear duplication. If
this was production code I would remove it, however for tests my stance
for a long time has been to allow this duplication to remain.
Readability and expressiveness is much more important. There are valid
times when duplication between tests is a bad thing. While this simple
example doesn't suffer from this problem [I will expand on how to keep
your tests expressive but DRY in a future
post](http://blog.shaunfinglas.co.uk/2015/04/dry-vs-damp-in-tests.html).

</p>

