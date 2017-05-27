Title: Past Mistakes - ORMs and Bounded Contexts
Date: 2016-08-31 07:12
Author: Shaun Finglas
Tags: http://schemas.google.com/blogger/2008/kind#post, retro, past-mistakes-series
Slug: past-mistakes-orms-and-bounded-contexts

Sticking with the theme of documenting past mistakes, it's worth
expanding a real life scenario where I was unaware of the use of bounded
contexts and fully understanding the tools you use.

#### Ignoring a Bounded Context

A fellow developer set upon a quest to rid numerous projects of
duplicated records, which was effectively the active record pattern.
This was a huge under taking split across hundreds of thousands of lines
of code, over numerous separate projects. Close to completing the task I
assisted and finally the shared library containing a single record for
each type was complete. Each project now referenced the shared copy.
This was versioned as each build was completed.

For a while this worked with no problems. It certainly felt nice to see
the reduction in duplicated code. Sadly sometime later myself and
another developer made a seemingly innocent change. In terms of
relation, the change was as far removed from the production error that
we had just been alerted to was. There was no link. It was a different
project, in a different path, on a different model. The only commonality
was the fact the issue only occurred after the previous deploy.

#### ORMs and Changes

Several minutes of panic later, the problem was spotted. While the model
we had changed had no direct relation, indirectly there was. As each
record was loaded by the ORM in question, links and dependencies where
also loaded or checked. So were the children's links and dependencies.
Finally this would hit the newly changed record. Due to the database
changing ahead of the library, numerous other projects now had a runtime
error. As we naively believed we were only working within a single
project, we deployed the changes within the one project. As the library
was shared, all other projects were now vulnerable.

This lack of [bounded
context](http://blog.shaunfinglas.co.uk/2016/06/ddd-bounded-contexts.html),
and focusing on [removal of
duplication](http://blog.shaunfinglas.co.uk/2015/06/dry-vs-coupling-in-production-code.html)
was not the only lesson here. This issue painfully highlighted the need
and importance to know exactly what your tools are doing, especially
when they are hidden behind the scenes. In fact, my use of ORMs other
than micro-ORMs is next to non existent at present.

#### Lessons

-   Use bounded contexts.
-   Favour loose coupling, over reduced duplication.
-   Anything shared must be deployed and tested as a single unit,
    otherwise remove the shared component.
-   ORMs (or other tools) should be understand and respected.

</p>

