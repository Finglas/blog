Title: UI Composition Techniques for Services
Date: 2016-07-01
Author: Shaun Finglas
Tags: microservices, SOA
Slug: 2016/07/ui-composition-techniques-for-services

When using services be it SOA, microservices or some other hybrid
approach, at some point you will need to display an aggregation of data
onto a UI. This simple task can actually involve some complexity and
hidden pitfalls.

As an example, this blog could be powered by three independent services.
A comment service, a post service and a archive service. Displaying this
content on the page could involve a few different approaches both with
pros and cons. Each vary in terms of benefits and complexity.

-   Service Composition
-   Server Side Composition
-   Backends For Frontends
-   Frontend UI Composition

------------------------------------------------------------------------

#### Service Composition

Composition within independent services should be avoided at all costs.
In these cases service A invokes service B which invokes service C,
which has a dependency on A and so on. The problems such composition
introduce defeats any benefits that a service based approach brings. In
short [composing data in this manner will lead to
problems](http://blog.shaunfinglas.co.uk/2014/07/soa-done-badly-vs-soa-done-right.html).

------------------------------------------------------------------------

#### Server Side Composition

Invoke each service behind a single request and perform composition on
the server. Return the results of the aggregation which can then be
processed by the UI. In most cases a *request* will be a request over
HTTP.

##### Pros

-   Single request to fetch all data.
-   Single server side place to change if UI requirements change.
-   Forms an anti corruption layer in front of the independent services.
    Client specific changes do not leak down into the service.

##### Cons

-   Coupling is moved to the server side. Harder/slower to change
    compared to HTML/JS/UI layer.
-   Handling failures must be considered more so than client side
    composition.
-   Timeouts or lack of responses must be considered using asynchronous
    techniques.

##### Where Does The UI Live?

Due to the nature of having to serve up data for the UI layer to
consume, it makes sense to purely store the UI components within the
host application. In this case the whole host application will use the
same UI techniques.

------------------------------------------------------------------------

#### Backends For Frontends (BFFs)

[An alternative which builds upon server side
composition](http://samnewman.io/patterns/architectural/bff/) is server
side composition but performed individually based on the UI required. In
other words, a set of server side applications for each host are
created.

As UI clients can differ drastically a single server side composition
technique may not be sufficient. Mobile devices may require a slimmed
down version of data, while desktop dashboards may prefer large
quantities. Additionally it is quite common to find certain clients
asking for additional fields or requirements specific to their client
implementation. In these cases BFFs make a great deal of sense.

##### Pros

-   Same pros as server side composition.
-   BFFs allow full control of server side composition tailored to the
    clients.
-   Specialized BFFs reduce change and prevent independent services
    handling UI specific edge cases.

##### Cons

-   Same cons as server side composition.
-   More moving parts, though BFFs should be owned by the client
    themselves for true autonomy.

##### Where Does The UI Live?

The same guidance as server side composition stands. Where the actual
BFF lives depends on how it is used. If the mobile client is expected to
have multiple implementations then a standalone service would be
required. Alternatively if only a single mobile platform is targeted,
then the service could live within the host application itself.

------------------------------------------------------------------------

#### Frontend Composition

[Invoke each service and display its data independently via the
client](http://udidahan.com/2012/06/23/ui-composition-techniques-for-correct-service-boundaries/).
The host application will include the front end of each service by
conforming to a common standard such as Javascript or other UI
components. The use of IDs and client side identifiers will be required
to ensure all services are linked in some manner.

##### Pros

-   Failure tolerant by default, if a single request fails the others
    carry on processing.
-   JS/UI layers make asynchronous calls easy, composition is a natural
    fit.
-   Weakest form of coupling is in the UI layer - easier and cheaper to
    change.
-   Flexible as you can create *mash ups* that would otherwise violate
    service boundaries.

##### Cons

-   Multiple requests to fetch content (four HTTP requests using the
    blog example above).
-   Aggregation may be complex. You may need to use more than just plain
    Javascript or face complex, coupled JS.
-   Depending on where the UI layer is stored, you may be coupled at the
    UI level due to the same framework or approaches needed across each
    service.

##### Where Does The UI Live?

Storing the UI within each service is ideal on paper, but in practice
has some limitations. Each service can vary and iterate at its own pace
which is fantastic as long as the integration of the service remains
unchanged. Unfortunately the downside is that each service is actually
independent in terms of the UI. This means that versioning the front end
component becomes an issue. Likewise there is nothing stopping different
services using different libraries or frameworks. If the UI component
requires any server side additions this becomes even harder. For example
a host application written in one language will be incompatible with
other services if they differ. The final issue relates to storing UI
components outside of host application frameworks. Many frameworks
simply make this either impossible or very difficult to achieve.

Using the host application to store the UI components side steps the
disadvantages and issues above. While you are at the mercy of the host
application to integrate each component, this is not a show stopper.
Chances are most applications have multiple views, so a single UI
component would never be reusable across applications. Additionally the
use of thin vertical slices should mean that even though the UI
component is physically separate from the service, there is no reason
why the two cannot be worked on in conjunction.

A final factor to consider is that there is no reason why a hybrid
approach cannot be taken. Each service should store its own UI
component, but also allow host applications the ability to integrate.
This UI component can act as a form of dog fooding as well as providing
an excellent development and test bed. It is far easier to work and test
a small widget with an automated test than it is to exercise this within
the context of a full blown application.

------------------------------------------------------------------------

#### Lessons

-   Avoid the use of internal service composition - remote calls to
    third parties being the obvious exception to this rule.
-   There is no best approach overall, the chosen solution will vary
    based on application.
-   Server side composition has benefits, but client side UI composition
    opens up new possibilities.
-   Client side composition seems more complicated but in reality it is
    merely different, though does require some up front planning.
-   Default to using the services directly, only introducing a BFF if
    client requirements differ or client requirements are being forced
    upon the independent services.