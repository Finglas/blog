Title: Getters and Setters are Evil
Date: 2011-04-01
Author: Shaun Finglas
Tags: programming
Slug: 2011/04/getters-and-setters-are-evil

**Update**: There is a [new
version](https://blog.shaunfinglas.co.uk/2015/04/getters-and-setters-are-evil-redux.html)
of this post.

------------------------------------------------------------------------

I've been programming with OO languages since I was seventeen yet in the
last week I've had what is without doubt one of the biggest learning
experiences since I've started.

Numerous developers that I've worked with claimed that we aren't doing
OO properly. By we I mean software developers as a whole. Their argument
being having all your code defined in classes does not mean you are
obeying OO principles. By this they are often referring to the "[Tell
Don't Ask](http://pragprog.com/articles/tell-dont-ask)" principle. One
particular individual at Codeweavers introduced me to idea that getters
and setters are evil. While not true at face value, this statement is to
get you thinking about what you expose to the outside world. Consider
one of the founding pillars of OO programming; encapsulation.

Encapsulation states that an objects internal state should be just that,
internal. If we want a object to do something we should tell it. We
shouldn't care how its done either. The more I begin to think about what
I'm programming the more I begin to question myself. In a recent
programming session this was even more apparent. I stumbled across a
situation in which I wished to hide a objects internal state, and in
turn tell the object to do stuff. The problem I encountered was how the
hell do I display the state of this object to the user (say on a GUI)
without adding a load of properties (getters/setters).

Had I added the properties to the object I could ignore the methods on
the object and just dig down and fiddle the objects internal state from
the outside. This was not right, alarms bells were going off yet I was
unsure how to solve this. Thankfully some inspiration from a helpful
[StackOverflow
user](http://stackoverflow.com/questions/5573479/oo-encapsulation-object-conversion-to-get-to-innards)
and advice from a collegue pointed me in the right direction.

The solution was simple and can be summarised in the following pseudo
code:

<script src="https://gist.github.com/Finglas/c9e599dd3d133c60a6b2.js"></script>
A more encapsulated approach could be:

<script src="https://gist.github.com/Finglas/cf632d3c42c1951ff144.js"></script>
A business object should property free, or at least only able to be
updated from the outside world by asking it to do something. Its
internal state may be internal to the class itself, or there may be a
DTO passed in at construction it matters not. The Writer in this case is
an abstraction around some form of output. We could have a console
writer, HTML writer, Json writer and so on. By inverting the dependency
we can avoid adding properties to the business object. Any consumer of
this object must invoke the business object's methods - aka tell the
object to do stuff. There is no way of the outside world modifying this
objects internal state without abiding by the business rules. What's
nice about this revelation?

There are many examples of this pattern at Codeweavers, yet I was
unaware of the problem it was solving. By being burned by this issue
personally the reason for patterns such as the one detailed above become
much clearer and stand out. Whats better is when this problem crops up
again I'll be able to handle it.

Properties or accessors have their place. They are required for DTOs,
frameworks and certain language features, yet as with any tool their
usage should always be considered. Blindly adding properties to a
object, or worse, having the IDE auto generate accessors to an objects
state is a clear problem. The biggest lesson I've took away is that even
for input/output the use of accessors is not required. As usual the
Codeweavers saying of "*if it feels wrong, it probably is*" still holds
true and on that I'm off to try and write some proper OO code for the
first time in six years...