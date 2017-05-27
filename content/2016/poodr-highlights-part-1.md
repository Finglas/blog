Title: POODR Highlights Part 1
Date: 2016-10-27 07:07
Author: Shaun Finglas
Tags: highlight, series, http://schemas.google.com/blogger/2008/kind#post, code
Slug: poodr-highlights-part-1

[Practical Object-Oriented Design in Ruby](http://www.poodr.com/) or
POODR is clearly a book about Ruby development, however the odd aspect
is much of the concepts apply to other languages. In fact I've taken
these ideas and used them both before and after reading the book in
other dynamic languages and even static languages such as C\#. In
summary the book is well worth a read, even if you don't do Ruby
development full-time.

A few of the highlights for me will be spread out across the following
posts.

### Dependencies

The author takes a firm stance on dependencies. Anything that cannot be
controlled by the class itself should be protected from change. In other
words a message sent to `self/this` is preferred than directly
interacting with a dependency.

<script src="https://gist.github.com/Finglas/086ca41a77d1623a999a9dcf8ddc97ac.js"></script>
I've followed this pattern in the past, but the seeing the
justifications for the benefit of this has made me realise the
importance of such a practice. In the first example the publish method
directly knows about the twitter feed it must interact with. In the
second example the class sends a message to itself, while the class
internally will still know how to interact with the dependency this is
hidden. The private method has this responsibility.

With a single use you could argue there is not much difference, but the
`PostPublished` method is a nice seam for both testing and changes. We
could easily add assertions or make changes within the `PostPublished`
method without fear of changing anything else. Finally if the
`PostPublished` method is used in multiple places this abstraction pays
for itself straight away.

### Arguments

Arguments are another key area that can change. Just like dependencies,
the book focuses on the idea that making small changes up front can lead
to flexible code that can handle change in the future. While you could
argue that the order of arguments changing in the future may never
happen, using named arguments has a great side effect on readability.

In static languages your IDE will most likely have a automated method of
adding these in, so the C\# example below can easily add named arguments
with the press of a keyboard shortcut.

<script src="https://gist.github.com/Finglas/8787b97afbfef6c4835ee3b3138f1025.js"></script>
Named arguments provide increased readability with very little effort.
Tests often benefit from the use of named arguments as you can remove
the need for temporary variables, and instead in-line them to the
location of use. While the third example is more “wordy”, they can
safely be re-ordered without fear of compilation or runtime errors.

### Lessons

-   Wrap dependencies even if they are only used once. A message to
    `self/this` is preferred. Easier to change and provides seams for
    future work.
-   Use named arguments for improved readability and the ability to
    reduce temporary variables. Named variables can be dropped if there
    is only one argument or the variable is well named.

</p>

