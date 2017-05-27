Title: Release It - Highlights Part 2
Date: 2015-09-08 06:33
Author: Shaun Finglas
Tags: release-it, http://schemas.google.com/blogger/2008/kind#post, books, release-it-series
Slug: release-it-highlights-part-2

This is the second part of my collection of notes and snippets from
[Release It!](https://pragprog.com/book/mnee/release-it)

-   [Part 1 - Shared Resources, Responses, SLA, Databases and Circuit
    Breakers](http://blog.shaunfinglas.co.uk/2015/09/release-it-highlights-part-1.html)
-   Part 2 - Caches, Testing, HTML, Pre-Computation and Logging (Future
    Post)

------------------------------------------------------------------------

#### Caches

-   Low memory conditions are a threat to both stability and capacity.
-   You need to ask whether the possible keys are infinite or finite and
    would the items ever need to change?
-   The simplest cache clearing mechanism is time based.
-   [Improper use of
    caching](http://blog.shaunfinglas.co.uk/2015/01/caching.html) is the
    major cause of memory leaks, which turn into horrors like daily
    server restarts.
-   Your system should run for at least the typical deployment cycle. If
    you deploy once every two weeks, it should be able to run for at
    least two weeks without restart.
-   Limit the amount of memory a cache can use.
-   Caches that do not limit memory will eventually eat all memory.

#### Testing

-   Every integration point should have a test harness that can be
    substituted.
-   Make your test harness act like a hacker - try large payloads,
    invalid characters, injection and so on.
-   Have your test harness log requests so you can see what has caused
    problems.
-   Run longevity tests - tests that put impulse and stress upon a
    system over long periods of time.
-   Someone saying "*the odds of that happening is millions to one*" is
    actually quite likely to happen. Given a average site, making
    thousands of requests a day this is an easy target to hit.
-   Sessions are the Achilles heel of every application server.
-   Most testing uses the app in the way it was expected to be use such
    as load testing a site using the correct workflow. What about load
    testing without using cookies? Would this spawn a new session each
    time?

#### HTML

-   Whitespace costs! In HTML (or the markup generated) remove all
    whitespace. It costs time to generate and money to send across the
    wire. You could argue this is for big traffic sites only, but this
    technique is very simple to apply as part of the build and speeds up
    client side rendering.
-   Omit needless characters in HTML such as comments. Use server side
    commenting instead, this will be removed when processed.

#### Pre-Computation

-   Precompute as much of the page as possible. Use "punch outs" for
    dynamic content. For example Slashdot generates its page once and
    serves to thousands of users. All users get the page equally as
    fast. Caching would mean handfuls of users would get a slow
    experience.
-   Precomputed content should be deployed as part of the build. For
    more frequent updates another strategy or "content deploys" would be
    required.

#### Logging

-   The human visual system is an excellent pattern matching machine.
    Make logs readable by using a custom format. Scanning logs is very
    easy then.
-   Two line log files are difficult. Harder to grep. Keep everything on
    one line.
-   Each week review the systems tickets. Try to identify and fix
    problems as you go. Try and predict future problems where possible
    based on this info.
-   Check the logs daily for stack traces that are suspicious. These
    could be common errors that are bugs/problems that need fixing.

</p>

