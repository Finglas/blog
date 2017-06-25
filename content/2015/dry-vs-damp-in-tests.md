Title: DRY vs DAMP in Tests
Date: 2015-04-01
Author: Shaun Finglas
Tags: programming, unit-testing, tutorial
Slug: 2015/04/dry-vs-damp-in-tests

In the [previous post I mentioned that duplication in tests is not
always
bad](https://blog.shaunfinglas.co.uk/2015/04/randomly-generated-values-in-tests.html).
Sometimes duplication becomes a problem. Tests can become large or
virtually identically excluding a few lines. Changes to these tests can
take a while and increase the maintenance overhead. At this point, DRY
violations need to be resolved.

#### Solutions

##### Test Helpers

A common solution is to extract common functionality into setup methods
or other helper utilities. While this will remove and reduce duplication
this can make tests a bit harder to read as the test is now split
amongst unrelated components. There is a limit to how useful such
extractions can help as each test may need to do something slightly
differently.

##### DAMP - Descriptive and Meaningful Phrases

[Descriptive and Meaningful
Phrases](http://www.pluralsight.com/courses/advanced-unit-testing) is
the alter ego of DRY. DAMP tests often use the builder pattern to
construct the System Under Test. This allows calls to be chained in a
fluent API style, similar to the [Page Object
Pattern](https://blog.shaunfinglas.co.uk/2014/05/flexible-selenium-tests-via-page-objects.html).
Internally the implementation will still use literals or value objects,
but each test can provide just the differences it needs in order to
execute. The key point regardless of how DAMP tests are implemented is
to favor readability over anything else, while still eliminating
duplication where possible.

<script src="https://gist.github.com/Finglas/d9308078e672ce5fd64f.js"></script>
The example shows a typical arrange aspect of a test written in the DAMP
style. The end result of this builder is we will have the ability to now
act and assert against the result - a controller instance. If further
tests were required we could use the same setup but simply provide
different order dates for example. Additionally we could add or remove
further chained calls. Behind the scenes the [implementation of these
builders is
straightforward](https://github.com/Finglas/Playground/blob/master/SutBuilder/SutBuilderExample.cs).

I tend to introduce this pattern after the third time of seeing
duplication between tests. There is a bit of an overhead otherwise, the
builder itself requires implementation and careful construction. Once
you go past three tests the overhead pays itself off by allowing you to
rapidly add new tests and make large, structural changes.

Beware the builders becoming too big or complex. If this starts to
happen you may wish to refactor as there may be missing abstractions in
your design. DAMP tests have numerous advantages, but they should be
applied where required rather than for every scenario. Tests for objects
that are lower in the dependency graph tend to fit into the more
traditional testing patterns, while higher up your stack DAMP tests can
prove useful.