Title: Log Everything
Date: 2012-01-01
Author: Shaun Finglas
Tags: programming
Slug: 2012/01/log-everything

*This post was originally conceived back in mid 2011, starting a new
project made me think back to this event, hence the post.*

Any developer worth their salt will know what logging is. You could
argue there are two types of logging, either developer logging or
auditing. Developer logging would be what we log when something goes
wrong. Using the results of this logging we can track down what went
wrong, and put fixes in place to stop this event from occurring again.
If this logging fails, or logs the incorrect thing it is not the end of
the world. Due to this, I generally do not care for testing such
scenarios. The code should behave the same with our without this
logging.

Auditing would come under logging which as part of the application needs
to be carried out at all times. Consider visiting a cash machine. When
withdrawing fifty pounds, you want to make sure your bank logs this in
case anything goes wrong. This sort of logging is crucial, and must work
and must log the correct data. This is considered a feature, therefore
this should be tested as it is part of the behavior of the application.

When I think back to my first few years of programming my code was
littered with logging. In the early days after each statement, variable
and function I would print out what happened, along with any errors that
happened. In fact I'd say that everyone starts out like this. The
strange thing is as we get better, the logging becomes less and less.
Rather than the first class citizen we relied on in the early days,
logging is seen as boring. The problem with treating logging code as a
second class citizen is that when things go wrong, it can be very
difficult or near impossible to track down what has happened. When you
realise you need logging, its often too late. You will need to redeploy
the application and wait for the problem to expose itself again.

Back in 2011 we had a difficult problem to track down. The dreaded
"`OutOfMemoryException`". Being the cocky developers we were, we decided
to add the logging last. After all, it was there for when things went
wrong. We never planned things would go wrong, after all it "*worked on
my machine*". After redeploying the application with logging we managed
to track down roughly what was going wrong, and in turn began to resolve
the problem. Had we added this logging initially, we could have resolved
this problem in half the time.

The lesson I learned here was simple. Any time you have an error, log
it. If the logging is not in place, we add it. Creating a new
application? In the first iteration(s) make sure some form of logging is
in place. I believe by following this simple rule any future issues can
be handled easier. Logging should be a first class citizen regardless of
purpose.