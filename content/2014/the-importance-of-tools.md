Title: The Importance of Tools
Date: 2014-07-22 19:19
Author: Shaun Finglas
Tags: best-practices, http://schemas.google.com/blogger/2008/kind#post, tools
Slug: the-importance-of-tools

One of the most influential books I've read on software development has
been [The Pragmatic
Programmer](http://www.amazon.co.uk/gp/product/020161622X/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&camp=1634&creative=6738&creativeASIN=020161622X&linkCode=as2&tag=bloshafin-21).

One of the key points raised within the book is that of automation and
tooling. For example, automating the build process is a very worthwhile
undertaking. You should be able to check out some code and execute a
script that will set up your machine, compile, test and deploy the code
base in question.

The key benefit of automating even trivial tasks such as automatically
pulling down the latest code daily is that unlike developers, automating
tooling will never perform the task wrong. Nor will they forget to do
it. Ultimately this prevents the dreaded "works on my machine" issue.

I've become such a fan of this approach to automating away any manual
steps that some of the [most used code I've
written](https://github.com/Finglas/commit.cmd) has been small scripts
that execute hundreds of times a day. From a development point of view,
the likes of good practices, SOLID, OO etc.. are usually void, such
scripts simply get the job done, allowing myself to focus on the more
important tasks such as delivering business value else where.

There is not a lot else to say on the subject of tooling. The best tools
should be composable, proven solutions where possible. In other words,
rather than something that must be configured via a GUI, opt for
something that can be automated. Also ensure that you are not
re-inventing the wheel unnecessarily. Save your time and energy on
creating the custom tooling you can't get "off the shelf".

</p>

