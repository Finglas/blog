Title: A Lotta Architecture - A Reply to "A Little Architecture"
Date: 2016-01-01
Author: Shaun Finglas
Tags: reply, retro, architecture
Slug: 2016/01/a-lotta-architecture-reply-to-little

A recent post about [architecture from Uncle
Bob](http://blog.cleancoder.com/uncle-bob/2016/01/04/ALittleArchitecture.html)
got me thinking and talking about a typical day in the life of a
developer. It's well worth a read. In fact at the time of writing this
reply there are 347 retweets and 288 likes - of which I was one of those
statistics.

The advice is practical and advice that I agree with. Except this is not
the full story. While deferring architectural decisions as late as
possible is a good thing, such details actually tend to be the most
important, costly and difficult parts of an application.

In the example the `BusinessRuleGateway` allows the business logic to be
coded in pure isolation, using a stub or fake. This is fantastic and
provides numerous benefits. Sadly the actual implementation of the
gateway requires knowledge of MySql. This may be obvious but the
decision of what database to use cannot be deferred or ignored forever.

Once chosen you will require intricate knowledge of how it works and is
implemented. When things go wrong and you are staring at a one hundred
line stack trace, you better hope you understand how the DB is
configured.

Additionally the gateway interface demonstrates another common problem,
[leaky
abstractions](https://blog.shaunfinglas.co.uk/2015/01/abstract-data-use-not-data-access.html).
This particular interface while coded without an implementation in mind,
is tightly coupled to a relational database. If we opted for a file
system or document database the use of transactions is now incorrect.

From my experience such implementation details end up taking the
majority of your time and effort - see the [80/20
rule](https://en.wikipedia.org/wiki/Pareto_principle). From small to
large systems, this tends to be a common running theme.

-   One project was tightly coupled to the web framework. Making a code
    change required detailed knowledge of the inner workings of the page
    request/response lifecycle.
-   Another required deep knowledge, awareness and fear of the legacy
    database schema. Code changes were easy. Plugging in a legacy
    database took horrific amounts of effort.
-   A current project is working with an asynchronous, distributed
    system. In order to be productive a solid understanding of the
    mechanics of message queues and distributed computing is required.

In some of these cases, the advice offered around abstracting
implementation details was actually used. Rarely is the problem ever
pure business logic. In a typical week I would bet a large sum of money
the majority of developers find themselves fighting with integration, or
third party dependencies, over faulty domain logic.

Deferring decisions is a sign of good architecture, but the act of
deferral or hiding behind interfaces only gets you so far. The sad state
of affairs is that any implementation detail left unchecked can swallow
applications in complexity.