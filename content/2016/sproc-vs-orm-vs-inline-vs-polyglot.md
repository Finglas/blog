Title: Sproc vs ORM vs Inline vs Polyglot
Date: 2016-02-01
Author: Shaun Finglas
Tags: retro
Slug: 2016/02/sproc-vs-orm-vs-inline-vs-polyglot

With relational databases the common data access patterns tend to fall
into three core options.

-   Direct access via inline SQL
-   Stored procedures using the standard library
-   ORM frameworks or libraries

Individually these have both pros and cons, often leading to heated
debate and discussion.

#### Inline

-   Leaky abstractions.
-   Dangerous in places via SQL injection.
-   Quick and dirty solution.
-   Non testable by default.
-   Useful for integration testing where dynamic input is required and
    safe.

#### Stored Procedures (standard library)

-   Can be clunky and low level to use in places.
-   Non testable by default.
-   Allows the use of DB specific features internally.
-   Easy to tune and optimize as long as interface is stable.
-   Developers can optimise the execution of queries.

#### ORMs

-   Testable by default.
-   Complex, large and difficult to use correctly.
-   Leaky abstractions.
-   Optimisation is harder, especially for DB engineers.
-   Mini or lightweight alternatives exist, with less of the downsides.

#### Polyglot Persistence

The actual decision of which data access method to use can be a non
issue providing a good abstraction is used. Whether you use inline SQL,
stored procedures or full blown ORMs is beside the point. [Instead of
abstracting the implementation detail, focus on the role the object or
function has to
play](http://blog.shaunfinglas.co.uk/2015/01/abstract-data-use-not-data-access.html).
A benefit of this approach is the ability to mix and match data access
patterns. Polyglot persistence is gaining more traction where alternate
data storage solutions are more appropriate.

#### N+1

One common flaw that all these data access patterns can have is the [N+1
problem](http://blog.shaunfinglas.co.uk/2016/02/the-n1-problem.html).