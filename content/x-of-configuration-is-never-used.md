Title: X% of Configuration is Never Used
Date: 2016-04-26 07:08
Author: Shaun Finglas
Tags: best-practices, http://schemas.google.com/blogger/2008/kind#post, programming, code-quality
Slug: x-of-configuration-is-never-used

Code configuration is essentially for the likes of URLs, credentials or
other per deployable settings. Sadly configuration seems to fall into
examples where there is simply too much configuration, or the system has
so many configuration points the actual code becomes far too complex for
its own good.

#### Too Much Config

I once worked on a system with in excess of six hundred different
configuration points. In reality all but a handful of these would ever
actually need changing. Most configuration is added to enable *anyone*
to make the change. Ironically if these configuration points do need
changing, developers need to do it. The business or non technical
individuals will never change settings. In this scenario you would need
to actually test all six hundred different combinations of
configuration. 1 on, 599 off, 2 on, 598 off and so on - this is not
ideal nor realistic.

#### Configurable Systems are Complex

One of the earliest project mistakes I can remember involved creating a
system that could be configured by *anyone*. A simple task became a
several day exploration in failure. Each quarter a minor change to a
static ASP page was required. This involved a date and some minor
alterations to some financial wording for legal requirements. Instead of
simply making the change I started building a custom CMS. A form
overlayed the content allowing anyone to make the change and generate
the page. It worked a treat technically, except it never saw the light
of day. The business would not use it. Numerous individuals required
approval before the change could be put live; security, legal, branding
and several more. Also using the form still required some implicit
knowledge of HTML. At the end of this we threw the prototype away and I
made the change in a matter of minutes. My mistake here was building a
solution that was not required.

#### Implementation

When it comes to implementing configuration a common mistake is to rely
upon the method of obtaining the value, rather than the value itself.
Additionally the use of some form of abstraction is often mistakenly
used such as IConfiguration.

[The solution is to instead provide the configuration value, not the
means of obtaining
it](http://blog.shaunfinglas.co.uk/2015/03/dependency-elimination-principle.html).
This can be done either via a constructor or directly to the method.
This allows the configuration to be provided in different manners such
as from a DB or file, with no code changes apart from the composition
root. Such solutions are easily testable and open to modification.

<script src="https://gist.github.com/Finglas/98f6e56488563d92fb2b54266fe5f3c4.js"></script>
#### Lessons

-   Only add configuration for values that will certainly change between
    deployable units such as credentials or URLs.
-   Leave everything else where it belongs, either in the source file
    next to a class, in a method or whatever is easiest. If it needs to
    change, just make the change when the time comes. Chances are it
    will never come.
-   If a configuration value is changed, run your automated tests (or a
    subset) against the deployable unit.
-   A configuration change should be treated as a code change.
-   The business will never change your configuration - that's a
    technical task.
-   Provide configurations values, not the means of obtaining them.
-   Rely upon convention over configuration as much as possible.

</p>

