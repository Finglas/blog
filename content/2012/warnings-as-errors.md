Title: Warnings as Errors
Date: 2012-02-01
Author: Shaun Finglas
Tags: programming
Slug: 2012/02/warnings-as-errors

One thing that annoyed me when starting at Codeweavers was the amounts
of warnings that would occur during a build of any of our projects.
Seeing the build progress only to spew out a screenful of text was
something that did not sit right with me. I was not the only one who
felt this was wrong, but as there was so many warnings in some cases, it
was easier just to pretend they were not there. After all everything was
working fine.

The [broken window
theory](http://www.codinghorror.com/blog/2005/06/the-broken-window-theory.html)
is very much in action here. During our last standards review we decided
that there should ideally be zero warnings per project. It is worth
mentioning that most of our warnings were just that, warnings about
something that was not really a major issue. Warnings such as unused
variables and so on fall into this area.

On the other hand, while 90% of our warnings were ignorable, there were
a handful which were rather important. Examples such as referencing
different versions of required .dlls. Warnings like this are extremely
helpful. It would be wrong for these to be hidden among a block of less
serious issues. Warnings such as these once visible, can save hours of
painful debugging.

Some of our projects had a fair few warnings - in the region of fifty
plus. In order to begin tackling these larger projects we started
slowly. If in a single day I would have removed a batch of warnings,
this was a step in the right direction. After a week or so all our
projects were void of warnings.

The next step was to make sure we do not go back to having larger
projects with warnings galore. To prevent this I enabled "**Treat
warnings as errors**" within Visual Studio. This is per project setting
and can be found under the "**Build**" tab. Do note that you must enable
this for "**All Configurations**" otherwise any settings you change will
only apply to Debug/Release builds.

I like this feature of Visual Studio immensely. Having the compilier do
as much work as possible - in this case check for warnings is similar to
a tip found in [Working Effectively with Legacy
Code](http://www.amazon.co.uk/Working-Effectively-Legacy-Code-ebook/dp/B0017DQ8KU/ref=sr_1_3?ie=UTF8&qid=1329313155&sr=8-3).
Here the concept of "leaning on the compiler" is introduced. In other
words you introduce an error in order to show you the usages of a piece
of code - this is stark contrast to manually searching for the code in
question.

The end result of this process is now during a build, if any warnings
occur, the build will fail. The build will report where the warning is,
along with why there is a problem. While this is great in theory it can
cause some slight pain when developing, as you may comment out some code
to experiment only to find the build failing due to unused variables.
Despite this treating warnings as errors has been a great help. Recently
we have solved some pretty serious issues with regards third party
dependencies all thanks to treating warnings as errors.

*The idea of allowing the computer to do as much work as possible
applies to all languages. For your compiler/interpreter etc... there
will be an option to apply warnings. This is not a specific language
feature.*