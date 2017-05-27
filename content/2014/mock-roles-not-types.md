Title: Mock Roles not Types
Date: 2014-08-17 15:15
Author: Shaun Finglas
Tags: testing, http://schemas.google.com/blogger/2008/kind#post, programming, mocking
Slug: mock-roles-not-types

> "if it feels wrong, it probably is" - numerous Codeweavers' developers

The framework we use at Codeweavers is the excellent
[Moq](http://code.google.com/p/moq/), therefore when something is
difficult to mock we are forced by the framework to write an adapter. We
use an interface for testing, then create a concrete type which simply
invokes the hard to test code such as static code, third party libraries
and resources that are expensive to set up. There are some ways ways in
C\# to get around this, but they involve black magic and should be
avoided at all costs unless you are deeply entangled in legacy code. A
refactoring would be preferable over hard to test code.

The process of writing an
[adapter](http://en.wikipedia.org/wiki/Adapter_pattern) around hard to
test code is a standard practice, we do it all the time as we are forced
to by the unit testing framework. Some frameworks we use at Codeweavers
such as [[ASP.NET
MVC](http://asp.net/mvc)]{style="text-decoration:underline;"}are
designed with testability in mind, so unlike scenarios where you cannot
test code easily, the MVC framework makes it possible. In a recent
feature myself and a fellow colleague wrote some code within a
controller which relied on some of the controllers' (the MVC framework)
internals.

Rather than abstracting this into a class which we inject to make
testing easier we went the route of setting up a complex, messy and
tedious routing test fixture. Why you ask? Maybe it was the fact it was
possible to test. Had it been straight up impossible or much harder,
then introducing an abstraction would have been the obvious solution.
The code in question was a small method that depending on the somewhat
complex and unique routing values performed on a certain response. Fast
forward a week later and the feature is to be expanded.

We were back were we started, the new feature needed more setup that
relied on the framework, and in turn once this production code was
changed, the old test fixture would need updating. The very thought of
this made me feel tired, fed up and generally annoyed that the test code
was harder to write than the actual production code! While the code did
not feel right, the actual process was a by the book approach, so it
must have been right. Taking a step back myself and my new pairing
partner decided for a different approach. Lets abstract the controller
internals we need and inject this into the controller. In turn our code
would read better and the tests would be easy to construct.

Having made this refactoring the tests were still green. The refactoring
was a great success. Now the test fixture set up consisted of a few
simple lines. All the complex framework specific nonsense had
disappeared. Getting to this stage took a bit of thought with regards
the implementation, but we got there non the less. Having made this
change, we wrote the next tests with such ease and joy it actually felt
fun, enjoyable and completely stress free. Just how programming should
be.

For the production code, as the framework is test friendly we had some
unit tests around the concrete object used in production. For scenarios
where this is not possible, a high level acceptance test to ensure
things are wired up correctly would suffice. Either way we should always
be confident when using code we do not own that it is correct, providing
we use it correctly. After all, this will be heavily tested by the third
party or so we hope. Manual testing will catch any integration issues
with third party code with any luck.

The whole process was staggering, I was blown away by my ignorance. I
knew the best practices, yet I chose [to depend on concrete
implementations rather than
abstractions](http://butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod).
After this session the whole theory behind [mocking roles and not
types](http://www.mockobjects.com/files/mockrolesnotobjects.pdf) \[pdf\]
became so much clearer. This is yet one more revelation to add to the
list. Every time I write `Mock<name>`, stop and think. Do I own the
type? If not then maybe there is an abstraction waiting to escape, after
all it will save a lot of pain.

</p>

