Title: The Self Shunt - Test Doubles without a Framework
Date: 2015-09-01
Author: Shaun Finglas
Tags: testing, unit-testing, tutorial
Slug: 2015/09/the-self-shunt-test-doubles-without

Generally you should [favour hand crafted stubs without a framework by
default](http://blog.shaunfinglas.co.uk/2015/08/why-i-dont-like-mocking-frameworks.html).
Before you reach for a framework there is another bridging step that you
can take only pulling in a framework if complexity arises - the Self
Shunt.

Assume a simple *Hello World* subject under test where we can provide
different formatters that format the message to a console, XML or JSON
for example. How do we test that the formatter is used, with the right
arguments?

Enter the [Self Shunt
(pdf)](http://www.objectmentor.com/resources/articles/SelfShunPtrn.pdf).
Have the test fixture implement the interface aka assume the role of a
message formatter. It provides itself as a parameter to the greeter in
the form of `self/this`. The greeter uses this implementation during its
execution, the test fixture can then assert or set state.

<script src="https://gist.github.com/Finglas/698caab47b1428d0e303.js"></script>
#### Benefits

-   Quick and simple to get up and running.
-   Most commands fall into the category of invoke something with some
    parameters, with little more complexity.
-   Forces you to respect the Interface Segregation Principle, otherwise
    this technique can become painful. A framework usually masks this
    complexity.
-   Code is inline to the test or fixtures.
-   Exposes and explains how frameworks work conceptually to new
    developers - removing some of the *magic*.

The Self Shunt is my default approach for testing commands which are
usually local to test fixtures. Queries default to hand crafted stubs
which are usually shared amongst tests. If further tests need the same
configuration the shunt can be promoted to a full object that lives
independently of the test fixture. Finally if this starts to become
difficult to work with I would reach for a framework - commands usually
reach this point first.