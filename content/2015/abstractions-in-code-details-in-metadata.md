Title: Abstractions in Code, Details in Metadata
Date: 2015-10-01
Author: Shaun Finglas
Tags: programming, retro
Slug: 2015/10/abstractions-in-code-details-in-metadata

I've programmed many games - each one was special in its own way. One in
particular stands out early in my university studies, a top down
shooter. It was not graphics, gameplay, or sound that made it stand out
however. It was the lesson it taught me about software development.

#### Level One

With the deadline for completion of the project looming, time was
running out. The core game engine was complete but other than the first
level there was nothing else for the player to do. With more marks
awarded for various components I decided to add a second level.

At the time the game consisted of a source file called `level.cs`. This
contained parts of functionality explicit to every level that I would
need. It also contained code specific to the first level. My solution
was to extract a base class and introduce `level.cs` and `level1.cs`.
This worked. The addition of level two was not as easy. The second level
required a considerable amount of additional code, despite the shared
functionality. A slow feedback cycle of change, compile, and test, made
this addition even more tedious. With the test phase consuming much of
my time.

Hopefully you can see where this is going. While I never added a third
level, the same problem exists. In fact for every additional level the
problem would get worse.

#### Lesson

The lesson I learned here was that a game engine should be abstract,
while the details of the level should be data that is configured outside
of the code. This allows anyone to make levels for the game. Levels can
be unique rather than constrained to how the programmers coded them to
be, introducing novel gameplay elements constrained only by the
imagination of the designers.

This concept is not unique to games programming. I would learn a few
years later that this is a well known and advised practice - [The
Pragmatic
Programmer](https://pragprog.com/book/tpp/the-pragmatic-programmer)
summarises that abstractions should live in code, while details lives in
metadata (data about data).

> "Program for the general case, and put the specifics outside the
> compiled code base."

Those of you with a keen sense for code smells may be thinking about
another issue with this story, and yes, you're right. The base class
caused issues. The use and misuse of inheritance will be the subject of
a future post.