Title: Dependency Injection for Common Global Dependencies
Date: 2016-04-13 07:09
Author: Shaun Finglas
Tags: programming, tutorial
Slug: 2016/04/dependency-injection-for-common-global

The use of [singletons can often be replaced by simply adjusting scoping
of
objects](https://blog.shaunfinglas.co.uk/2016/03/singletons-and-singleton-lifestyle.html).
The vast majority of dependencies fit this pattern, with a few
exceptions such as DateTime instances, or logging.

Sometimes you just need these dependencies everywhere. You can find
yourself passing these dependencies down into the deep depths of your
code base. Such changes are often dangerous, time consuming and
undesirable.

#### DateTime

For a while the use of some date/time abstraction was my default
approach to handling dates and times. This fake clock or calendar
instance when combined with DI at the lowest level does actually work.
However if we stop and think about the abstraction it is clearly
unnecessary in many cases. Unless your domain is dealing with date and
times explicitly, you don't really need an abstraction. In other words,
other than the system where the code is running when or why would you
provide a different implementation?

The approach taken as part of the [example within the Dependency
Elimination
Principle](https://blog.shaunfinglas.co.uk/2015/03/dependency-elimination-principle.html)
is my current solution to date/times and DI. This is still dependency
injection, except the value is provided, not the method of obtaining the
value. This is essentially one of the benefits of functional
programming.

#### Logging

All systems need some form of logging. Commonly either the standard
library or a highly rated logging framework is used. The general advice
has been to use the logging component directly, rather than providing
your own abstraction. Most frameworks already provide interfaces or base
classes that make this easy to achieve.

Even so logging suffers the same issue as date/times when it comes to
DI. You often need the logging component everywhere, whether it is
simply to pass on to other services.

Logging and DI generally do not go well together. Instead simple use the
logging instance directly. A good logging framework would be fast, so
any automated tests will not notice the difference. Likewise whether
logging is configured or not, this should not cause tests to fail. In
summary, not every object has to be provided via dependency injection.
Loggers being a prime example.

Due to this directly using a logging instance is the preferred approach.
Do not rely on DI. However [semantic or structured
logging](https://msdn.microsoft.com/en-us/library/dn440729%28v=pandp.60%29.aspx)
does change this suggestion as the use of a domain explicit interface
can provide benefits. Semantic logging will be expanded in a future
post.

#### Others

Date/Time and Logging are the two most common global dependencies. The
majority of all other dependencies can and probably should be satisfied
by traditional DI where possible. As always each dependency should be
validated prior to introduction. It may be possible to either [eliminate
or replace the component in
question](https://blog.shaunfinglas.co.uk/2015/03/dependency-elimination-principle.html).