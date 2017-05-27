Title: Ratcheting
Date: 2014-11-18 18:41
Author: Shaun Finglas
Tags: testing, http://schemas.google.com/blogger/2008/kind#post, programming, CI, build
Slug: ratcheting

Some tasks in software development are mundane such as formatting and
code conventions. Where possible tooling should take away some of this
pain, however sometimes you need a developer to take on a task that
requires a great deal of time and/or effort to complete. Tooling will
only get you so far.

An example of this would be declaring that all projects build and
compile with zero warnings. I've tried this in the past after a team
retrospective. We had hundreds of errors per project, covering about
fifteen projects at the time. Spending several weeks of development time
resolving these would not have be fun nor financially viable. However we
really wanted to implement this change

Solution
--------

-   I wrote a single test which would execute as part of the build
    process that asserted the count of the errors per project.
-   Every now and then whenever I had some slack time (10 mins before a
    meeting, 30 mins at the end of the day etc...) I would open up a
    project and fix some errors. Then run the test and try and lower the
    number of errors it was asserting against until I hit the lower
    limit.
-   Rinse repeat this process and after a while a project would assert
    that there are no errors.
-   From here on it was impossible for a developer to commit in a change
    that would raise a warning.
-   The limit would ensure that during this period no new errors were
    added, increasing the work load.

After a month or so all the projects reported zero warnings. Going
forward the test was modified so that new projects added to source
control would be checked and have the same tests run against them,
meaning no new projects can have a warning count greater than zero.

It turns out this has been documented before - its called
[Ratcheting](http://martinfowler.com/articles/useOfMetrics.html#MetricsAsARatchet).
While I didn't know it at the time its nice to have a name to use when
[describing this technique](http://bugroll.com/ratcheting.html).

</p>

