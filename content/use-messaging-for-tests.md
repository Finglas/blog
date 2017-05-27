Title: Use Messaging for Tests
Date: 2017-05-25 16:16
Author: Shaun Finglas
Tags: http://schemas.google.com/blogger/2008/kind#post
Slug: use-messaging-for-tests

Part one of my series on Acceptance Tests for Asynchronous Messaging.
See the introduction for the definitions and example scenario.

1.  Use Messaging for Tests
2.  Assert End System Results
3.  Rely on Monitoring and Auditing
4.  End System Results plus Monitoring

------------------------------------------------------------------------

One approach is to actually rely on async messaging for the tests
themselves. Using the previous example we could simply subscribe to the
messages that service A, B and D produce. While this leads to stable
tests in theory, the actual results can differ wildly. Assuming service
A generates a message within the test timeout period our test will
safely pass. However if no message is generated, or the message is slow
to process, or retries are triggered, the test may either take some time
to complete or simply fail.

Assuming service C is outside of our domain (controlled by another team,
department, company etc) you can easily run into problems around scope.
If certain messages are required, you can often leak internal details
from another domain into your tests, something which the use of services
is meant to prevent. Why are tests any different in this case? This
tends to lead teams into developing internal stubs which trigger
messages on pre-defined input. While this works it certainly violates
the idea of boundaries between domains. If service C was to change, how
do we change the stub? How would we know? The maintenance of stubs that
use messaging is an additional overhead. One way to counter-act this is
to have the external service provide a messaging stub. This use of
nearest neighbours works well as long as the provider of the service is
the owner of the stub.

Another factor to consider with using messaging for tests is complexity.
Most programming languages allow a HTTP request to be sent in a few
lines of code, with very little ceremony. The use of durable messaging
tends to lead to the opposite. While this will vary on language,
framework and tooling the complexity should not be underestimated. This
is especially true if the automation of such tests is to be written by
those without familiarity of the underlying implementation.

While services do not dictate the use of HTTP as a hosting model, the
use of REST API's is the dominate force in this area. With many
different front end applications consuming the services this tends to be
a practical decision. Given this the use of messaging within acceptance
tests is a poor choice. If messaging is nothing more than an
implementation detail, tests relying on messaging are actually leaking
implementation details. Future changes or additions will cause these
tests to fail, even though functionally the system is correct. The pain
here can be reduced by writing DAMP tests though the underlying issue is
still present.

In general the use of messaging is a poor solution for acceptance tests.
While you can fight through some of the technical issues messaging
introduces, the leaking of implementation details and general complexity
mean there are better solutions. While acceptance tests make poor
candidates for this style of testing, when working inside the domain the
use of domain events or event sourcing can massively simplify testing
activities. In these lower level tests the strategy of publishing and
subscribing to events is highly recommended.

</p>

