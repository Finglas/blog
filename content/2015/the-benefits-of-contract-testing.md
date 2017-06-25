Title: The Benefits of Contract Testing
Date: 2015-07-01
Author: Shaun Finglas
Tags: testing, contracts, unit-testing
Slug: 2015/07/the-benefits-of-contract-testing

[I previously claimed that you need some integrated tests but as few as
possible](https://blog.shaunfinglas.co.uk/2015/07/integration-tests.html).
There are huge benefits to this approach, but there is a problem. How do
you stop your test doubles falling out of line with the real
implementations? The answer is to use Contract Tests.

#### Steps

1.  Create a base test fixture, this is where your tests live. All
    assertions belong here.
2.  Subclass this base class with each implementation.
3.  Override each setup step to provide the implementation that is to be
    tested.
4.  All tests should pass for each instance.

#### Example

In this example there is a SQL repository and an in memory repository.
It is not possible to change either in any manner that causes them to
behave differently. We can safely use the in memory repository for
tests, with confidence that the test double matches the contract of the
real implementation.

<script src="https://gist.github.com/Finglas/63a042dd2a20487410ab.js"></script>
The test double implementations can be executed on every test run. While
real implementations can be relegated to execution prior to commit or
during continuous integration. This trade off allows for fast feedback
cycles while ensuring all tests are run against production like
implementations.

#### References

-   [Contract
    Tests](http://blog.thecodewhisperer.com/2009/10/08/who-tests-the-contract-tests/)
-   [No Mocks
    Example](https://github.com/arlobelshee/ArsEditorExample/blob/master/SimulatableApi.Tests/FileSystemCanLocateFilesAndDirs.cs)