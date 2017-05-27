Title: Test Your Live System using Live Service Tests
Date: 2016-08-24 06:56
Author: Shaun Finglas
Tags: testing, http://schemas.google.com/blogger/2008/kind#post, productivity
Slug: test-your-live-system-using-live-service-tests

Traditionally there are three categories of functional tests.

-   Acceptance
-   Integration
-   Unit

This is often refereed to as the testing pyramid. Unit tests form the
bulk of your suite, followed by a smaller subset of integration tests.
Acceptance tests that cover features should be the tip of your testing
strategy, few in number. These are great but there is a missing suite of
tests - live service tests.

-   Live Service Tests
-   Acceptance
-   Integration
-   Unit

#### Live Service Tests.

The role of live service tests (LST) is to test the live system against
the production environment and configuration. LST would be fewer in
number than acceptance tests. Unlike acceptance tests, these should run
constantly. Once a run has completed, kick of a new test run. This will
require a dedicated machine or piece of infrastructure, but the value
provided is well worth it.

LST should focus on journeys instead of functionality or features. In
contrast to acceptance tests a user journey would be the core purpose of
the system. For example, a LST suite to cover this blog would ensure the
home page loads, an individual post can be loaded, and the archive is
accessible. The rest of the site such as comments or social media
interactions could be broken, but the core purpose of the system is
working. Readers can read and browse the blog. If at any time the tests
detect a failure in the core journey there is a big problem.

#### Why

LST offer the fastest feedback possible due to the fact they are
constantly running. It is far more desirable to detect a problem before
your users do. Naturally LST offer great protection after deploys.
Deployment of new code is one of the times you are more likely to
encounter issues, so a suite of tests triggered after a deployment is a
natural fit. LST also protect against unplanned events. In my
experience, exceeding disk space, DNS failure, third party issues and
more have all be detected.

#### How To

Adding another suite of tests may sound like increased effort but the
cost associated with LST is rather low. Sometimes acceptance tests can
be run as LST, meaning no extra effort. Care must be taken here if the
tests perform anything destructive or anything that interacts with third
parties.

Alternatively writing LST is simpler than standard acceptance tests. The
same tooling can be used such as Selenium, NUnit and so forth. As the
tests themselves focus on journeys rather than functionality, the tests
are often less complex to write.

The only difficulty LST introduce is the fact they are executing against
the live system. Consider interactions with a third party. Using a real
account on the real system may be problematic. One way to get around
this issue is to embed test functionality within the system itself. For
example you could set up a test account which the tests use. Instead of
executing against the third party system, the dummy account is used.
Likewise most third parties have test accounts which can be setup and
used instead.

LST are a nice compliant to a diagnostic dashboard. If your dash is
reporting no issues, and your tests are green, you can be confident the
system is operating in a *good enough* state.

#### Lessons

-   Functional tests are not enough.
-   Use live service tests to test the real production system.
-   Run live service tests constantly for the earliest feedback
    possible.
-   Alter production code to introduce test functionality.
-   Make use of test accounts and anything else that third parties may
    offer.

</p>

