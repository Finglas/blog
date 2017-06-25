Title: Singleton's and the Singleton Lifestyle
Date: 2016-04-01
Author: Shaun Finglas
Tags: programming, tutorial
Slug: 2016/03/singletons-and-singleton-lifestyle

[The death of testability and the lack of
isolation](http://misko.hevery.com/2008/12/15/static-methods-are-death-to-testability/)
make the singleton pattern a relic of times gone by. Rarely have I had a
real need to code a singleton since my first year of university. Most
decisions to use a singleton boil down to scoping issues.

#### Singleton

Assume a game requires a single instance of a rendering component. In
this example configuring and initialising the renderer may be expensive.
We only want to do this once.

<script src="https://gist.github.com/Finglas/931913cda1df6d3a5eb2.js"></script>
While this singleton renderer solves the problem of instantiating more
than once it suffers from the fact there is only ever one instance. If
we want multiple renderers such as a console debugger we are out of
luck. Testability is also lost. If we wish to exercise the Game, we need
to provide and use a real rendering component.

#### Static Classes

Or class instances give you the same advantages and disadvantages of
singletons. You only have one instance and you can access it easily. One
big difference is that unlike singletons you cannot provide static
instances as arguments. In practice this is rarely a problem given you
have easy access to the instance anyway. You should treat static classes
as suspiciously as singletons. However static classes are not bad. [They
do have uses](https://blog.shaunfinglas.co.uk/2015/07/static-code.html).

<script src="https://gist.github.com/Finglas/1ad58d37ba4d4d55a01b.js"></script>
The renderer is now a static class. The same disadvantage as the
singleton remains. We are always stuck with a single instance.

#### Singleton Lifestyle

When using DI you need to consider lifestyle. Singleton lifestyle is one
of the most useful. Do not be confused with the Singleton pattern.
Despite the name, singleton lifestyle is purely a scoping issue.

<script src="https://gist.github.com/Finglas/457a3b37b2c9cb16e960.js"></script>
By adjusting the scoping of the renderer, the game can now be provided
with a single instance. Any component from the game down is unaware of
this fact, they simple interact with a rendering component. If we were
to provide a composite of rendering components the game would be
unaware. This change of scope provides the benefits of a singleton. One
area that has been lost is the lazy initialisation of the renderer which
may or may not be an issue.

DI does not solve all problems however. [Sometimes dependencies are
global](https://blog.shaunfinglas.co.uk/2016/04/dependency-injection-for-common-global.html).
The likes of date/time or logging spring to mind. In these cases
[alternative solutions
exist](https://blog.shaunfinglas.co.uk/2016/04/dependency-injection-for-common-global.html).