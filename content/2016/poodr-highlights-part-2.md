Title: POODR Highlights Part 2
Date: 2016-11-01
Author: Shaun Finglas
Tags: highlight
Slug: 2016/11/poodr-highlights-part-2

Two other stand out topics from POODR were the use of tests and
inheritance. The first set of [higlights covered dependencies and
arguments](http://blog.shaunfinglas.co.uk/2016/10/poodr-highlights-part-1.html).

#### Tests

A conclusion that I agree with is that in general “most programmers
write too many tests.”. A great quote in the book sees “tests (as) the
canary in the coal mine; when the design is bad, testing is hard”. Sadly
too many poor tests are often written. Examples such as property or
construction tests, framework tests or tests that are coupled to the
implementation are all common problems. Instead we should aim to get
better and more value out of our tests by writing fewer of them, but of
higher quality. In short test everything once and only in the proper
place. A first step is to simply focus on the ROI that tests give, and
focus on the high risk areas.

The test categories are broken down into two core types of tests.

-   Incoming Public Messages (public API)
-   Outgoing Public Messages (To public API of another object)

State based tests should be used for incoming public messages. While
verification based tests should be used for outgoing public messages as
the state is tested on the receiver, elsewhere. The [distinction between
commands and
queries](http://blog.shaunfinglas.co.uk/2015/04/cqrs-simplest-introduction.html)
is also highlighted. In summary incoming messages should be tested for
the state they return. Outgoing commands should be tested to ensure they
get sent. Outgoing query messages should not be tested, merely stubbed.

These testing rules are nothing new, but the summary and importance of
following these guidelines is nicely summarized within the chapter
covering testing principles.

#### Inheritance

Inheritance is widely abused and misunderstood. Either inheritance is
the solution for all problems, or you're advised to never use
inheritance. POODR takes a more pragmatic approach. Inheritance is a
tool that can sometimes provide an excellent solution, however you are
[better off duplicating
code](http://blog.shaunfinglas.co.uk/2015/06/dry-vs-coupling-in-production-code.html)
and [defer such
decisions](http://blog.shaunfinglas.co.uk/2015/11/dont-build-thing.html)
until you know more.

The wrong abstraction is harder to work with than duplicated code as
duplication can easily be removed. A bad abstraction that is used in
many places is much harder however. The application of the [Rule of
Three](http://wiki.c2.com/?RuleOfThree) can help here.

#### Lessons

-   Tests are hard - write less but focus on the quality.
-   Minimize the number of tests you write by using boundaries via
    incoming/outgoing messages.
-   Inheritance is not all bad.
-   Defer or hold back using inheritance until you understand the
    problem.