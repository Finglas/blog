Title: Release It - Highlights Part 1
Date: 2015-09-08 06:34
Author: Shaun Finglas
Tags: release-it, http://schemas.google.com/blogger/2008/kind#post, books, release-it-series
Slug: release-it-highlights-part-1

[Release It!](https://pragprog.com/book/mnee/release-it) is one of the
most useful books I've read. The advice and suggestions inside certainly
change your perspective on how to write software. My key takeaway is
that software should be cynical. Expect the worst, expect failures and
put up boundaries. In the majority of cases these failures will be
trigged by integration points with other systems, be it third parties or
your own.

My rough notes and snippets will be spread across the following two
posts. There is much more to the book than this, including various
examples of real life systems failing and how they should have handled
the problem in the first place.

-   Part 1 - Shared Resources, Responses, SLA, Databases and Circuit
    Breakers
-   [Part 2 - Caches, Testing, HTML, Pre-Computation and
    Logging](http://blog.shaunfinglas.co.uk/2015/09/release-it-highlights-part-2.html)

------------------------------------------------------------------------

#### Shared Resources

-   Shared Resources can jeopardize scalability.
-   When a shared resource gets overloaded, it will become a bottleneck.
-   If you provide the front end system, test what happens if the back
    end is slow/down. If you provide the back end, test what happens if
    the front end is under heavy load.

#### Responses

-   Generating a slow response is worse than refusing to connect or
    timing out.
-   Slow responses trigger cascading failures.
-   Slow responses on the front end trigger more requests. Such as the
    user hitting refresh a few times, therefore generating more load
    ironically.
-   You should error when a response exceeds the systems allowed time,
    rather than waiting.
-   Most default timeouts of libraries and frameworks are far too
    generous - always configure manually.
-   One of the worst places that scaling effects will bite you is with
    point to point communication. Favour [other alternatives such as
    messaging](http://blog.shaunfinglas.co.uk/2015/08/queue-centric-work-pattern.html)
    to remove this problem.

#### SLA

-   When calling third parties, services levels only decrease.
-   Make sure even without a third party response your system can
    degrade gracefully.
-   Be careful when crafting SLA's. Do not simply state 99.999%, it
    costs too much to hit this target and most systems don't need this
    sort of uptime.
-   Reorient the discussion around SLA's to focus on features, not
    systems.
-   You cannot offer a better SLA than the worst of any external
    dependencies you use.

#### Databases

-   Your application probably trusts the database far too much.
-   Design with scepticism and you will achieve resilience.
-   What happens if the DB returns 5 million rows instead of 5 hundred?
    You could run out of memory trying to load all this. The only
    answers a query can return is 0, 1 or many. Don't rely on the
    database to follow this limit. Other systems or batch processes may
    not respect this rule and insert too much data.
-   After a system is in production, fetch results can return huge
    result sets. Unlike developer testing where only a small subset of
    data is around.
-   Limit your DB queries, e.g. SELECT \* FROM table LIMIT 15 (the
    wildcard criteria would be substituted)
-   Put limits into other application protocols such REST endpoints via
    paging or offsets.

#### Circuit Breakers

-   Now and forever [networks will always be
    unreliable](https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing).
-   The timeout pattern prevents calls to integration points from
    becoming blocked threads.
-   [Circuit
    Breakers](http://martinfowler.com/bliki/CircuitBreaker.html) area
    way of automatically degrading functionality when a system is under
    stress.
-   Changes in a circuit breaker should always be logged and monitored.
-   The frequency of state changes in a circuit breaker can help
    diagnose other problems with the system.
-   When there is a problem with an integration point, stop calling it
    during a cool off period. The circuit breaker will enable this.
-   Popping a circuit breaker always indicates a serious problem - log
    it.

</p>

