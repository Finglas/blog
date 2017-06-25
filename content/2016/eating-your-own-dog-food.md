Title: Eating your own Dog Food
Date: 2016-03-01
Author: Shaun Finglas
Tags: retro
Slug: 2016/03/eating-your-own-dog-food

Also known as *dog fooding*. It's an odd term, [with roots dating back
to 70's adverts and the even more
bizarre](https://en.wikipedia.org/wiki/Eating_your_own_dog_food#Origin_of_the_term).
In software development the idea is simple. Use the software you produce
to make it better. This can be taken to the extreme with examples such
as Notepad++ being built with Notepad++, or the Github team using Github
internally. These examples mean the product is as good as it can be from
real life use.

#### API's

Dog fooding works great for APIs. When the boundary of a system is an
API building a fake test UI is a wise move. This integration acts as if
you were the user. If you can solve the basic uses cases that your
integrators need you can be confident the API is fit for purpose.
Integration highlights problems and areas for improvement. Building a
test UI is a very easy step to carry out which is also useful for
demonstrating and documenting the API to others.

The danger of not eating your own dog food when producing APIs is
detachment from what your users will be trying to do, versus what you
implement. In many cases this means that while your API may be fully
compliant with the latest standards, framework and technology, it is not
actually fit for purpose. Naturally this will incur overhead when the
users raise issues that need resolving, often late in the day.

#### Libraries

It is often tempting to extract a library for a common task. As always
[try to fight this urge until at least the third
time](https://blog.shaunfinglas.co.uk/2015/03/reused-abstraction-principle.html).
As well as this try to use the library yourself before releasing. If you
can use this library in at least three places you very well may have a
successful piece of software. If the answer to this question is no, the
library may not be as useful as you think.

Libraries that have not been built using dog fooding are often clunky,
unintuitive and frustrating to use. Every developer could name numerous
examples that would fit this criteria, but the opposite is also true.
The use of dog fooding tends to force libraries into the later.