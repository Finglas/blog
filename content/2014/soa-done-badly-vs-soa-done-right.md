Title: SOA Done Badly vs SOA Done Right
Date: 2014-07-01
Author: Shaun Finglas
Tags: architecture, programming
Slug: 2014/07/soa-done-badly-vs-soa-done-right

I was under the assumption I had been doing SOA for over 3 years.
Previously I have had services which did stuff, these talked to other
services which did other stuff and so on. We would group services around
functionality.

We would break these services down if they got too big to handle. Behind
the scenes the services would talk to a single database. When it came to
creating an application or system, these front end applications would
invoke various services, which in turn invoked other services. This
layered style of architecture worked for a while, so everything appeared
to be fine.

The overall architecture looked like this:

![Bad example of
SOA](http://4.bp.blogspot.com/-c5WU2EqQCtY/U8uM98_qD1I/AAAAAAAAAEs/dD5OlDqWdr4/s420/bag.soa.png "Bad example of SOA. Messy.")
Over time I began to question the benefit of this style.

-   I spent more time coding than solving business problems
-   I spent more time debugging than solving problems
-   I spent more time fixing broken deploys than solving problems
-   I spent more time writing infrastructure (to glue services together)
    than solving problems

</p>
It turns out this is actually quite a common style to SOA. But there are
some serious flaws with this layered approach.

#### Problems

-   If a service fails, the whole system is pretty much broken.
-   If the database breaks, the whole system is pretty much broken.
-   If a service is slow or breaks SLA, the whole system is pretty much
    broken.
-   In order to decouple between services, you need complex, costly
    abstractions.

</p>
#### Solution

A solution to solve these problems is to partition the domain
boundaries, vertically. The overall architecture would look like this:

![Good example of
SOA](http://4.bp.blogspot.com/-OiuVjYL4pqk/U8uI0vIxAKI/AAAAAAAAAEg/Q4Ct8linDEk/s420/good.soa.png "A good example of SOA")
##### Details

-   Each domain could consist of one or more "services".
-   Each with their own choice of data store, e.g. SQL, NOSQL, file
    system etc...
-   No domain can directly communicate with another domain.
-   If they do need to communicate, then the pub/sub model would be used
    or an ansyc command could be issued. Think .NET events or the event
    design pattern but across processes, not objects.

##### Benefits

-   Each service could fail and the impact would be minimal, simply
    rollback the deploy or fix the problem. Once the service comes back
    to life any commands or events that have not yet been processed
    would be handled. Each service would have their own message queues
    to persist commands/events.
-   Services could be re-wrote and distributed easily, proving they are
    highly decoupled.
-   No complex infrastructure, e.g. no need to map between objects
    because the service owns the whole stack. The same model could be
    used across partitions for example.
-   Works really well with agile development methodologies, e.g.
    vertical slicing of stories.

There is more to this introduction. Microservices are a hot new topic.
Being defined as "SOA done correctly". Using the second example, within
each domain there could be multiple services (or autonomous components)
that coexist. The likes of [UI
composition](http://www.udidahan.com/2012/06/23/ui-composition-techniques-for-correct-service-boundaries/)
to enable applications to be created from services is another great
benefit. This enables so called "mashups".

I'll expand on these topics over time, but I am certain this method of
vertically slicing services based upon business capabilities will be my
default approach going forward.