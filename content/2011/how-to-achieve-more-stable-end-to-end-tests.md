Title: How to Achieve More Stable End to End Tests
Date: 2011-12-01
Author: Shaun Finglas
Tags: tutorial, testing
Slug: 2011/12/how-to-achieve-more-stable-end-to-end

Recently myself and another colleague wrote an [acceptance
test](http://en.wikipedia.org/wiki/Acceptance_testing) for a feature
that had yet to be implemented. For this end to end test we used
[Selenium](http://seleniumhq.org/), after all we wanted to test the
whole feature so this made sense. Our test performed some simple user
input, performed a calculation and checked the response. The problem
with the test was it was very brittle. If the application had not
recently been used, the massive data set the application relied on would
not be cached.

To get around this we added a few
[Thread.Sleep()](http://msdn.microsoft.com/en-us/library/d00bd51t.aspx)
statements into the test. This worked rather well for the majority of
test runs, but sometimes these pauses were not long enough. On the other
hand sometimes the data was cached, meaning these sleeps would be
unnecessary. One resource which has recently done the rounds was
regarding useful [advice about using WaitForPageLoad() and
WaitForCondition()](http://www.bonitasoft.org/blog/tutorial/how-to-get-faster-selenium-test-cases-execution/).
WaitForCondition will only execute once a condition has been met, such
as a element becoming visible. This meant that for the times when the
dataset was in memory the test would be executed immediately, while the
times when the data was being loaded, the test would simply wait until
the test was ready to move on. This was a very simple, yet highly
effective tweak to our tests. The execution time went from roughly
thirty seconds, to just less than ten seconds in one case.

This was not the end of the battle to achieve more stable Selenium
tests. Some of our tests were still rather flaky. Some mornings we would
enter work, notice the red build and discover that the several failed
tests were down to Selenium timeouts. During the daytime however, we
rarely had these issues. In order to fix these problems I increased the
frequency of builds. The idea being the more we run our builds the more
chance we have of spotting the errors. After all, if something was to
fail at 2am, I am unlikely to care. 2pm however, and the team will be
all over it. By making the problem more visible, we would be forced to
fix the outstanding issues.

The aim was to make the tests as fast as possible, while maintaining
stability. One thing the excellent [Growing Object-Oriented Software
(Goos)](http://www.amazon.co.uk/Growing-Object-Oriented-Software-Guided-Signature/dp/0321503627)
touches on is the aspect of not needing to perform end to end testing at
the GUI all the time. The benefit of not touching the UI is huge. Your
tests are faster, they're more stable and a heck of lot easier to write.
The other nice benefit of testing from an API point of view, rather than
the browser is it forces you to decouple your app from the views. If
you're not writing [fat models and skinny
controllers](http://weblog.jamisbuck.org/2006/10/18/skinny-controller-fat-model),
you'll have adapt in order to test as much of your application as
possible without hitting the UI.

What about the remaining part of your feature that is not covered by the
application? I like to imagine this part as the tip of an iceberg. As
this area is small enough the actual UI testing you need should be
minimal. So here we can let Selenium do what it is good at. Click
things. Selenium is great at this. All you need to do at this level is
check for 404s, incorrect page titles and a few other mundane aspects of
the UI. There should be no need to check if your actual application is
correct at this level. For correctness, you should have a large suite of
fast, isolated, unit tests.

Another point to consider is how often your view actually changes, in
comparison to your actual underlying API. A designer should be free to
move things, rename content, add images and so forth without breaking
tests. As long as there is a calculate button somewhere on the page, and
said button takes you to a result page, who cares about everything else?
Likewise the code underneath can be consistently changing behind the
scenes, as long as the API remains constant, our tests should always be
valid.

*For the technical low down on some of the ways we are achieving more
stable end to end tests, check out [six tips to speed up Selenium
tests](6-ways-to-speed-up-selenium-tests.html).*