Title: Why I Don't Like Mocking Frameworks
Date: 2015-08-04 20:39
Author: Shaun Finglas
Tags: http://schemas.google.com/blogger/2008/kind#post, tdd, mocking, unit-testing
Slug: why-i-dont-like-mocking-frameworks

Disclaimer: By *mocking* framework I generalize anything that includes
support for stubs and mock objects.

------------------------------------------------------------------------

The use of mocking frameworks was a difficult part of my TDD journey.
Not only are newcomers expected to get their head around the basics of
the practice there are now new tools to contend with. To make matters
worse there is a lot of mocking frameworks out there with differing
quality qualities and suitability.

The use of mocking frameworks includes a variety of disadvantages.

-   Readability suffers in most cases. You often find yourself asking
    *what is exactly happening here?* The frameworks themselves usually
    impose these constraints and make the issue worse.
-   [The use of frameworks tends to lead to header interfaces and not
    role interfaces being
    used](http://blog.ploeh.dk/2010/12/02/Interfacesarenotabstractions/).
    IDE's usually have a factor in this as they make this anti pattern
    so very easy to introduce.
-   A lot of developers are not aware of what these frameworks are doing
    behind the scenes. This can lead to confusing tests and a general
    lack of understanding.

#### Solution

My preference is to use hand crafted test doubles. While these are
looked down upon by some, they offer numerous benefits.

-   [Stubs and Fakes are easier to
    understand](http://stackoverflow.com/a/6674671), write and maintain
    when hand crafted.
-   Manual test doubles read easier. The key benefit here being able to
    name implementations after their use and function.
-   Hand crafted test doubles promote reuse. It is likely that such
    doubles will be used across numerous tests. Once created code
    duplication actually reduces.
-   Hand crafted test doubles are a [prerequisite to enable contract
    testing](http://blog.shaunfinglas.co.uk/2015/07/the-benefits-of-contract-testing.html).

The actual implementation of these hand crafted doubles is minimal. In
most cases simply providing the arguments as constructor or method
parameters works. For more complicated scenarios [DAMP
tests](http://blog.shaunfinglas.co.uk/2015/04/dry-vs-damp-in-tests.html)
can be used.

One area where frameworks provide a benefit is that of mock objects. In
non trivial examples the requirements to verify numerous parameters and
configurations can be verbose to hand craft. However there are
alternatives to hand crafted test doubles such as the self shunt pattern
which will be expanded upon in a future post.

</p>

