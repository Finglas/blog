Title: Static Code
Date: 2015-07-07 20:40
Author: Shaun Finglas
Tags: best-practices, http://schemas.google.com/blogger/2008/kind#post, programming, code-quality
Slug: static-code

Static code is considered a bad thing by developers. This is especially
true when working with legacy code. The use of static code is often seen
as a smell and should not be used.

This is not as black and white as it first seems. Static code can be
problematic when global state is involved. Not only is it hard to
change, static code is very hard to test in an automated fashion. Bad
examples of static code include persistence, third party services, and
out of process calls. These examples should avoid static code where
possible.

One guideline that served me very well in my early days of TDD was
treating [static code as a death to
testability](http://misko.hevery.com/2008/12/15/static-methods-are-death-to-testability/).
Unfortunately some developers don't move on from this guideline and
treat any use of static code as bad.

In fact static code can have a benefit. If a method within a class can
be promoted to a public static method (PSM) it shows that the code is
stateless. This allows the "extract class" refactoring to be performed.
Without a PSM such refactoring is much more difficult. IDEs can automate
this step and if in a dynamic language you can simply lean on the
runtime to catch issues.

<p>
The steps to perform this refactor are easy. If at any stage this is not
possible the method contains state.

</li>
1.  Make the method public.
2.  Make the method static.
3.  Move the public static method to the new class.
4.  Update usage of the previous calls.
5.  Optionally remove the static modifier and update previous call
    sites.

If the code cannot be promoted to a PSM then state exists. Increasingly
the code I write leads itself to a functional paradigm despite not be
written in a strictly functional language. Small, focused classes that
tend to be immutable. The use of PSM makes transition to this style of
code easy. There is no reason to avoid the use of static code as an
intermediate step to get to this position.

</p>

