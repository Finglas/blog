Title: Why are you not using Design by Contract?
Date: 2013-04-01
Author: Shaun Finglas
Tags: programming
Slug: 2013/04/why-are-you-not-using-design-by-contract

When learning to program I distinctly remember coming across the concept
of placing asserts within your code. Assert statements are primarily
used for "*things that cannot happen*", but in my early days I was too
focused on the stuff that was supposed to happen!

"*Defensive programming*" was also introduced. Principles such as "Never
trust the user" and "*80% of your code will be validation and
verification*" were highlighted. Despite these introductions many years
ago, the concept of asserts never stuck with me. Yet I program
defensively like there is no tomorrow.

The use of asserts can be extended into "[Design by
Contract](http://en.wikipedia.org/wiki/Design_by_contract)" or DBC. In
DBC the developer makes use of pre-conditions, post-conditions and
invariants. Some languages such as
[Effiel](http://www.eiffel.com/developers/design_by_contract.html) have
taken DBC as a core feature while other languages leave DBC up to
libraries.

One of my favourite programming books is the [Pragmatic
Programmer](http://pragprog.com/book/tpp/the-pragmatic-programmer).
Having stood up to many re-reads I always found myself intrigued by the
idea of DBC. Yet I never found myself following this interest through,
at least in a production environment.

Our team recently came across a bug in which part of the system was
using a component in a way which was deemed invalid. We had a suite of
tests to accompany this feature, but these tests were unable to
highlight the problem. When the object was sent across the wire, the
Javascript front end was firing a null reference across, this was out of
our control in the back end of the application. As the feature crossed a
boundary and spoke to another system defensive programming would have
been difficult. All we could do was error and inform the developer what
was wrong. Even without defensive programming, the system was currently
doing this anyway. We had little to gain.

Here I decided to experiment for the first time in my programming career
with code contracts. A contract was applied that said the collection
sent into the system must **not be null** or **empty**. If so, the
second system would blow up informing the developer what was wrong. This
contract was a very primitive example of a pre-condition - something
that must be true in order for the rest of the following code to
execute.

The benefit here came from just a few mere lines of code. Had we tried
to program defensively the second systems' code base would have suffered
for little gain. We would need to report the error, add error codes,
introduce exception handling and so on, all for a simple defect that
could be fixed immediately and potentially never occur again once the
developer integrating has configured the components correctly.

One important factor to consider with DBC is the contract violations
should **never be caught or handled**. Every single contract that is
violated is a bug. To stop the violation you need to fix the code that
is breaking the contract. Likewise contracts make little sense when
dealing with a public API. On the edge of the system you should presume
your users will make mistakes and "*do the wrong thing*", here you must
use defensive programming.

Since this day I've liberally applied code contracts whenever we cross
system boundaries or interact with the infrastructural aspects of our
code, e.g. database helpers. This has increased my confidence that the
system as a whole has been correctly "glued together". Another benefit
is several bugs have been thwarted thanks to the contracts as unlike
unit tests, contracts are always present when enabled, meaning missed
boundary conditions can easily be detected.

Hand in hand with our automated test suite, **code contracts make a
great companion**. Never alone will one suffice, but when used in
conjunction they can be extremely powerful. So the question is, why
aren't you using them?