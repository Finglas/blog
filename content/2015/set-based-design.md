Title: Set Based Design
Date: 2015-10-01
Author: Shaun Finglas
Tags: architecture
Slug: 2015/10/set-based-design

Each morning newspapers hit the newstands without fail. Live broadcasts
are the same. Come show time they hit the air without fail. You can
probably think of more examples of deadlines that are constantly
achieved. So why does software development accept missed deadlines?
Software development not only encourages software to be late, it has
become accepted or just another risk to the project by default.

#### Solution

[Implementing Lean Software
Development](http://www.amazon.co.uk/Implementing-Lean-Software-Development-Addison-Wesley/dp/0321437381)
introduces the concept of Set Based Design (SBD). SBD provides an answer
on how to never miss a deadline every again, providing the deadline is
feasible. SBD will allow software to constantly hit deadlines just as
newspapers and TV shows do.

SBD requires multiple teams to implement the same functionality split
over several sets (versions) of work. Each team works independently and
in parallel to fulfil the same goal. This is in stark contrast to normal
proceedings where each team is usually assigned to separate projects. At
the end of the deadline the set that is best fit for purpose is chosen.
This ensures the teams as a collective have delivered the best possible
solution within the deadline. Each set should increase in scope and
complexity. This means each additional set has a higher chance of
missing the deadline.

#### Example

The number of sets you decide upon is based on each variation, so there
is no fixed limit. Assume three for the following introduction.

##### Set One

-   Start by accepting and acknowledging the deadline. This may be an
    integration deadline, a release or third party dependencies.
-   One of the teams should be working on the simplest thing that can
    possibly work. Some may say this is verging on a bodge or hack. You
    may end up adding logic to views, inserting business logic into
    sprocs or committing any other coding related atrocity. Despite this
    you must ensure the functionality is fit for purpose, tested and
    agreed by all.
-   The worst case scenario is the first set is released. You hit the
    deadline and you resolve some technical debt in the background
    afterwards.

##### Set Two

-   The team working on the second set would up their game. Still aiming
    for the deadline while the scope increases. Instead of adding logic
    into views, it goes into domain objects. Logic in sprocs? No chance.
    Other further enhacements could be added.
-   The worst case scenario? The deadline is missed but they have a
    solution which is better than the first set and close to completion.
-   After the first release the team simply finish up and deploy after
    the fact. This wipes out the technical debt of the first set and
    provides both a met deadline (via the first set) and the best
    possible solution.

##### Set Three

-   A third set would take a much higher level approach to the solution.
    This would be the best proposed solution. A strategic decision for
    the team factoring in long term goals and ambitions.
-   The chance of completing this set within the deadline are slim to
    none.
-   The worst case scenario is the team on the third set miss the
    deadline and one of the other two sets are released.
-   This is not the end of the world. Depending on how much work is left
    would dictate what happens. Scope could be further reduced, the set
    could be finished, or abandoned completely.

#### Questions

##### Is this waste?

No. The goal is to hit the deadline with the best possible solution.
While a number of sets will never be released, the teams have hit their
target. Teams should judge success on goal completion, not lines of code
into production.

##### What are the downsides?

Trying to explain SBD and actually convincing the business to have a
number of teams all working on the same project would sadly be an
incredible challenge in most organisations.

##### When would you not use SBD?

SBD makes sense when there is a fixed scope deadline that cannot be
missed. If this is not the case, iteration or refactoring at each step
would suffice.

##### Alternatives?

Producing an architecture that allows replacement or changes easily is
another alternative, though this has risks of its own. Changeable
architecture will be covered in a future post.