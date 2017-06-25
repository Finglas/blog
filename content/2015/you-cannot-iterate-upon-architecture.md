Title: You Cannot Iterate upon Architecture
Date: 2015-11-01
Author: Shaun Finglas
Tags: architecture, agile-architecture-series
Slug: 2015/11/you-cannot-iterate-upon-architecture

This is the first part of a series of posts as to why gradual iteration,
doing the simplest thing that can possibly work over a software project
fails in many cases. This series will explain why this is the case, and
provide solutions.

-   Part 2 - [Don't Build a
    Thing](https://blog.shaunfinglas.co.uk/2015/11/dont-build-thing.html)
-   Part 3 - [Throw Code
    Away](https://blog.shaunfinglas.co.uk/2015/11/throw-code-away.html)

------------------------------------------------------------------------

[Spotify has gave a
talk](http://blog.crisp.se/2013/01/13/henrikkniberg/how-spotify-builds-products)
on how it builds products and manages teams internally. This provides
some great insights and advice. As part of this an incredibly effective
image is used. This shows the production of a form of transport to
travel from A to B.

![Building a car from a skateboard.](http://3.bp.blogspot.com/-GIv_yj7SN08/VkDhOX_5DoI/AAAAAAAAAIo/12OKoGVoCvY/s1600/images.duckduckgo.com.png)

In the first half of the image, the product is built in iterations. Each
step adds to the next. It is not until the fourth step that the product
is able to take passengers from A to B. Agile development aims to solves
the issues around this.

The second half of the image is built iteratively. The goal is still the
same. A product to travel from A to B. From the first version this goal
is complete. However the team would be embarrassed to release in this
state. Further iterations are carried out as the team learns more.

From my experience building software in this manner only works half of
the time. Any software projects from my first line of code up until
present day fall into one of two categories.

#### Known Projects or Unknown Projects

A known project would be where the destination is clear and well
defined. Internal development projects, refactoring, or replacement
would fall into this category. Easily half of my professional time has
been spent on projects where we know what we are building and when it
must be complete by.

The second type of projects is where the destination is unknown. You are
working for an external customer directly. On a regular basis you
regroup with the client. You gather feedback and iterate. Over the
course of this process your destination may very well surprise you,
along with the route you use to get there.

#### Refactoring is Class or Method Level Only

You could claim the image works for unknown projects. At any point the
client (internal or external) could put a halt on development after
their vision is complete. For known projects, the area this image fails
is simple - if a car is required, build a car. If this is demonstrating
a known project, building only then to start recycling, refactoring and
forming the code into another shape is costly. Sticking with the vehicle
analogy - building a car is complex. In one iteration it would not be
possible to gather feedback until it was too late. Much time and
resources would be wasted.

Translating to a software example, this would be the same as building a
complex web application. The goal is known, yet the first stab is a HTML
page. This is followed by some simple sever side logic. On top of this
we add an ORM. Further iterations thrash and push the code around. Early
simple decisions start to come back to haunt us. This technical debt is
either repaid or ignored. As further iterations follow the architecture
of the application suffers. Through sheer force of determination the web
application is complete. Usually there are many compromises along the
way. Further enhancements or changes could be costly.

#### Solutions

For unknown projects there are two solutions. First and foremost build a
[walking
skeleton](https://blog.shaunfinglas.co.uk/2015/05/walking-skeleton.html).
Using the vehicle example, the first iteration of a known project should
produce the frame of the car. Other than wheels there would be very
little else here. However this is still a car, though limited in
functionality and features. Using the software example this would be the
core flow of the web app. Either hardcoded in places or built using
scaffolding. You would still be embarrassed to release this.
Architecturally you have all the core parts you need. The benefit of
this is that future iterations simply build upon the good, known
framework. The foundations of the project are stable. There is no fear
that after several iterations you stumble upon a technical
implementation issue.

The second solution is turn an unknown project into a known project.
This sounds difficult but there is a remarkable easy way to achieve this
- the subject of the next post.