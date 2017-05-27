Title: Throw Code Away
Date: 2015-11-24 08:11
Author: Shaun Finglas
Tags: http://schemas.google.com/blogger/2008/kind#post, architecture, agile-architecture-series
Slug: throw-code-away

The third and final part of my agile architecture series.

-   Part 1 - [You Cannot Iterate upon
    Architecture](http://blog.shaunfinglas.co.uk/2015/11/you-cannot-iterate-upon-architecture.html)
-   Part 2 - [Don't Build a
    Thing](http://blog.shaunfinglas.co.uk/2015/11/dont-build-thing.html)

------------------------------------------------------------------------

[Part
one](http://blog.shaunfinglas.co.uk/2015/11/you-cannot-iterate-upon-architecture.html)
suggested walking skeletons for new features or projects. [Part
two](http://blog.shaunfinglas.co.uk/2015/11/dont-build-thing.html)
suggested building the limited, smallest and simplest functionality
possible. However you do not always have the luxury of deferral.
Likewise if the project already exists and you are amending
functionality, a walking skeleton is going to be limited.

#### Solution

Throw code away. This sounds brutal and overkill, but throwing code away
has many advantages.

#### Benefits

-   The second time around you will solve the problem quicker having
    benefited from first time. The first attempt is a prototype in this
    case. Throwing away prototypes is expected. They are not production
    ready, usually built with short cuts or quality comprises
    intentionally.

-   The cleanest code is no code. Your following attempts will be
    cleaner. Knowing the issues from the previous attempt allows the
    ability to put code and procedures in place to prevent the same
    quality problems occurring.

-   Long term goals can be achieved rather than aiming for short term
    wins. Instead of focusing on meeting the current iterations' goal,
    answer whether or not your solution is fit for purpose going
    forwards. Does it scale? Is the quality there?

-   You benefit from hindsight. Most code to be replaced should have
    lived through some sort of review process. If the code has lived
    through production you have even more ammo to target the weak
    points. Where are the hotspots? What changes more frequently? Where
    do bugs tend to reside?

#### Objections

Throwing code away should not be taken lightly, but it is certainly a
valid technique under the right circumstances.

You will have an easier time suggesting to start over on two days worth
of work than you would two weeks, two months or two years. Keep your
batch sizes small and the ability to throw code away will become easier
to accept, with the benefits outweighing the negatives.

Small batches are not the only prerequisite to suggest throwing code
away. Small changes are also essential. You can easily suggest throwing
a method or class away, but you will rightly so have a harder time
suggesting throwing away a module or system.

Refactoring is often used as a suggestion to combat the need to rewrite
or throw code away but this is rarely the case in practice. Refactoring
is a misused word and crucially misunderstood technique. If you change
architecture you are not refactoring.

The biggest objector you will likely find is yourself. Having become
invested in a task it can be hard to try again. Fight the urge to resist
and throw code away. You may be pleasantly surprised by the results.

</p>

