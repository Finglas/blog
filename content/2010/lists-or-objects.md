Title: Lists or Objects
Date: 2010-12-01
Author: Shaun Finglas
Tags: code-quality, programming
Slug: 2010/12/lists-or-objects

> "Our rule of thumb is that we try to limit passing around types with
> generics (the types closed in angle brackets). Particularly when
> applied to collections, we view it as a form of duplication. It's a
> hint that there's a domain concept that should be extracted into a
> type." [[Growing Object-Oriented Software, Guided by
> Tests](http://www.growing-object-oriented-software.com/) - Steve
> Freeman, Nat Pryce, page 136)]

### Example

Not ideal - business logic will leak.

<script src="https://gist.github.com/Finglas/24ed5ead118ea8e2730c.js"></script>
Better - quotes are now encapsulated.

<script src="https://gist.github.com/Finglas/ed5e69d1e10925e7a4dd.js"></script>
### Why?

The benefit of the second approach is that you begin to force the
collection to do the work. Consider a collection of quotes - using the
first approach a developers' typical instinct would be to loop over the
list and check each quote until the lowest quote was found. You could
argue that this in turn violates the '[Tell Don't
Ask](http://www.pragprog.com/articles/tell-dont-ask)' principle because
very quickly you can find yourself digging down into objects. We would
not do this with standalone objects, so collections should not be any
different. Yet as developers we often avoid creating objects to
encapsulate collections, despite this principle being taught in the
early chapters of any OO programming beginners book.

Another key point of encapsulating collections is that you reduce
duplication. If another part of the application needs to perform a check
for the lowest quote, you'd end up either duplicating the code to loop
over the quotes, or creating a helper method to do the actual
processing. Using the collection means such features are only a method
call away at all times.

In a recent [code
kata](http://codekata.com/kata/kata09-back-to-the-checkout/) as well as
a current set of work, we are applying some of the above concepts and
finding a dramatic increase in the quality of our code. Those of you may
have noticed that the above implementation inherits from a standard
list, therefore it is indeed possible to still violate encapsulation and
dig through the collection yourself. There are pros and cons to this
approach, one benefit is all of the out of the box functionality you get
for free - the ability to loop over the quotes (for displaying say) and
return a count for example. The downside being developers can treat
these collections as if they were a list.

In C\# it is possible to use
[indexers](http://msdn.microsoft.com/en-us/library/aa288465%28v=vs.71%29.aspx)or
interfaces to improve the above implementation, though we tend to agree
that it's up to the developers to do the "right" thing - in other words,
not dive down into the collection. Interesting this very topic has been
[discussed on the excellent
StackOverflow](http://stackoverflow.com/questions/21715/listbusinessobject-or-businessobjectcollection)
- I and others will sure agree that the answer(s) provided are well off
the mark. Encapsulate your public collections - do not treat them as
primitives!