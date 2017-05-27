Title: FirstOrDefault in LINQ
Date: 2015-06-23 20:54
Author: Shaun Finglas
Tags: null, http://schemas.google.com/blogger/2008/kind#post, programming, c#, linq
Slug: firstordefault-in-linq

Explicit null checking is a code smell in most cases. It should be
limited where possible, or pushed to the edge of the system. A common
anti pattern I've noticed is the incorrect use of `First()` in LINQ,
which I have used myself on many occasions in this manner.

Assuming a collection of items that you wish to query, the incorrect
approach is to explicitly check for a null return value and act
accordingly.

<script src="https://gist.github.com/Finglas/0ab1ace9e1d582047485.js"></script>
The use of `FirstOrDefault()` is redundant because no default is
actually set. The default value of a reference type would be null.
Meaning the explicit null checked is required. We could use `First()`
alone, but this will throw an exception if there are no elements to
query against.

A better solution is to set the default. As long as our initial query is
not operating on a null reference this is safe. Here the explicit null
check is gone. We have replaced it with a more functional solution which
is after all what LINQ is based upon. While both are equivalent, the
second example is much cleaner as well as being open to further chained
statements.

<script src="https://gist.github.com/Finglas/f8622201f6cd44af138d.js"></script>
`First()` relies on one or more items being in the sequence. When you
are only ever dealing with one result `Single()` is more appropriate.
This method will throw an exception if more than one result is found,
acting as a form of assertion. Like `First()`, `Single()` offers
`SingleOrDefault()` which would work in the same manner as above.

</p>

