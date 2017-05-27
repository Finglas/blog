Title: Ten Lessons from Rewriting Software
Date: 2016-07-10 14:27
Author: Shaun Finglas
Tags: http://schemas.google.com/blogger/2008/kind#post, retro, ten-lessons
Slug: ten-lessons-from-rewriting-software

1.  #### It Will Take A Lot Longer Than Estimated

    -   Its navie to actually think this but if a system has been in
        production for say five years, expecting to reproduce it in five
        weeks is not possible. You may be able to get 80% of the core
        functionality done, but the remaining 20% that was added to,
        iterated and stabilized over the remaining five years is what
        will destroy any form of schedule.
    -   If your estimate exceeds three months, you need to reasses what
        you are doing by breaking down the work, or changing plan. The
        bigger the estimate, the bigger the risk.

2.  #### Deploy Incrementally Via CI

    -   If you aren't deploying to a live environment as soon as
        possible, any future releases are destined to be failures,
        troublesome or just plain difficult.
    -   Soft releases and feature toggles should be used to aid constant
        releases.

3.  #### Morale Will Drop The Longer It Goes On

    -   Probably the biggest and most surprising realization is the drop
        in personal and team morale.
    -   If you miss a "deadline" or keep failing to ship, then morale
        will tank.
    -   While software is never complete, a rewrite has a definitive
        target. If this target continues to move, team morale will move
        too.

4.  #### Users Will Probably Hate It Anyway

    -   Predominantly the UI, but your users will complain about change.
    -   Big sweeping changes often receive the most hate. A website I
        frequent had a major change both in visuals and the underlying
        technology used. While there was warning, you were left to your
        own to figure out where features were. This caused a great deal
        of frustration and negative feedback.
    -   Small, incremental changes allow your users to keep pace.
    -   Alternatively some tutorial or hint system can help reduce user
        pain.

5.  #### Do What The Legacy System Does

    -   As many of the original developers will likely have moved on, no
        one is really sure what the legacy system does.
    -   Even with the source code available, it is likely going to be
        hard to figure out the intent, afterall that's one of the
        reasons for the rewrite.
    -   If you are not careful you will end up simply reimplementing the
        same legacy in a new language or framework. Always weigh up
        preserving existing behaviour versus introducing technical debt.

6.  #### Be Cheap And Quick - Use Stubs

    -   When implementing the new system, [don't build a
        thing](http://blog.shaunfinglas.co.uk/2015/11/dont-build-thing.html).
        At least at first.
    -   Use stubs to build the simplest, dumbest thing you can to get
        feedback.
    -   Without fully integrating the system in an end to end manner
        you'll end up throwing away a great deal of code.

7.  #### Feedback, Feedback, Feedback

    -   Early and fast feedback is essential.
    -   With a working end to end system gather as much as you can from
        any stakeholders.
    -   Chances are as you begin you'll naturally incur some additions,
        removals or modifications.
    -   Waiting months or longer for feedback is a guaranteed path to
        failure.

8.  #### Thin Vertical Slices Over Fat Technology Splits

    -   Avoid the temptation to have a UI team, a backend team and a
        data team and so on.
    -   Splitting at technology boundaries leads to systems that do not
        integrate well, or worse fail to handle the required use cases.
    -   Your first iteration should consist of all parts of the
        technology stack, in the thinnest manner possible. Combine this
        with early feedback and the fast development speed of stubs.

9.  #### Strangle Existing Legacy Code

    -   When rewriting in increments or by logical sections the
        [technique of
        strangulation](http://martinfowler.com/bliki/StranglerApplication.html)
        is useful.
    -   Instead of releasing the new code as a standalone piece,
        integrate the new code into the existing legacy code base.
    -   This may be tricky at first however over time the legacy system
        will form nothing but an empty shell that integrates with the
        new system.
    -   The beauty of this approach is early feedback, and a guarantee
        that the new system behaves as intended.
    -   The final step would be to replace the legacy shell with the new
        modern interface or frontend.

10. #### Refactor Where Possible

    -   Deciding to refactor or rewrite is never easy. Refactoring
        should be the default approach in many cases.
    -   Old languages or unsupported frameworks are good reasons to
        adopt a rewrite, but this varies case by case.
    -   If business agility is suffering such rewrites can be beneficial
        when using some of the techniques above.

</p>

