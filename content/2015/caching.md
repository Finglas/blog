Title: Caching
Date: 2015-01-01
Author: Shaun Finglas
Tags: programming
Slug: 2015/01/caching

The naive approach to implement caching is to just store everything in
an in memory collection such as a hashtable. After all it works on my
machine.

I've worked on systems in the past that used this technique but:

-   Bring in two processes and this falls apart
-   No Time to Live (TTL)
-   No cache eviction, memory will grow until it crashes the process

This sort of caching meant the system needed daily restarts due to each
worker process starting to eat up more and more RAM. At the time I
didn't realise this was the problem as to why daily restarts were
required. These were automated so the team just sort of forgot about the
problem after a while. This never felt right.

> "Improper use of caching is the major cause of memory leaks, which
> turn into **horrors like daily server restarts**" - [@mtnygard in
> Release It!](https://twitter.com/mtnygard).

Scale this system up, and daily becomes twice daily and so on. In a
global market where software shouldn't be constrained by time zones or
"working hours" this is wrong.

#### Solutions

There are numerous easy ways to solve these problems depending on the
application in question.

##### Don't Roll your Own, Try a Third Party

Easy. Just use an off the shelf solution that solves the problems above
plus includes a whole host of additional features.

##### Use your Standard Library

For example .NET includes caching functionality within the
[System.Runtime.Caching](http://msdn.microsoft.com/en-us/library/system.runtime.caching%28v=vs.110%29.aspx)
namespace. While there are limitations to this, it will work for some
scenarios and solves some of the problems above.

##### Soft References

I've overlooked [soft
references](http://docs.oracle.com/javase/7/docs/api/java/lang/ref/SoftReference.html)
in the past but for caching they can be incredibly useful. Use soft
references for anything that isn't important or that can be
recalculated. An example would be content displayed within an MVC view
using the web servers session. Here if each item stored is a weak
reference we introduce some benefits.

-   Stops your web server running of of memory - references will be
    reclaimed if memory starts to become a bottleneck.
-   Greater scalability with the same amount of memory - great for a
    sudden spike in traffic.

A web server's session being full of references that won't expire for a
set period is a common cause of downtime. If soft references are used
all we need to do is perform a simple conditional check prior to
retrieval from the session. Different languages have similar features,
e.g. [Weak
References](http://msdn.microsoft.com/en-us/library/system.weakreference%28v=vs.110%29.aspx)
in .NET.

##### Pre-Computation

Caching isn't always the best solution, in some cases pre-computation
can be much easier and offer better performance. In other words at least
some users will experience a slow response until the cache is warm,
other techniques can be used to avoid this completely. I will expand on
pre-computation in a future post.

#### Reference

More information can be found in the excellent book [Release
It!](https://pragprog.com/book/mnee/release-it)