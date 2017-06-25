Title: Walking Skeleton
Date: 2015-05-01
Author: Shaun Finglas
Tags: development, team
Slug: 2015/05/walking-skeleton

[A Walking Skeleton is the thinnest possible slice of new functionality
that can be delivered end to
end](http://alistair.cockburn.us/Walking+skeleton). The term "*walking*"
refers to the ability for the feature to "*stand on its own*". You
should be able to deploy a Walking Skeleton and demonstrate it. Just
like a human skeleton is an incomplete body, a Walking Skeleton is an
incomplete piece of software with many internals stubbed, not
implemented or consisting of basic functionality.

While the software won't do much it provides rapid feedback. It allows
your build and deploy pipeline to be set up if not already in place.
More importantly it gives developers a framework or scaffold to work
with.

Production of a Walking Skeleton should be fast. Components such as
[which objects to introduce should ideally be developed top
down](https://blog.shaunfinglas.co.uk/2014/02/top-down-vs-bottom-up.html),
however the actual direction each solution takes will vary. Some design
will still be required, but the choice of patterns or implementation
details should be deferred where possible. Core interfaces such as
application services, domain models and data access will naturally fall
out of this process.

#### Tasking

Each new story or feature should be implemented as a Walking Skeleton
whenever possible. The first task a team should implement should be to
create the skeleton itself. An optional step during implementation is to
wrap the functionality in a acceptance test. Once the skeleton is
complete, a task per object can be created with clear inputs, outputs
and responsibilities.

#### Benefits

-   Highlights problems that tasking often misses.
-   Tasks can be implemented in parallel once a framework is in place.
-   Implementing or replacing stubbed code is easy given a stable API.
-   Provides working software very quickly and cheaply, which is great
    for feedback or exploration.
-   Puts the whole team on the same page.
-   Code trumps documentation.
-   Leads to a more stable API.
-   TDD is a natural fit once the skeleton is complete.

Producing a Walking Skeleton is not perfect, problems still crop up, but
they can be handled in a more controlled manner. Most issues relate to
implementation details at lower levels, rather than integration or
functional failures which are often symptoms of tasking before writing
any code.