Title: Learning Tests
Date: 2014-05-01
Author: Shaun Finglas
Tags: testing, tdd
Slug: 2014/05/learning-tests

At the last [Agile Staffordshire](http://www.agilestaffordshire.org/) I
attended [the task was to complete the string calculator with
constraints](http://www.agilestaffordshire.org/agile/january-2014-kata-with-constraints/).
The group worked in pairs and everything was running smoothly. Until I
heard a few guys behind struggling with something.

I'd worked with one of the developers previously, so they called me over
to take a look. What he found was pretty shocking - they had found a bug
in the .NET framework. The string class of all things. Bugs exist in all
code. Bugs in the substring method though are probably rarer given how
exhaustively used this particular bit of code is.

The problem was how they expected the method to behave. When creating a
substring they were getting confused with how the offests worked.

This is an easy mistake. Different languages or frameworks can have
different methods to do similar tasks. I take no shame in not knowing of
the top of my head whether the offest of the substring method is an
offset of the index, or an offset from the start of the string.

I managed to spot the issue very quickly but never let on. Instead I
decided to share a technique which I use regularly to great effect.

Rather than painfully using the debugger and stepping through the code
line by line I suggested he write a simple test around the single line
of code they were convinced was misbehaving.

After a couple of more tests it was clear how the substring method
worked in .NET. Once this was cleared up, we deleted the tests we just
wrote and modified the production code to use the correct offset. This
whole process took less than sixty seconds.

I explained afterwards that such a technique of writing [learning
tests](http://blog.thecodewhisperer.com/2011/12/14/when-to-write-learning-tests/)
or scaffholding tests is incredibly valuable. The feedback cycle here is
very quick. Quicker than explaining to another developer what is wrong;
Quicker than "Googling" the problem; Quicker than looking at the
reference implementation and certainly quicker than using the debugger.

My rules are pretty explicit when dealing with learning tests. They
should be short lived. Testing implementation details is often a bad
idea, but that is the whole point of such style of testing. Therefore if
you do decided to check these tests in tagging them so they are only run
as part of CI builds is worthwhile. In other words, just like real world
scaffholding, they are temporary. [Don't feel bad about writing some
tests, only to delete them minutes
later](http://blog.shaunfinglas.co.uk/2012/01/write-unit-tests-start-deleting-them.html).

Learning tests have another nice side effect. They give static languages
which have a slower feedback cycle a form of
[REPL](http://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop).
It's a lot quicker to write a test method and execute than it would be
to spin up a new project in languages such as C\# or Java to just try
something out.

Next time you're stuck, try writing a test.