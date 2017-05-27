Title: Pre Computation
Date: 2015-11-03 07:53
Author: Shaun Finglas
Tags: release-it, http://schemas.google.com/blogger/2008/kind#post, books, architecture
Slug: pre-computation

[Caching is a common
technique](http://blog.shaunfinglas.co.uk/2015/01/caching.html),
especially with HTTP as it is made so easy. However pre computation is
an alternative that can be used to reduce failures as well as speed up
processing and response times.

#### Caching Example

Assume a list of countries to be displayed on the UI. These are often
stored in one logical place, the database. A remote call is issued to
query the database and return the results. The results are then
manipulated and inserted into the UI. Repeat calls will then be cached
for some period by the web server and/or proxy.

#### Pre Computed Example

As part of the build process have the same query performed, dynamically
building up the result set. Using a templating language modify a base
source file which simply inserts the dynamic result set. The end result
of this would be a source file containing a collection of countries as
if you had hardcoded the values. The difference is these values are
pulled from a single source of truth as part of the pre build step.

In a statically compiled language you would have compile time safety
after this file is generated. Regardless a simple suite of tests to
ensure the collection is not empty or badly formed would be beneficial.

Once the deploy is complete all queries to retrieve the collection of
countries would be performed by the pre computed collection. This
technique works regardless of language due to the simplicity of storing
a collection of items in a literal array or hashtable. For content that
changes regularly you can use a separate content deploy which simply
deploys any changes to content.

Pre computation works for even what appears to be dynamic content.
Article submission sites, e-commerce or wikis could all be developed
using pre computation.

Use punch outs for anything that varies based on user or context.
Javascript is the natural choice for inserting this dynamic content.
This advice flies in the face of much of the direction the modern web is
heading. However the benefits of reduced remote calls, fast responses
and less moving parts should not be under estimated.

Naturally pre computation will not work in areas where content is highly
dynamic or specific to users. Single page applications, social media
streams and the like are better suited to dynamic content cached where
possible. Additionally adjusting a system to handle content deploys is
not something that can be achieved lightly. As the build and deploy
process must accommodate these changes, pre computation is usually
required to be thought of up front or require some rework to introduce.

</p>

