Title: Top Down vs Bottom Up
Date: 2015-03-29 10:13
Author: Shaun Finglas
Tags: http://schemas.google.com/blogger/2008/kind#post, design, agile, development
Slug: top-down-vs-bottom-up

**Top down development** has you starting at the highest point in the
application that you can. From here you code down until there is nothing
else left to develop. Once you reach this point you should be code
complete. Along the way you may need to stub out areas that have not yet
been created, or designed.

**Bottom up development** has you starting at the lowest point in the
application. The idea being that this part of the application has the
most complexity or will be the most important. You will build the system
up from a series of smaller components.

[Top down development and bottom up
development](http://en.wikipedia.org/wiki/Top-down_and_bottom-up_design)
was introduced to myself in my early days of university. At the time the
distinction didn't really mean much - I was very much a developer who
would work from the bottom up.

Over time I have completely switched my stance on this. I believe agile
practices and TDD are the reason for this change. I feel so strongly
about this that I would go as far as to claim that **within an agile
team - bottom up development is an anti pattern**.

Consider the following tasks to be completed on a team of four
developers.

-   Create controller - *main entry point, request mapping.*
-   Create service - *service layer, simple business logic.*
-   Database query - *thin wrapper around complex DB query.*

With a bottom up approach a pair of developers could work on the complex
database query. After some time they would have this working. The other
two developers could start with the controller or service.

The problem with this approach comes from the **painful integration
process**. The developers working on the service might be coding against
the interface the team discussed during a planning session, while the
developers on the query may have had to change their approach.

<script src="https://gist.github.com/Finglas/42c9e3e19c10f9fcffb3.js"></script>
This example is trivial, but imagine a story with thirty tasks, more
developers and more complexity and this bottom up approach is difficult.
Over the past few years my top down approach has evolved.

My first step would be to **stub out the workflow** with the above
implementation. There is no real logic here - only the objects
collaboration is implemented. At this stage there are **no tests, TDD
would not be used**. After all there is no logic here. The code is so
simple it can be reasoned about with peer review, planning sessions and
so on.

<script src="https://gist.github.com/Finglas/0309d16a3d45ebf732dd.js"></script>
At this stage **all of the tasks are open for any developer to pick
up**. If a breaking change was required, there would be no way for one
pair to commit these changes without the other pair knowing. Another
benefit of this approach is that an end to end acceptance test could be
wrapped around the functionality from the get go.

As **part of these tasks each developer would use TDD**. Remember no
tests exist at this point. Building up the tests in stages would ensure
the logic of how the objects collaborate is preserved, and ensures that
the actual domain logic that is implemented is correct. **Does this mean
we aren't doing TDD? No, of course not**. The tests will drive the
implementation. If we need to introduce new objects that is fine - these
simply become implementation details that the other devs need not worry
about as long as the workflow is not broken.

This approach to top down development isn't new, though many don't
appreciate its benefits. I plan on expanding on this style of pragmatic
TDD in the coming months.

</p>

