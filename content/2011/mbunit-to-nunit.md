Title: MBUnit to NUnit
Date: 2011-03-01
Author: Shaun Finglas
Tags: testing, programming
Slug: 2011/03/mbunit-to-nunit

Over the last few weeks we've ported our tests from
[MBUnit](http://www.mbunit.com/) to [NUnit](http://www.nunit.org/). This
was done as after a quick spike it was seen that NUnit tests run almost
fifty percent quicker. For example our common projects' test time went
from around **40s** to around **20s** on average.

This whole process was no easy task. Initially our largest project was
converted by the whole team. We split into pairs/individuals and tackled
a test project each. Working in this manner we could commit after each
project, meaning at any one time the build was only fractionally broke,
rather than completely unbuildable. Previously we tried a big bang
approach but after several thousand errors, we quickly reverted. After
each commit the tests were gradually moved over. This took around an
hour or so, and therefore our allocated dojo/technical dojo time for
that week was used. For the remaining projects an ad-hoc approach was
taken. The first pairs to work on a project would be responsible for
porting the tests over. Thankfull our other projects bar one were fairly
straightforward to upgrade and were done as part of waste or kaizen.

Some of this process could be automated however things were not
completely smooth. For example converting the MBUnit namespace over was
achieved by project level find and replace. Other issues such as Asserts
being slightly different required a manual fix. One example being
asserting a exception is thrown. The MBUnit approach used attributes
while in NUnit it is more preferable to use *Assert.Throws*. The other
issue we faced was porting over the relevant build scripts and Cruise
Control configs. Again there was no easy way to do this. We had a fair
few CI fails when this was done, but when editing the xml build files
there is no real way to test what you've done without actual trying it!

Overall the whole episode was not as bad as I thought it would be. We
seem pretty stable at time of writing, and the tests are definitely
quicker to run locally. We still have slow tests, and as part of waste
we'll be looking into whether these slow tests are needed. One
interesting practice I've noticed over the upgrade is how many dodgy
tests we've removed. Tests such as *Assert.IsNotNull* after creating a
new object - the sort of tests everyone writes when starting TDD have
been removed. These legacy tests serve no purpose now, but were the key
starting point of the TDD introduction to Codeweavers several years ago.
Other tests which are covered else where or simply not needed were also
removed. The final issue we are aiming to improve is that of our
regression/acceptance tests, many of which are Selenium tests.

Would we recommend upgrading your test suite to the latest/next best
thing? Not unless you can prove with figures that it has an actual
benefit. We provided no value to the business by doing this, but by
hopefully taking one step to increase our feedback cycle we'll see the
benefit over time. If anything, we should be more likely to run our
tests. As for why MBUnit was slower? It features a lot of stuff we
simply don't need, while NUnit is more lightweight and just plain faster
for our use. We could perhaps speed the tests even more by writing our
own test runner, but the likes of Visual Studio integration are a must
therefore this is no easy task.

One interesting point to conclude was that during this process there was
talk about wrapping NUnit within a Codeweavers test framework,
essentially meaning we could switch test frameworks whenever. Is this
overkill for most projects? Most likely, but it was something to
consider especially for large applications. As who knows, maybe there
will be an even faster framework out there that we can upgrade to again,
next year...