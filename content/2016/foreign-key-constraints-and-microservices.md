Title: Foreign Key Constraints and Microservices
Date: 2016-05-01
Author: Shaun Finglas
Tags: microservices, distributed-systems
Slug: 2016/05/foreign-key-constraints-and

Database constraints when used in relational databases are great. They
ensure data integrity at the lowest level. No one would argue against
using them in practice. Essentially constraints can be thought of as
assertions against your database. Rules such as requirement, default
values and foreign key constraints double check your use of the
database. This ensures your application is interacting in a sane manner.
Databases often out live applications therefore constraints also ensure
integrity long after the application has been replaced or modified.

#### Distributed Systems

Distributed systems change how foreign key constraints should be
considered. As distributed systems own their data, each piece of data
that is mastered by a single service should ensure integrity via foreign
key constraints. However outside of this boundary the use of foreign
keys should be avoided. This sounds disturbing at first. Especially
given the traditional approach of a single system backed by a single
database.

#### Example

Consider a blog post service that provides a selection of posts. The
service would be responsible for everything related to blog posts, but
nothing more. The comments for the site are a separate service, yet
there is clearly a link between posts and comments. For example, in
order to display both posts and comments a link is needed.

    - tblPosts (blog database)
        + Id
        + Title
        + Date
        + Body

Each post would store data related to the blog post itself.

    - tblComments (comment database)
        + Id
        + PostId
        + AuthorId
        + Message
        + Date

The comment service would include a reference to each post that the
comment is linked to. In this case both `PostId` and `AuthorId` would
not use foreign key integrity as other services master this data.

If this was a single database both `PostId` and `AuthorId` could enforce
integrity, however as each service is independent this is not possible.
With physically separate databases this lack of link is quite obvious.
Working around this in application code would introduce subtle bugs, and
temporal coupling. Such solutions are best avoided.

#### Check Formats

When using the comment service, this approach leaves you with very
little work to do other than simple format checks. The format of a
`PostId` and `AuthorId` should be known, so the comment service can
validate at this level. The core benefit is both the blog post service
and comment service are highly decoupled. The comments could be changed
to another service altogether, even a 3rd party provider, yet other
services would remain unaware.

#### Valid Format, Invalid Data

Format checks will only provide so much value. There is nothing stopping
a valid request for a blog post that does not exist. In cases such as
this there are a few options. One is to provide a compensating action.
Periodically delete any comments that do not have corresponding blog
posts. An alternative would be to rely upon events. Only insert comments
when a blog post is added, likewise when the service publishes the fact
a post has been removed, any associated comments could be deleted.

#### Many Services, Single Database

Confusion and resistance around the use of foreign keys is often found
when transitioning from a single database, to a single database operated
upon by multiple systems. Teams adopting microservices find themselves
in this dilemma usually when a large, legacy database is involved. In
these scenarios existing constraints may need to be removed, or
modified. Another technique is to have the independent services add
dummy data in order to pass database constraints. While this is far from
ideal, this pragmatic solution can work well while databases are being
separated.

#### Lessons

-   Use foreign key constraints when using a single database via a
    single application.
-   Modify, replace or drop constraints when multiple services are
    writing to a single database.
-   Independent services should own their own data. Only enforce
    integrity within service boundaries.
-   Outside of service boundaries, use format checks to prevent errors.
-   Rely on compensating actions or events for data management.