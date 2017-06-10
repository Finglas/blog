Title: Production Code is Dirty
Date: 2015-08-01
Author: Shaun Finglas
Tags: retro, code-quality
Slug: 2015/08/production-code-is-dirty

Production code is dirty. *Dirty* may be the wrong word however. Complex
could be more suitable. Unlike code that is not yet in production, it is
weathered, proven, and full of edge cases including numerous bug fixes.
After some time this build up of additions can cause the code to be
considered dirty or legacy.

Greenfield development used to appeal so much more. Small classes. Small
methods. Few dependencies. Just simple, clean code. Except this is not
the case. Get into production and that clean code starts to weather.
You'll handle edge cases, fix bugs and stabilize the functionality. That
lovely, small, well factored application starts to accumulate dirt. The
new code smell wears off and you're back waiting for the next new
project so you can do it properly a second time around.

This does not have to be the case however. Long living software such as
operating systems, browsers and embedded systems are maintained and
extended well after they were created. Production code can be
complicated but still clean with redeemable qualities. In order to do
this you should write tests, [control
dependencies](http://blog.shaunfinglas.co.uk/2014/12/limit-amount-of-dependencies-you-use.html)
and get into production or the hands of the user as soon as possible.
This may seem an obvious solution but sadly many software projects fall
into this trap of dirty code after a handful of iterations.