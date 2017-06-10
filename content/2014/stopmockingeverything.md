Title: Stop.Mocking.EVERYTHING
Date: 2014-08-01
Author: Shaun Finglas
Tags: programming, retro, tdd
Slug: 2014/08/stopmockingeverything

I've flip flopped on how to use mock objects since 2008. It's took me
nearly five years to finally claim to have a solid, practical answer on
what is in my opinion, their correct use.

#### Mock Everything

Some developers told me to mock everything. Every. Single. Collaborator.
I wasn't sure about this approach.

-   My tests felt too brittle - tied to implementation details.
-   My tests felt like a duplication of my production code.
-   Your test count rises rapidly.
-   This style of testing will slow you down - more to
    write/execute/debug.

#### Mock Nothing

Some developers told me to mock nothing. Sometimes I never used mocks. I
wasn't sure about this approach either.

-   My tests felt too loose - it was easy to introduce bugs or defects.
-   My production code suffered as I introduced accessors only for
    testing.

No wonder I was confused. Neither approach seemed to be comfortable with
me.

#### Solution

-   Use mocks for commands
-   Use stubs for queries

This halfway house is built around the idea of [command and query
separation](http://martinfowler.com/bliki/CommandQuerySeparation.html)
as detailed by [Mark
Seeman](http://blog.ploeh.dk/2013/10/23/mocks-for-commands-stubs-for-queries/).
This simple principle makes a lot of sense, and finally helped me
realise how best to use stubs and mocks.

-   Any commands (methods that have no return type) should have a mock
    object verifying their use if they are architecturally significant.
-   Any queries (methods that have return types) should have a stub
    object that is returned if their use is architecturally significant.

If the collaborator is not significant, or in other words is simply an
implementation detail then no mock or stub is needed. That's right, just
new up (or instantiate) your dependency there and then. This allows you
to refactor the internals aggressively, without the fear of breaking or
rewriting tests.

This approach has served me well for a while now, and in fact can be
achieved even without the need to use a complicated mocking framework,
though that will be the subject of a future post.