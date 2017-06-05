Title: Object Discovery
Date: 2012-12-01
Author: Shaun Finglas
Tags: programming
Slug: 2012/12/object-discovery

Recently we had [@kevinrutherford](https://twitter.com/kevinrutherford)
in to talk about object discovery. While TDD is a great tool, it is no
excuse for some sort of design process. If you don't, you'll most
[likely end up with a
mess](http://devgrind.com/2007/04/25/how-to-not-solve-a-sudoku/). This
session was based around this principle.

One point that was discussed what that the first few seconds of a test
for a new class is the most important part of the TDD process. It is
here where you will decide whether to take a state or interaction based
approach to testing. This first test will dictate the structure of the
new class. Once you start with tests, it becomes difficult to evolve or
change the design of a class without friction.

There is generally two types of code at Codeweavers.

<script src="https://gist.github.com/Finglas/4a9e9d35d64c150d6075.js"></script>
The trick comes from the fact that just because you use C\#/Java/etc..
most of the time you aren't actually writing OO code. You often end up
writing procedural code in a rather obtuse manner. A takeaway from this
afternoon was to try and perform more CRC
[(class-responsibility-collaborator)](http://en.wikipedia.org/wiki/Class-responsibility-collaboration_card)sessions.

### CRC (Object Cube)

During this session we performed a modified version of a CRC. One thing
I always find with CRC sessions is how useful they are. The problem I
and others find is when it comes to day to day development, I'm too
eager to start coding without performing some sort of up front design.

### Events

In order to write flexible OO code, you need to hide as much state as
possible. While this is great in practice it turns out to be very
difficult to achieve in the real world. One method of getting around
this is to make use of events aka the [observer
pattern](http://en.wikipedia.org/wiki/Observer_pattern).

Kevin used a wiki as an example. Consider a page that is updated. If
this page was to fire a changed event, then anything that is listening
for these events would be notified. The observers could then react once
the event was received. The nice thing about this approach is that the
code obeys the [open/closed
principle](http://en.wikipedia.org/wiki/Open/closed_principle). New
features can be added without the need for the change to have a large,
rippling effect.

### Nouns and Namespaces

When I was first exposed to object oriented programming, apart from
believing that inheritance was the coolest aspect of OO, I was also led
to believe that using nouns when designing classes can be useful. It
turned out that this was a fallacy. If you follow this advice you'll end
up with a small collection of classes that do everything. The biggest
revelation I had during the session came from the importance of
namespaces. Using nouns for up front design can be extremely useful if
you remember that the noun can potentially be a namespace. This means
you'll end up with a handful of namespaces that are relevant to the
domain in question. Inside these namespaces you will have one or more
classes that do [one thing, and one thing
well.](http://en.wikipedia.org/wiki/Single_responsibility_principle)

### Closing

At the end of the session I was left with many questions and new ideas
to test and try out. Using events to hide state, yet allow other objects
to interact when required was a real eye opener. However it turns out
that when actually trying to implement these ideas in code, it is
actually quite difficult due to my current thinking. The plan for the
next month will be to explore these ideas in more detail and see what
affect it has on my day to day development.