Title: Pulling the Plug on Date Time Parsing
Date: 2016-03-30 06:49
Author: Shaun Finglas
Tags: testing, programming, unit-testing
Slug: 2016/03/pulling-plug-on-date-time-parsing

Date/time logic is hard. Throw in time zones along with daylight saving
and it's even harder. Recently a suite of tests that had happily been
running for months started failing. There were no code changes and all
the tests were somehow related to date/time ranges.

Despite this the production code was functioning as expected. It turns
out the API was explicitly setting the locale to use `en-GB`. However
the suite of tests were not.

The fix was simple. Prior to the test fixtures executing, explicitly set
the locale. In order to test this assumption and see the tests pass, a
temporary change on the development machine was required.

The locale was set on the development machine to another region. In this
case setting to `en-US` was enough to cause the tests to fail. After the
code change the tests passed. Any locale can be used as long as the date
format differs.

This idea is pretty easy, and is very close to my technique of [pulling
the plug on automated
tests](https://blog.shaunfinglas.co.uk/2012/05/achieving-more-isolated-unit-testing.html).
The test suite can now be run on any machine, even those incorrectly
configured and we can be sure the tests will still pass.

Going forward for any date/time tests I will make an active decision to
temporarily change my regional settings. With more codebases utilizing
the cloud, relying on implicit configuration should be avoided where
possible. In fact I would bet a large sum of money that many codebases
out there would fail this temporary locale change. Give it a go - pull
the plug.