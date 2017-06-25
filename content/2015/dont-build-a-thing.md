Title: Don't Build a Thing
Date: 2015-11-01
Author: Shaun Finglas
Tags: architecture, agile-architecture-series
Slug: 2015/11/dont-build-thing

Part two of my agile architecture series.

-   Part 1 - [You Cannot Iterate upon
    Architecture](https://blog.shaunfinglas.co.uk/2015/11/you-cannot-iterate-upon-architecture.html)
-   Part 3 - [Throw Code
    Away](https://blog.shaunfinglas.co.uk/2015/11/throw-code-away.html)

------------------------------------------------------------------------

Here is a real life example of where I treated a unknown project
incorrectly. Why I handled this is badly and how I should have handled
it if I could rewind time.

#### Whoops

An external client had a proposal for a web service which would power
part their new web application. This service sounded very simple. Data
import and some basic querying. There were plans to add additional bells
and whistles at a later date. After an initial meeting development
began.

A week later a second meeting was placed. A good few hours of
development had been invested by this point. The meeting was useful,
however some changes had cropped up. The data format had been modified,
my solution could not handle the new format. Also the querying needed
various modifications.

A week later, after several more hours of changes, the second meeting
landed. There were more changes. This time technical adjustments based
on the feedback from the clients' developers.

The third meeting introduced scope creep. Could this service handle any
potential customer going forwards? It certainly could not at present.

You should see where this is heading. Eventually the requirements
stabilized. Not until several days of my time had been taken up building
something that was not needed, only to have to tear it down and salvage
what I could.

The end result was a project I was not proud of. Due to my heavily
invested time I wanted to save as much work as I could. It would be hard
to tell my superiors we've wasted X amount of money. The project also
lacked long term stability. Each iteration built upon the next. The
feature to handle generic customers was tacked on. Had this been known
from day one, things would have looked much better both in terms of code
quality and architecture.

#### Solution

There is an easy way to transform a unknown project into a known project
- build as little as you possibly can. Do this in the shortest amount of
time to gather feedback, learn and defer decisions. After this process
you will be in the best possible shape to tackle the project. These
principles are the key to the processes within a lean start up.

#### How I Should Have Handled It

Starting with a minimal project in order to demo and deploy this would
do nothing other than returned a hardcoded JSON literal. Enough to
demonstrate and spark conversations.

During week two the discovery that a new data format had been chosen
would not matter. The feature to load data had not been written after
all. At this point the hardcoded data would be tweaked to match the new
content. Easy.

Week three would pose no threat. Technical changes around best practices
or technology are easily handled because very little code exists.

The newly required functionality discovered in week four would
prototyped, estimated and agreed. As no real work has been done, adding
this feature in would not only be achievable, it would be
architecturally sound rather than bolted on as an after thought.

#### Why?

Deferring decisions such as the above is so useful that this can be
applied to any project from my experience. Knowing how long a decision
can be deferred is dependent on the scenario, but you will be pleasantly
surprised in many cases at just how long decisions can and should be
deferred. Even for known projects the power that deferral brings is so
beneficial I tend to favour this style whenever possible. Build just
enough to gather feedback and go from there.

The key point is that very little time and energy has been invested. In
the second example of how I should have handled the client I invested
hours of my time. In reality I invested days. I was invested in the
first solution. The second solution however could be chopped, changed or
thrown away with no protest. The act of throwing code away is so
important, yet so rarely practised it will be the subject of the third
part of this series.