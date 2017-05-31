Title: The Problem with Auto Updating Browsers
Date: 2015-05-02 15:28
Author: Shaun Finglas
Tags: selenium, testing, http://schemas.google.com/blogger/2008/kind#post, browsers
Slug: the-problem-with-auto-updating-browsers

At the time of writing the latest version of Firefox (version 13) has
just been released. Bear in mind that a week ago I updated our Selenium
bindings so that we could use Firefox 9+ for running our browser tests.

The latest release is another great release for the Firefox team, except
there is software out there will be broken. The software in question I'm
talking about is any code that uses [Selenium
2.22.0](http://seleniumhq.org/download/) that was released 2012-05-29.
It turns out the bindings only work for Firefox 12 or less.

For whatever reason any tests that used Selenium this morning just
stopped working for us - [and
others](http://groups.google.com/group/selenium-users/browse_thread/thread/83a7895693364c3a).
The tests in question caused the runner to hang as no window could be
opened. I'm not sure what causes this, as the browser is essentially the
same to the end user, bar some new features. Not being a Selenium
developer I cannot comment how or why this has happened, nor can I
suggest the Selenium team should be version agnostic.

Our solution in the end was simple. Turn off the auto updating and
downgrade the browser. [I've blogged about this in the
past](http://blog.shaunfinglas.co.uk/2011/12/how-to-achieve-more-stable-end-to-end.html),
but since Firefox 10 - the team are adopting a "silent" update process.
This is great for end users. Imagine the countless man hours saved if
IE6 had shipped with an auto update feature? The problem now seems to be
in the hands of developers.

Another attempt to make this problem more obvious has been to add a
check prior to our tests running to ensure that it can open a window. If
this fails or hangs, we display a useful error message indicating that
the browser in question is not compatible. This is due to the fact that
it is not immediately obvious what the problem is. More confusion occurs
when some machines will execute the tests with no problems at all.

Tools -&gt; Options -&gt; Advanced -&gt; Update Tab

So if you use Selenium and Firefox - ditch the auto updating. Manually
update your bindings and check compatability for now...

</p>

