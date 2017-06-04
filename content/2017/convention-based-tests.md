Title: Convention Based Tests
Date: 2017-01-11
Author: Shaun Finglas
Tags: tutorial, testing
Slug: 2017/01/convention-based-tests

Most projects have some form of convention. Examples would include:

-   Attributes/Properties for REST API's
-   Inheritance for third party base types
-   Assemblies/Packages for third party code that is loaded dynamically
-   Folder or namespace conventions
-   And many other forms of conventions

In a few of these examples static analysis can detect issues, but the
majority of these problems would resolve only at runtime.

A technique I've used in the past to great success is the concept of
convention based tests (CBT). These are tests that ensure a particular
convention is followed. As a general practice CBT tend to be written
after the discovery of a problem as it is preferable to rely upon higher
level tests initially. The good news is that CBT ensure that such
problems never return and if a convention is broken you'll be notified
during your test run.

In terms of quantity there will be a very small number of these tests,
and unlike typical tests that focus on behaviour rather than
implementation, these tests are focused on implementation.

### Reflection

Tests generally should [favour readability and clarity over the removal
of
duplication](http://blog.shaunfinglas.co.uk/2015/04/randomly-generated-values-in-tests.html).
Additionally the use of programming constructs such as loops or
conditionals within tests are usually a bad idea. Using reflection is
not recommended in most cases though the opposite is true for CBT.

Reflection allows the previous examples to have tests written in a
fairly flexible and dynamic manner. Future changes would automatically
be tested.

-   Tests to ensure particular types within a namespace have the correct
    attribute/property applied.
-   Tests to ensure particular types within a namespace have the correct
    base class.
-   Tests that assemblies/packages required at runtime are present
    within the bin directory.
-   Tests that folders/namespaces match a team/project naming standard.
-   And so on.

### Simpler Tests

In some cases reflection is not a suitable tool for convention based
tools. In this scenarios a simpler style of test is required. These are
essentially convention based tests that ensure additional tests are
written. These simple tests act more as a prompt to the developer
reminding them to add a test for a particular convention.

This test would first detect how many types exist within the namespace
and then detect how many tests have been written for those types. While
this style of test does nothing other than really count the number of
expected conventions versus the number of tests, the failure of this
test provides a hint to the developer that they have forgotten
something.

The key with these simple detection tests is to provide a good failure
message that includes details on why the test failed, and more
importantly why and how a new test should be added.

These simple CBT work when the use of reflection is difficult. While
they may seem primitive, they do provide value as simple reminders to
add future tests. Despite this it's worth remembering they provide no
guarantee of the quality of the additional tests that are written. Here
peer review is required.

### Lessons

-   Add convention based tests if a convention cannot be detected by
    static analysis or you cannot detect issues with higher level tests.
-   Reflection is a valid tool to write a single CBT that covers many
    areas.
-   If a CBT is hard to write, use a test to prompt you to add further
    tests in the future.