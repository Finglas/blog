Title: Recursively Building a Web Service using the same Web Service
Date: 2012-03-01
Author: Shaun Finglas
Tags: testing
Slug: 2012/03/recursively-building-web-service-using

Back during the later part of 2011 there was a common theme occurring in
our retrospectives each week. How can we replicate our live environment
as close as possible?

We took steps to achieve this goal by creating a single machine image to
ensure all our machines were configured correctly. Another quick win was
to ensure certain aspects of our live data was restored to our local
development databases during the night. This enabled us to take stack
traces from our logs, and quite literally paste them into our IDE and
replicate the users problem instantly. Without the same data set we
could have seen different results. Despite these positive steps, there
was a missing link in our replication process. How do we simulate the
traffic of our live environment? As an example, we average anywhere from
four to five thousand calculations per minute with our current web
services, with our local and demo environment no where near this figure.

During 2011 I found myself involved in many deployments in which despite
heavy testing I was uneasy. On our demo environments we could throw the
same amount of load against our services, yet sometime after deploying
our service would fall over. We would quickly have to revert and go back
to the drawing board. The problem we had despite our traffic being
mimicked in terms of volume was the load was not real. Our customers
however have many more variations of requests that we were simply not
predicting. The other obvious issue was during local development, the
service may well handle the same volume of traffic, yet once live and
the process has been running for a few hours - things might go bump.
Factors such as memory or timeouts being the culprits here.

Collectively we had a few ideas on how to solve this. We looked into low
level solutions such as directing traffic from IIS/apache towards other
servers. We examined other load testing tools, and we even contemplated
creating our own load creator. This internal tool would go over our
database and fire off a number of requests at our demo environment. I
felt uneasy with all these solutions. They were not "real" enough. I
wanted the real time traffic to be submitted to our demo services, only
then could we have full confidence in our work.

My idea was rather radical in the sense it was so easy, yet dangerous
enough that it might just work. I proposed we integrated our own
service, into itself. In other words, just before our service returns
the results of the calculation, it takes the users request and submits
it again, against our demo environment. The same service would be
recursively submitting into itself. In order to ensure we did not affect
the speed of the service, the submission is performed via an async call,
meaning if this second call was to die the live service would be
unaffected. The obvious downside here was that in order to test this, we
needed to deploy the changes to our live service. This was achieved via
a [feature toggle](http://en.wikipedia.org/wiki/Feature_toggle), meaning
at any time we could turn the feature on or off without affecting any
customers.

The end result of this was that when the feature is enabled, the traffic
on our live service is sent to our demo service. This allows us to
deploy experimental or new features and changes to the demo environment
and check them under real load, with real time data. If all goes well
after a period of time we can deploy to our live service, if not we roll
back and no one is the wiser.