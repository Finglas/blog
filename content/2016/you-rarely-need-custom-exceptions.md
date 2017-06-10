Title: You Rarely Need Custom Exceptions
Date: 2016-05-01
Author: Shaun Finglas
Tags: programming, tutorial
Slug: 2016/05/you-rarely-need-custom-exceptions

Implementing custom exceptions usually gives a hint as to why you rarely
need custom implementations. They are often nothing more than sub
classes where the only difference is the type name and containing
message.

<script src="https://gist.github.com/Finglas/b7341379033d951aa88d2b7ed28aaba5.js"></script>
In this C\# example there is a lot of code for *nothing*. When checking
logs or handling bugs you will read the message and the stack trace. The
first line containing a bespoke name rarely matters. Within the code
throwing the exception very little context is gained from the type of
exception - instead most of the details will be present within the error
message.

Each custom exception you introduce adds overhead from source lines of
code (SLOC) to compilation and execution.

#### Alternative

Simply do not create custom exceptions except in the rarest of
occasions. Instead rely on the standard library of the language you are
using.

[Take Python as an example](https://youtu.be/o9pEzgHorH0) \[Video\].
\~200,000 lines of code yet only \~165 exceptions. This works out at
about one exception for \~1200 lines of code.

If battle hardened and widely used standard libraries need only a
fraction of the amount of custom exceptions, what makes your tiny CRUD
app so special that it needs a namespace dedicated to handfuls of
bespoke implementations?

#### Example

Rather than throwing NoBlogPostsFoundException use a
[HttpException](https://msdn.microsoft.com/en-us/library/system.web.httpexception%28v=vs.110%29.aspx)
with a useful message. Instead of BlogPostConfigurationException use
[ConfigurationErrorsException](https://msdn.microsoft.com/en-us/library/system.configuration.configurationerrorsexception%28v=vs.110%29.aspx).
Trying to add a comment to a post that is not published? Use an
[InvalidOperationException](https://msdn.microsoft.com/en-us/library/system.invalidoperationexception%28v=vs.110%29.aspx).

The downside to this suggestion is knowledge. You need to know what
exception to use and more importantly where to find it. Consulting
documentation or simple digging around will often yield what you need.
As a rule try and default to reusing an exception over creating a new
one.

The benefit of this approach is less code, and the removal of
placeholder classes where the only thing that differs is the message. To
ensure nothing is lost in communicating intent, care must be taken to
ensure the message is useful, concise and clear.

#### Custom Exceptions

There are two exceptions (see what I did there) to this rule.

1.  When you explicitly need to handle a certain scenario and you cannot
    allow other unhandled exceptions to trigger that code path. In this
    case a custom exception may be valid. As usual question whether an
    exception is necessary at all, it may be possible to control this
    with an explicit code path.
2.  When the exception has some form of behaviour. This tends to be
    common with frameworks where when an exception of type X changes the
    flow but also carries out some action such as building up an error
    response.

In these cases this behaviour belonging with the exception makes sense.
Generally most code bases treat exceptions equally. In other words any
exception triggers a failure path, meaning the type of the exception
does not matter in most cases.

#### Lessons

-   Reuse exceptions from the standard library, chances are there is one
    fit for the job already.
-   Only introduce custom exceptions if the scenario is exceptional and
    needs to be handled uniquely.
-   Put effort into ensuring the message of an exception is useful -
    messages and the stack trace are the most important elements.