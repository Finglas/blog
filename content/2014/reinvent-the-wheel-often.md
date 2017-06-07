Title: Reinvent the Wheel, Often
Date: 2014-10-01
Author: Shaun Finglas
Tags: retro
Slug: 2014/10/reinvent-wheel-often

We are often never told to reinvent the wheel. In other words, if your
job is solve problems within Domain X you shouldn't spend your time
recreating or solving problems that fall outside of this domain.

For production code, this I agree with this statement fully. Software
development is hard enough. The last thing we want is to waste resources
such as time or money on anything we can get away with not implementing.
For example, creating your own web framework is a project within itself.
All you'll end up with is a slow, buggy, badly implemented version of a
web framework that happens to power your domain. Sadly I have been on
the receiving end of such decisions.

There are two times however, when reinventing the wheel is a good thing.

-   You can't get the product off the shelf
-   Learning or personal benefit

Chances there is no web framework, database client, caching layer or so
forth that you can use is very slim. Some systems become so bespoke or
scale to such volumes that recreating such components makes sense. These
are the Netflix/Facebook/Google of the world. Most enterprise software
will never reach a slither of this sort of scale.

The biggest benefit of recreating well known, solved solutions is the
vast amount of learning and knowledge you will obtain. In the past I
have re-invented numerous wheels, but each time taken away something of
value.

Systems that seem simple at first such as static website generator, turn
out to be incredibly complex once you understand the full set of
scenarios and edge cases you must handle. The key point here is these
wheels, never make it into production for the reasons detailed
previously.

In turn you will come to appreciate library and framework developers if
you can fight the urge to resist [Not Invented Here
Syndrome](http://en.wikipedia.org/wiki/Not_invented_here). Their full
time project is the delivery of that solution. They have the time to
solve all the edge cases you don't. Not to mention the vast amount of
other users that will have debugged and improved the solution going
forwards. By not reinventing wheels you get as much time as possible to
focus on delivering your solution to the domain problem in question,
which after all is your job.