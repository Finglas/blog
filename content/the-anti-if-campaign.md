Title: The Anti If Campaign
Date: 2015-04-23 18:53
Author: Shaun Finglas
Tags: best-practices, http://schemas.google.com/blogger/2008/kind#post, programming
Slug: the-anti-if-campaign

Firstly if you are unaware of what the [Anti If
Campaign](http://www.antiifcampaign.com/) is, I advise you to take look
before coming back. My first impression a few years ago was the site
must have been some sort of spoof. Programming without "if" statements,
this was crazy nonsense. After all the "if" statement is one of the core
constructs of any language. If you look deeper however the campaign is
not advocating the abolition of "if" statements, it is simply
encouraging cleaner code by removing the likes of type checking and
control coupling. This can be achieved by the use of Polymorphism and
abiding by the [Single Responsibility
Principle](http://en.wikipedia.org/wiki/Single_responsibility_principle)
(SRP).

The Anti If Campaign is relevant as I have recently had first hand
experience of what the supporters are campaigning against. I was working
on one of our greenfield projects where I had violated SRP for an easy
win. We had a class which would look up a quote based on some input
criteria. I allowed this input to control how the lookup was performed.
In some scenarios the input would be in a different form, meaning the
lookup would need to be carried out in a different manner. An "if" check
was introduced to handle this logic. In pseudo code:

<script src="https://gist.github.com/Finglas/54c9876cd1510228b36e.js"></script>
The code in question had supporting methods for both paths.

Fast forward a few months and something terrible had happened. Like a
plague, this simple conditional I had introduced was spreading. Code
that was executed much later on was beginning to perform the same
conditional check! At the same time I discovered this problem, I was
asked to perform a trivial change as the requirements had evolved. What
should have been a five minute job, turned into a few hours of paying
back technical debt.

The fix was well overdue at this point. I had to push the conditional
statements as high as I could. [The closer they were to the edge of the
system the
better](http://silkandspinach.net/2011/09/19/conditionals-on-the-edge/).
The by product of this refactor is that the code is a lot clearer now.
Each class and method did just one thing, and they did it well. It
turned out I was actually able to push the conditional statement so far
up that it effectively disappeared into the routing of the system. It
was up to the caller to "*do the right thing*".

After the refactor:

<script src="https://gist.github.com/Finglas/e53f5a01135b8c1f7c1e.js"></script>
As each part of the code complies with SRP, I know exactly where to go
if there is a problem. For example, if we have any problems with the
retrieval of new quotes, I can easily debug and fix the issue. Likewise
if we wish to extend the lookup of existing quotes, I can confidently
change the code without the fear of breaking the retrieval of new
quotes. The other side effect is that I can easily reason about and test
the code in question.

</p>

