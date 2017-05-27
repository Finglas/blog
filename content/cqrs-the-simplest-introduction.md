Title: CQRS - The Simplest Introduction
Date: 2015-04-23 17:51
Author: Shaun Finglas
Tags: http://schemas.google.com/blogger/2008/kind#post, cqrs, programming, SOA
Slug: cqrs-the-simplest-introduction

[CQRS or Command Query Responsibility
Separation](http://martinfowler.com/bliki/CQRS.html) is easy to
understand but it can become complex due to various levels to which
developers take the principle behind it. Simply - [CQRS is two models,
where the used to be
one](http://codebetter.com/gregyoung/2010/02/16/cqrs-task-based-uis-event-sourcing-agh/).
Nothing more at its heart.

Take the Customer aggregate below. This exposes both commands as void
methods and queries as methods with return types. Public state is
leaked, but needed in order to display or persist the data. Many
frameworks or libraries require public accessibility in order to
function.

<script src="https://gist.github.com/Finglas/c1d94351de393f782435.js"></script>
CQRS states we split commands from queries. This means we end up with a
pure Customer aggregate root that exposes behaviour only. Likewise we
end up with a basic application service that simply returns data.

<script src="https://gist.github.com/Finglas/dd2ff5c706847c3f4734.js"></script>
#### Benefits

##### Commands

-   Domain model is purely behaviour.
-   No data is exposed, public fields/methods gone (no getters/setters)
-   Only way to modify customers is via the commands - encapsulation is
    preserved.
-   Less relationships simply for querying/persistence (has-a
    relationships)
-   Testing is easier, check event raised/command issued rather than
    state
-   Allows task based UI's, rather than CRUD focused interactions.
-   If you use repositories, you only need a GetById method.

##### Queries

-   Queries can be simplified - in many cases by a huge amount. Just
    read from the data store, no need to create relationships between
    models.
-   You can [use direct data access, rather than repositories or other
    abstractions](http://blog.shaunfinglas.co.uk/2015/01/abstract-data-use-not-data-access.html).
    This has a lot of benefit.
-   It's easy to develop, less layers and moving parts.
-   You can independently replace persistent storage mechanisms per
    query based on use cases.

#### Complexity

-   CQRS is not architecture - it is a pattern, often used within
    boundaries of a system.
-   [Event Sourcing and Eventual Consistency don't need to be
    used](https://lostechies.com/jimmybogard/2012/08/22/busting-some-cqrs-myths/),
    but they can be employed if needed. Many examples of CQRS include
    these, making CQRS appear more complicated than it really is.
-   You can separate read and write stores. For example, store the read
    data in document store, while storing write data in a relational
    database. This increases complexity and means that seeding/feeding
    data becomes an issue. [A collaborative domain can signal the need
    to do this](http://www.udidahan.com/2011/04/22/when-to-avoid-cqrs/).

CQRS is an easy concept, that introduces many benefits. However
implementation of this pattern can vary from simple, to complicated. The
extent to which CQRS is implemented should be judged on a case by case
basis. Many systems can get away without separating read and write
stores, yet still enjoy the benefits that this pattern provides.

</p>

