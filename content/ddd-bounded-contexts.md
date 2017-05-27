Title: DDD - Bounded Contexts
Date: 2016-06-14 07:25
Author: Shaun Finglas
Tags: best-practices, http://schemas.google.com/blogger/2008/kind#post, DDD, development
Slug: ddd-bounded-contexts

A single domain can grow large when applying Domain Driven Design. It
can become very hard to contain a single model when using ubiquitous
language to model the domain. Classic examples prevalent in many domains
would be `Customer` or `User` models. A bounded context allows you to
break down a large domain into smaller, independent contexts.

In different contexts a customer may be something completely different,
depending on who you ask and how you use the model. For example, take
three bounded contexts within a typical domain that allows customer
administration, customer notifications and general reporting.

#### Example

##### Notification Context

A customer is their account id, social media accounts, email and any
marketing preferences. Anything that would be required to uniquely
identify a customer, and send a notification.

        + Id
        + Email
        + Marketing Preferences
        + Social

##### Reporting Context

When reporting customers are nothing more than statistics. A unique
customer ID is more than enough just for aggregation and statistic
collection.

        + Id

##### Account Context

Allowing the customer to administer their account would require anything
personally related to the customer to be modelled.

        + Id
        + First Name
        + Last Name
        + Address
        + Email

Despite the common elements such as Id and email, the other elements are
specific to the context in which the customer is used. One of the
biggest mistakes I've made by ignoring a bounded context is to see [a
common model and try to apply this
everywhere](http://blog.shaunfinglas.co.uk/2015/06/dry-vs-coupling-in-production-code.html).
This leads to less code, but increases coupling. A single small change
in one context can cause a rippling effect. In fact the best solution is
to have a customer model per context.

The result of this approach is you will end up with at least three
models using the example above. While structural duplication increases,
coupling decreases. Each context can change and evolve at its own pace.
This is a good thing. No business logic here is being duplicated, only
the model. As each context operates in its own speciality, there should
never be a case where this is problematic.

#### Lessons

-   Structural duplication outside of bounded context is not a bad
    thing.
-   Resist the urge to use a base class for common attributes. This is
    especially true if you use an ORM or anything that will couple you
    further when these models are used.
-   Ending up with multiple models per bounded context is likely going
    to happen, embrace it.

</p>

