Title: Loops vs Functional Programming Styles
Date: 2015-08-11 20:31
Author: Shaun Finglas
Tags: functional, http://schemas.google.com/blogger/2008/kind#post, functional-programming, javascript
Slug: loops-vs-functional-programming-styles

The following examples are four of the most common functional
programming patterns that appear in mainstream languages though they may
be known under different names.

Being a [fan of CQS and
CQRS](http://blog.shaunfinglas.co.uk/2015/04/cqrs-simplest-introduction.html),
queries work great when coding using the functional style. While this is
completely subjective in terms of style there is another benefit -
composition. In other words the functional styles below can all be
joined together with minimal changes. A traditional loop would require
additional modifications. The benefit composition provides is similar to
the [pipes and filter
architecture](http://www.enterpriseintegrationpatterns.com/PipesAndFilters.html)
- it is very easy to change the behaviour of the pipeline by simply
adding or removing statements.

Composition and concise code aside, traditional loops should not be
avoided fully. Each scenario will have different solutions. Sometimes
you really just want a standard loop.

The benefit of learning the key concepts behind `Map`, `Filter`,
`ForEach` and `Reduce` is the ability to translate these styles and
idioms into other languages that may have the same functionality just
behind a different interface.

#### Map

Also known as Projection. Convert the array into a new array based on
the callback provided.

<script src="https://gist.github.com/Finglas/76da9beecc3f482daf20.js"></script>
#### Filter

Filter the array based on the callback if the result is true. In the
same manner as Map, the non functional version of this code is an
extremely common pattern so the functional version really shines here.

<script src="https://gist.github.com/Finglas/1347cd4e6b5fb318429c.js"></script>
#### ForEach

Invokes the callback for each member of the array. This is another very
common pattern that really benefits from the functional form.

<script src="https://gist.github.com/Finglas/cd49450677bd2583dffe.js"></script>
#### Reduce

Converts the array into a single value by taking the current index and
the next index as parameters to be applied.

<script src="https://gist.github.com/Finglas/41ebbc74a83232227db8.js"></script>
</p>

