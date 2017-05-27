Title: Characterization Tests
Date: 2014-10-13 17:41
Author: Shaun Finglas
Tags: testing, http://schemas.google.com/blogger/2008/kind#post, programming
Slug: characterization-tests

Having worked with some truly awful codebases a common problem tends to
arise every now and then. You need to make a change within some legacy
component that most likely has limited or no automated tests around.
This can be a scary process.

There are a few techniques you can use to limit the fear of breaking
some legacy code such as [sprout methods or
classes](http://xunitpatterns.com/Sprout%20Class.html), however these
aren't always optimal in all scenarios.

Another option is [characterization
tests](http://en.wikipedia.org/wiki/Characterization_test) or "what is
this bit of code actually doing?".

1.  Start with a simple test such as "ItWorks".
2.  Run the test - watch it fail.
3.  Using the stacktrace or error reported, write some additional setup.
4.  Run the test - watch it get past the previous error.
5.  Rinse and repeat step 3 - 4 until green.

As part of the first step you should keep the initial test as simple as
possible. For example if an input to the system under test (SUT) takes a
Foo object, just instantiate Foo. Don't start setting values or fields
on Foo. Let the failing test indicate what needs to be set such as a
BarException informing you that "bar must be greater than zero" as part
of step three.

By now you should have exercised a good chunk of the system under test.
However you may need to add additional tests. For example if the code
contained an "if" statement, you would need at least two
characterization tests. A good way to detect how many tests you need is
a code coverage tool, or manually inserting assertions into the SUT to
show any missing coverage. Likewise a good manual review is required to
fully detect any other tests you may have missed such as boundary cases.

Now the fun can begin. You can refactor like crazy.

Afterwards you should have a nicely refactored component that you can
easily extend or modify to add your new feature. You also have a solid
suite of tests to prove you've not broken anything. These tests will
also document the current behaviour of the system - bugs included.

Examples
--------

-   [Therapeutic
    Refactoring](https://www.youtube.com/watch?v=J4dlF0kcThQ) - an
    excellent video showing this process in action.
-   [Working Effectively with Legacy
    Code](http://www.amazon.co.uk/Working-Effectively-Legacy-Robert-Martin/dp/0131177052) -
    a must read book for anyone working with legacy code.

</p>

