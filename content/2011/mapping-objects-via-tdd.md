Title: Mapping Objects via TDD
Date: 2011-06-01
Author: Shaun Finglas
Tags: programming
Slug: 2011/06/mapping-objects-via-tdd

### Why we map?

Many times at Codeweavers we often have tasks which involve mapping
between various objects. It is no secret that I dislike such tasks. The
reason we map between objects though is actually a good thing as pointed
out by several developers. Mapping means our components are less
coupled. For example, we can write one feature and then simply map
different web services to use this feature. If we chose not to map to a
common object we would need to re-implement this functionality for each
service. Therefore not only do we decouple our code, but our codebase is
much [DRYer](http://en.wikipedia.org/wiki/Don%27t_repeat_yourself).

### What ways do we do it?

-   One approach is a test per property. One developer will write a
    failing test for a property (accessor), while the other developer
    writes the code to make this test pass. During this process the
    keyboard flicks back between each developer very rapidly, in fact
    most of the time when writing a property per test is spent sliding
    the keyboard to the other developer.

-   Another approach we have tried on occasion is to have one developer
    write one test for the whole class, while the second developer will
    write the mapping code to make this test pass. We may or may not
    split each assert into separate tests. TDD purists will find this
    odd, as it does indeed go against our normal work flow. On the other
    hand, the reason we do this is the tests and code are virtually
    identical; therefore it is quicker. The downside with this "big bang
    approach" is the developer writing the code to make the tests pass
    may miss something. If this happens, finding out what is wrong is
    much harder as the code was written in one big go.

-   The final approach we have attempted is to not test mapping code,
    after all what could go wrong? It turns out a lot. Mapping often
    defaults values to specific values, or is subtly different to the
    source object. Much time can be wasted when all your tests are
    passing, yet the application is falling over because some data is
    being set incorrectly.

### What is wrong with this approach?

My main gripes with mapping, albeit an integral part of our development
process is how boring it is. Not to mention how slow mapping tests can
be to write. After an hour to have successfully mapped an object you
feel exhausted, not because of how challenging the process was, but how
tedious the task was. I also cannot seem to shake the fact that after
this process is complete you feel as if you are exactly the same
distance away from your goal as you were before. For someone on the
outside looking in, no "real" work has been done.

### Enter AutoMapper

[AutoMapper](http://automapper.codeplex.com/)is a project I wish I had
created myself. AutoMapper as the name suggests will map objects to
other objects on your behalf. For example, imagine a view model that
needs mapping from a bog standard DTO. Providing the objects names
follow the same conventions, auto mapper will automatically map these
values for you. Currently we have only used this on an internal project,
though based on the official website AutoMapper's [usage is
widespread](http://automapper.codeplex.com/wikipage/comments) with great
success.

Not all mapping is straight property to property however. Sometimes the
source or destination will be of a different type. AutoMapper can handle
this. It is worth mentioning special flavours of mapping such as enums
are supported straight out of the box too. Additionally not all mapping
is one to one. Other times [default
values](http://automapper.codeplex.com/wikipage?title=Null%20Substitution&referringTitle=Home)
may be required, but AutoMapper's fluent interface allows this to be
achieved with limited fuss. AutoMapper can also handle more bespoke,
advanced mapping scenarios. For example we mapped a raw string into a
complete object with default values. This required a [custom value
resolver](http://automapper.codeplex.com/wikipage?title=Custom%20Value%20Resolvers&referringTitle=Home)
to be wrote, which in turn defeats the purpose of using a tool like
AutoMapper but as this scenario was a one off this was not a problem.
All together we're becoming big fans of this tool, it is just a shame it
has taken so long for us to discover it.

### Benefits

There are huge benefits to using AutoMapper. After getting to grips with
the tool we have been able to map a complete webservice within less than
thirty minutes. The trick to creating a hierarchy (objects containing
other objects) is to take a bottom up approach. By taking this approach
each step is gradual and steady. You are not forced to implement a large
chunk of functionality in one go. In combination the way to test this
was to use the built in [AutoMapper
validation](http://automapper.codeplex.com/wikipage?title=Configuration%20Validation&referringTitle=Home).
This one assert will ensure that any mapping that has been written is
indeed valid. This will cover all your standard scenarios. From here, we
wrote one test per object to ensure that any defaulting we had set up
was indeed performed. For the scenario discussed above the webservice
response had around ten types, this meant ten, quick unit tests ensured
the whole mapping functionality worked correctly. The built in testable
assertion makes much of this process a joy to do. While the two main
methods you use with AutoMapper are static, we simply wrapped these in
instance methods that we use in our production code.

Like most open source projects, the documentation for AutoMapper is
pretty weak, though the error output you receive when developing is
outstanding. Each failed test will indicate in plain English what is
wrong, and better yet how to solve it. A few of us are pretty excited
about AutoMapper and I look forward to mapping again in the future,
something I feel odd stating. Yes, this tool is that good.