Title: A Unit is Not Always a Method or Class
Date: 2015-01-30 19:07
Author: Shaun Finglas
Tags: best-practices, http://schemas.google.com/blogger/2008/kind#post, 3-steps-code-quality, tdd
Slug: a-unit-is-not-always-a-method-or-class

Part three of my [Three Steps to Code Quality via TDD
series](http://blog.shaunfinglas.co.uk/2014/12/three-steps-to-code-quality-via-tdd.html).
The most important concept when coupled with the previous two points -
not every unit will relate to a method or class.

-   Part 1 - [Stop Making Everything
    Public](http://blog.shaunfinglas.co.uk/2014/12/stop-making-everything-public.html)
-   Part 2 - [Limit the Amount of Dependencies you
    Use](http://blog.shaunfinglas.co.uk/2014/12/limit-amount-of-dependencies-you-use.html)

------------------------------------------------------------------------

Most introductions into TDD use simple examples. Even the excellent [TDD
by
Example](http://www.amazon.co.uk/Driven-Development-Addison-Wesley-Signature-Series/dp/0321146530)
uses a value object in terms of Domain Driven Design. Most introductory
articles on the Internet suffer the same fate. While these are great for
demonstrations, they don't relate to what most developers need to code
on a day to day basis. It's around this point where people proclaim that
the benefit of automated testing (even after the fact) is a waste of
time.

One of my biggest [revelations with
TDD](http://www.stevefenton.co.uk/Content/Blog/Date/201305/Blog/My-Unit-Testing-Epiphany/)
was that each unit does not need to equate to a single method or class.
For a long time I followed what others did. Each collaborator would be
injected and replaced with a test double. Each class would have a
corresponding test file. However as I have [stated in the introduction,
this leads to
problems](http://blog.shaunfinglas.co.uk/2014/12/three-steps-to-code-quality-via-tdd.html).

We should test units of behaviour, not units of implementation. Given we
know we should be using as [few dependencies as
possible](http://blog.shaunfinglas.co.uk/2014/12/limit-amount-of-dependencies-you-use.html),
and we know we should [limit
visibility](http://blog.shaunfinglas.co.uk/2014/12/stop-making-everything-public.html),
each test should be simple to write. As part of the refactor step if we
choose to introduce a new class that is fine. There is no need in most
cases to extract this and introduce a test double. Every time this is
done we tie the test closer and closer to the implementation details.
Every class having a corresponding test file is wrong.

By testing a unit of behaviour we can chop and change the internals of
the system under test without breaking anything. This allows the
merciless refactoring automated testing advertises as a benefit.

##### Aren't you describing integration testing?

No. [Tests should be isolated as I've documented
before](http://blog.shaunfinglas.co.uk/2012/05/achieving-more-isolated-unit-testing.html),
but there is nothing stating they should be isolated from the components
they work with. If we isolate at the method or class level we make
testing and refactoring much harder. Due to the term "unit" being so
closely linked with a class or method, I like the [naming convention
Google
use](http://www.amazon.co.uk/Google-Tests-Software-James-Whittaker/dp/0321803027)
for their tests - small, medium and large.

Additionally an excellent [article from Martin Fowler on the subject of
unit testing](http://martinfowler.com/bliki/UnitTest.html) introduces
two new terms, solitary and sociable tests. Neither one style alone
works so the type of test you write should be based on context.
Unfortunately the industry seems to be fixated on solitary testing.

#### Sociable Tests

Work great at the aggregate root level. Does the object do what we
expect it to? It can use zero or many collaborators behind the scenes
but these are implementation details. Here we would limit the use of
test doubles as much as possible but still have fast, isolated tests. As
generalization - most automated testing should fall into this category
as the core domain of your application is likely to have the most amount
of logic present.

#### Solitary Tests

Useful at the adapter or system edge. For example, does the controller
invoke the correct application service? We don't care how it works
behind the scenes. Anything beyond this service would be a test double.
These sort of tests are more closely coupled to implementation details
so should be used sparingly.

##### Doesn't this lead to huge tests?

No, not really. As you will limit implementation details leaking into
the public API the use of test doubles will reduce. This will shrink
test setup and in most cases improve readability. Worrying about large
tests shouldn't be a problem with this style of testing. You will not
reduce the amount of tests required, however you will find them to be
much more stable and resilient than before.

</p>

