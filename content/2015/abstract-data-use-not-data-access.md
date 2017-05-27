Title: Abstract Data Use Not Data Access
Date: 2015-01-30 19:06
Author: Shaun Finglas
Tags: best-practices, data-access, http://schemas.google.com/blogger/2008/kind#post, programming
Slug: abstract-data-use-not-data-access

Common data access abstractions I've come across and been guilty of
implementing myself are the likes of:

-   `IDatabase`
-   `IPersistentStore`
-   `IConnection`
-   `IDataStore`
-   `IRepository`

The problem is, these are not really abstractions. If anything they add
an extra layer of indirection. One such benefit of this level of
indirection is each concrete implementation can be substituted. This
makes testing easy. Other than this, such generic solutions introduce a
**whole host of problems**.

------------------------------------------------------------------------

#### Problems

##### Abstraction

Such examples are said to be at the [wrong level of
abstraction](http://blog.codinghorror.com/the-wrong-level-of-abstraction/).
This indirection **forces** developers to work at the wrong level of
abstraction. For example, a controller has no right to be directly
querying your data store directly. If the same query is required
somewhere else you introduce duplication.

##### Big Bang Upgrade

Given such indirection offers a poor abstraction, upgrading to use a
different implementation is tricky. If we assume one hundred usages of
`IDatabase`, all of these code paths need to be migrated and tested.
This can be such a huge undertaking that upgrades are often left as
technical debt, **never to be fulfilled**.

##### Leaky Abstractions

In a similar manner to the previous point, these abstractions are poor.
[They leak implementation
details](http://www.joelonsoftware.com/Articles/LeakyAbstractions.html).
Due to this they **cannot be considered as valid abstractions**.
Consider a SQL implementation of `IDatabase`, we may have a `FindById`
method that takes an integer as the Id. If we wished to update to a
NoSQL solution the lack of a primary key causes problems. `FindById` for
the NoSQL implementation may require a Guid. There interface is now
broken.

##### Interface Bloat

Another downside of coding at the wrong level of abstraction is that the
amount of use cases increase constantly. What might begin as a humble
interface consisting of a handful of query methods soon becomes a
**dumping ground** for all sorts of exotic behaviour - specific to niche
use cases.

##### Lowest Common Denominator

Different data access providers have different capabilities, but in
order to stay "decoupled" only core functionality present in all
providers can be used. This leads to **dull, limited interfaces**
consisting of standard data access functionality. The limited feature
set can mean a poor integration. Why avoid the advanced features your
library offers?

A poor abstraction that exhibits the problems above may look like this.

<script src="https://gist.github.com/Finglas/2ad697bce48b01a17a8f.js"></script>
To retrieve a user based on the Id.

<script src="https://gist.github.com/Finglas/320fa71003931d994099.js"></script>

------------------------------------------------------------------------

#### Solution

If we abstract how the data is used and not how the data access is
performed we can avoid these pitfalls. By staying at the right level of
abstraction and not leaking implementation details we end up with a
different looking interface.

<script src="https://gist.github.com/Finglas/a8183a4b9accc5fb4862.js"></script>
The concrete implementation in this example will be a SQL implementation
using [Dapper.NET](https://github.com/StackExchange/dapper-dot-net).

<script src="https://gist.github.com/Finglas/c36fd801f48bb8e6588c.js"></script>
The usage is similar.

<script src="https://gist.github.com/Finglas/cec4daf23ef4aea11a96.js"></script>
The key point here is that we solve the problems of the "generic"
solution.

-   `IUserQuery` is a better abstraction, it allows selective upgrades.
    This use case will have limited use, meaning updating a handful of
    references is easier than updating every data access component in
    one go.
-   The fact we use a SQL database as our store is hidden, no details
    leak. `UserId` encapsulates how we identify users, if we were to
    switch to a NoSQL store our consumers would be unaware.
-   One of the biggest benefits is the ability to use our third party
    library to its fullest. Rather than wrapping Dapper we can make use
    of it directly, making use of any special features it offers, rather
    than conforming to a limited subset of an API.

------------------------------------------------------------------------

##### Aren't We Introducing Lots of Classes?

More, but not "lots". However this is a common complaint when the above
solution is proposed, though given the vast benefits included this trade
off is certainly worth it. Additionally, each query or repository that
is implemented in this manner is easier to develop and test due to
closer adherence to the Single Responsibility Principle.

##### How Do We Unit Test SqlUserQuery?

You don't. In this example we make use of the third party library
directly. The benefits discussed prior justify this, though it means
unit testing is not possible. Therefore you should apply integration
testing against a real data store. The rest of the system will be coded
against the abstraction, so unit tests can be applied as normal here.
Any attempt to "abstract" or wrap the third party will remove many of
the benefits of this solution, so don't worry about it.

------------------------------------------------------------------------

For a great discussion on this topic, check out a talk by [Kijana
Woodard](http://ayende.com/blog/166594/ravendb-conf-videos-abstracting-ravendb-dont-do-it)
for more examples.

</p>

