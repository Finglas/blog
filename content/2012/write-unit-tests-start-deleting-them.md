Title: Write Unit Tests? Start deleting them
Date: 2012-01-01
Author: Shaun Finglas
Tags: programming, tdd, unit-testing
Slug: 2012/01/write-unit-tests-start-deleting-them

A recent [blog post by Steve
Klabnik](http://blog.steveklabnik.com/posts/2011-09-22-extracting-domain-models-a-practical-example)
concluded with a statement about tossing unit tests if you have end to
end tests covering the code in question.

> Don't be afraid to change the tests! As soon as you've verified that
> you've transcribed the code correctly, don't be afraid to just nuke
> things and start again. Especially if you have integration level tests
> that confirm that your features actually work, your unit tests are
> expendable. If they're not useful, kill them!

A few people on Twitter found this odd, and I'd have included myself in
this statement a while back.

> [@isaacsanders](https://twitter.com/isaacsanders)
> [@avdi](https://twitter.com/avdi) seeing
> [@KentBeck](https://twitter.com/KentBeck) delete unit tests during his
> screencasts changed my TDD process forever.
>
> — Shaun Finglas (@F1nglas) [January 21,
> 2012](https://twitter.com/F1nglas/statuses/160776765353111552)

<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
[Kent Beck's TDD
screencasts](http://pragprog.com/screencasts/v-kbtdd/test-driven-development)
changed my view on deleting unit tests however. During the later videos,
he actually deleted some tests. Pretty much all TDD resources don't
really mention this. One of the key points beginners learn is that if
you break any tests, you've introduced a regression. This is not always
the case. If you follow the rule of never deleting ANY tests you
encounter you are going to be stuck with someone else's implementation
forever. Likewise unit tests are there to drive design, not enforce how
something works. I remember discussing deleting unit tests with my work
colleagues and finding Kent's videos pretty shocking at the time. I mean
deleting unit tests!?

The more I do TDD, the less this statement becomes so jarring. For
example.

<script src="https://gist.github.com/Finglas/217feb75bc8facf38534.js"></script>
Consider a test for the above behavior, such as we get the result back
in a particular state. Pretend the logic is rather simple, and it does
not warrant a separate object. Any other developer should be free to
come along and change the internals of this method. As long as we get a
result back in the correct state, the test should be valid. The test
should not care that we are using strings, lists or whatever internally.

Occasionally I find tests like this hard to pass. In other words, I feel
like the logic is correct yet the test fails. Maybe I'm using a new
language feature, or a language feature that seems to be not working as
I expected. If so I'll break out a new unit test that tests the
implementation. Such tests are often refereed to as [learning
tests](http://blog.thecodewhisperer.com/2011/12/14/when-to-write-learning-tests/).
Here with a smaller focus I often become aware of what I'm doing wrong.
Following Kent Becks example, I ditch the test after and move on.

I feel this sums up my feelings nicely.

> [@elliottcable](https://twitter.com/ELLIOTTCABLE)
> [@F1nglas](https://twitter.com/F1nglas)
> [@isaacsanders](https://twitter.com/isaacsanders)
> [@kentbeck](https://twitter.com/KentBeck) let them \[tests\] guide you
> to a design but don't let them hold you to a design.
>
> — Avdi Grimm (@avdi) [January 21,
> 2012](https://twitter.com/avdi/statuses/160780747827974145)

<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
I and others are not saying bin every unit test you have that is covered
by end to end tests. Unit tests are great, you can run hundreds in a
matter of seconds. They have their place as part of the development
process, but do not find yourself working against them. However I am
saying you should delete any test which relies on implementation
details. I am saying bin any test which does not make sense. I am also
saying bin tests as part of a refactoring session as long as you have
test coverage higher up. If you don't have test coverage such as
acceptance tests, you cannot be sure you have not broke anything after
the refactor.