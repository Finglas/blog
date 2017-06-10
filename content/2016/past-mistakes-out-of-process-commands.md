Title: Past Mistakes - Out of Process Commands
Date: 2016-05-01
Author: Shaun Finglas
Tags: retro, past-mistakes-series
Slug: 2016/05/past-mistakes-out-of-process-commands

Some of the best lessons you can learn are from failure. I figured a
series on mistakes I've made in the past would highlight where I went
wrong and more importantly what to remember going forward. These real
life examples vary from my early days of programming all the way up
until present day.

------------------------------------------------------------------------

I once wrote a feature that sent email to users on their behalf. On
localhost this was fine. Fast, stable and good enough to get the job
done.

Despite early successes, under load in a live environment, things were
different. Sometimes the process would out right fail, requiring the
user to retry. Other times it would be slow to process. This meant the
users browser would hang while the email was being sent.

It was hard to replicate these problems. The actual code itself was
pretty simple, there was nothing to optimize it seemed.

#### Mistakes

The core mistake was performing an operation out of process from within
the life cycle of a HTTP request.

When sending the email was slow, the HTTP response was slow as the
thread was blocked. This was blindingly obvious after the fact.

Frustratingly actually demonstrating or testing this feature was hard.
Locally the server was nearby so latency was less. This started to
introduce other red herrings such as was the server misconfigured?

#### What to do Instead

After the user has requested an email, record this fact and simply
display a success message. Do this as quickly and simply as possible.
While the message states an email has been sent this is not strictly
true.

Instead the act of requesting the email is recorded. Ideally via a
message queue or other durable storage solution. A separate service then
monitors this queue and periodically sends out emails.

Users will not care if an email lands a few seconds or minutes after the
fact. Additionally if anything goes wrong during this process no data is
lost. The user will get their email eventually. Most e-commerce sites
work in this exact manner.

This approach works great when commands from users cannot and should not
fail. Examples such as processing payments or key user interactions
would be excellent candidates.

Unfortunately not all out of process requests can be avoided. HTTP
queries to retrieve data being one example. This cannot be faked. In
these cases minimize the number and rely on other techniques, such as
HTTP's excellent caching policies to reduce the affect on the system.

#### Lessons

-   Never perform commands that cannot fail out of process from within
    the same HTTP transaction.
-   Fear all out of process calls - they are costly, prone to failure
    and can cause chaos with your systems performance. Reduce and
    replace where possible.
-   When commands that should not fail are required, use a message queue
    to record the command prior to processing them.
-   Rely on HTTP caching policies to reduce the effect of queries that
    cannot be avoided.