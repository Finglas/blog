Title: Design is Important
Date: 2014-07-22 19:20
Author: Shaun Finglas
Tags: http://schemas.google.com/blogger/2008/kind#post, programming, design
Slug: design-is-important

When I was a student I used to cheat. Not in exams or practical
assignments, but I used to cheat when it came to my process to develop
code. Early on I noticed a common pattern. After receiving an assignment
I would perform some analysis, figure out a basic design and document my
steps. The problem came when to code up the solution. I may have
overlooked something, or made a mistake. Sometimes I would just come up
with a better solution. This meant any time I spent documenting was
lost. It turns out this wasn't cheating, after all there was nothing
within the assignments enforcing a waterfall approach.

I wasn't alone with this experience. Most of my peers had the same
issue, and the report aspects of an assignment were often disliked for
this very reason. My solution was simple. Code up something, get it
working then document the design aspect. Rinse and repeat. Back in the
early 2004 I wasn't aware of agile methodologies, but this solution
worked a treat. In turn my classmates started to adopt this similar
approach, either from my encouragement or their own discovery.

Moving from university into a practical environment was a joy. It almost
appeared as if little to no documentation was produced. The
documentation that was produced, was often created by other teams.
Developers simply wrote code. At the time I thought this was great, but
after some reflection the errors of my ways have been highlighted.

Problems
--------

In my experience a variety anti patterns are to blame.

-   ### No or limited design

    The **worst** thing that can be done when it comes to design or
    planning is the absence of any design or plan whatsoever.

-   ### Coding your way out of problems

    Given some limited or poor design, I've often experienced scenarios
    where 80% of the tasks will be complete, then you hit a roadblock.
    In order to progress the team will hack their way around it,
    introduce [technical
    debt](http://en.wikipedia.org/wiki/Technical_debt) or put in some
    **not so temporary fixes**.

-   ### "Weeks of coding can save hours of planning"

    A colleague I used to work with used this once and I fell in love
    with the quote. Take an average web application, if the life cycle
    of this would be a meager two years, **spending a few hours putting
    a design together is nothing**. You could argue that spending a few
    days would be equally fitting, better yet **a couple of weeks well
    thought out design is only a small percentage of the overall cost of
    delivery**. When it's too late you can code your way around the
    problem. Though this debt will soon add up, meaning features are
    even slower to add going forwards.

-   ### Playing the "Agile" card

    A misconception of the [agile manifesto](http://agilemanifesto.org/)
    is to favour "*working software over comprehensive documentation*".
    **Most developers read this as never document anything**. This is
    far from the truth. Documentation, design and planning should be
    built into the product in iteration. [Just In
    Time](http://en.wikipedia.org/wiki/Just_in_time_%28business%29)
    (JIT), rather than all up front or never at all.

-   ### Greenfield projects

    Having been involved with a couple of "rewrites" I've seen this
    happen first hand. **No design, limited design or bad planning in
    the first few iterations of a project can kill it**. [Only by
    iteration three, four or five will you notice something isn't
    right](http://beust.com/weblog/2008/03/03/tdd-leads-to-an-architectural-meltdown-around-iteration-three/).
    At this point you've lost. Suggesting to restart, reboot or refactor
    is a hard sell, especially to management teams. **Architectural
    changes are very difficult at this point**, as you'll most likely
    have users, automated tests and other teams relying on what you have
    produced.

-   ### Refactoring can save the day!

    Give me a bad class or method and I can make it beautiful. Give me a
    bad application and we have a problem. **Refactoring is a class or
    method based activity**. [I don't buy architectural refactoring -
    and I'm not
    alone](http://www.amazon.co.uk/gp/product/0470684208/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&camp=1634&creative=6738&creativeASIN=0470684208&linkCode=as2&tag=bloshafin-21).
    Emergent design is a very powerful tool, but without some upfront
    planning you'll be stuck in limbo.

Solutions
---------

There are a few ways to overcome the previous problems.

-   ### Whiteboards

    As much as I love technology you **cannot beat a whiteboard** (or
    piece of paper) and a couple of engineers. Visual collaboration in
    this manner is very easy, plus physically having the presence of
    another individual helps. You can also snap a picture of these
    diagrams to reproduce them in a more friendly, shareable, digital
    form afterwards.

-   ### CRC's

    [Class Responsibility and Collaboration
    cards](http://en.wikipedia.org/wiki/Class-responsibility-collaboration_card)
    are another low tech solution, but one I find incredibly valuable,
    yet for some reason don't appear to do enough of. **Best performed
    in groups**, though I've had some success on solo efforts.

-   ### JIT documentation

    Not pages of wiki articles or documents, just lean, self contained
    documents that serve a purpose. Develop these in iteration and
    you'll avoid a "documentation sprint" from hell.

-   ### Code itself

    **Prototypes are worth their weight in gold**. Spike solutions when
    used across a team are also incredibly effective. Rather than a
    single prototype being produced, each team has a crack at the
    problem in isolation. After regrouping you present back your
    solution and findings. The team then combine to form a "best of
    breed" approach.

    Iteration zero is often used for getting the build up and running.
    If you take this one step further, the ideal scenario is to produce
    a [walking skeleton](http://alistair.cockburn.us/Walking+skeleton).
    This should consist of empty or basic class/method/function
    definitons that have not yet been implemented. **With a basic API in
    place, fleshing out the details is rather enjoyable**. You focus on
    the problem, not the design or architecture.

None of these are ground breaking ideas, but combined these approaches
have served me well both personally and professionally.

</p>

