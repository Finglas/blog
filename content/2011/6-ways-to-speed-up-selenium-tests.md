Title: 6 Ways to Speed Up Selenium Tests
Date: 2011-12-01
Author: Shaun Finglas
Tags: tutorial, testing
Slug: 2011/12/6-ways-to-speed-up-selenium-tests

[Having finally achieved more stable end to end
tests](http://blog.shaunfinglas.co.uk/2011/12/how-to-achieve-more-stable-end-to-end.html)
via Selenium, we figured it would be worth while sharing how we achieved
this. The following are six steps we've found that you can do to make
Selenium tests more stable.

1.  Turn off automatic updates for your browser/plugins
2.  Set your IIS (or equivalent) app timeouts to zero
3.  Create a base Selenium Fixture for use in your tests
4.  Update to the latest version of Selenium
5.  Warm up your apps prior to testing
6.  Ditch Selenium - test at the API level

Turning off automatic updates seems like a no brainer, but after a fresh
install we forgot to do this once and spent some time figuring out why
Firefox would not load on the CI server. It turns out that the "You've
just updated" window was blocking the test from continuing as it had
stole focus.

The second point is with regards caching and the general responsiveness
of your application. We have a few applications that take about thirty
seconds to fully warm up due to the huge data set they rely on. If we
can build this cache once, then store it for as long as possible,
subsequent hits to the app should be instant. In other words, we try to
mirror our live environment as much as possible.

Our custom test fixture attribute enables the ability to modify all
Selenium tests in one go. We found that from 3am to 5am our databases
undergo maintenance, therefore we do not run our regression tests during
this time. All this took was one change within the attribute to apply to
all tests. For example:

<script src="https://gist.github.com/Finglas/a23514ff0aecd9e496a6.js"></script>
We simply inherit from [NUnit's
TestFixtureAttribute](http://www.nunit.org/index.php?p=testFixture&r=2.5.10)
and use this custom attribute rather than the standard TestFixture
attribute. The inheritance is required to ensure that third party tools
such as test runners still work as expected.

Previously we were using Selenium 1.x with Sauce RC. Having ditched this
and [upgraded to Selenium
2.x](http://seleniumhq.org/docs/appendix_migrating_from_rc_to_webdriver.html#migrating-to-webdriver-reference)
we've been able to update our browsers to the latest versions, in turn
this allows improved speed and stability when running the tests.

On our local development machines the application you are working on is
often in memory, meaning subsequent hits should be much faster after all
dependencies are loaded and cached. The issue we discovered on our CI
server was that after a fresh build of the whole codebase, the initial
hits to the applications would be very slow. To combat this we added a
warm up step to our build. Just before the tests are run we would
perform a HTTP GET to invoke our applications start up processes. This
added somewhere in the region of thirty seconds to the build, but the
increase in stability is staggering. No longer will Selenium report
timeouts.

Finally the fastest end to end tests come from not using Selenium.
Ditching the browser completely and testing as high up in your API is
the quickest, and most stable solution. Combining this thinking, with a
handful of dumb Selenium tests that just check for the likes of 404s
seems to be the most optimal solution currently.

Having done these at some point over the past few months we're starting
to get to a more stable point with our Selenium tests. We'll be looking
to take this forward with future tests and hope to enjoy continued
stability.