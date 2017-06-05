Title: MVC is Broken
Date: 2012-10-01
Author: Shaun Finglas
Tags: retro
Slug: 2012/10/mvc-is-broken

If you look up the definition of [MVC or Model View
Controller](http://en.wikipedia.org/wiki/Model_view_controller), it will
hail the definition as being able to change your front end without
affecting other parts of the application and vice versa. This sounds
great in theory, however this claim is nothing more than a *blatant
lie*.

A failing of the architectural pattern comes from the whole codebase
being tied to a specific stack. Take ASP.NET MVC. The domain logic will
most likely be in C\#. Therefore your models will be in C\#. Your
controllers will be in C\#. Your views will be a mixture of C\# and some
form of a templating language.

If you want to change your stack to the "next big thing" you are forced
to take a big bang approach. ASP.NET MVC *won't be around forever*.
Being tied to a specific technology feels wrong. Therefore this coupling
means your designers are forced to use the templating language that your
framework supports. This should be a flexible option that should be easy
to change, after all the MVC pattern states this as one of it's
benefits.

Being tied to a specific technology leads onto our most recent project.
One of our biggest and most important projects is a legacy Flash
application. Back in the early 2000's it was a cutting edge application
- consistent across all browsers, ajax style requests, responsive
design, you name it.

That being said we all know Flash is on its way out, and there lies the
problem. It took myself about two weeks to add a few text boxes to the
app in my first year at Codeweavers, all because the UI code is so
difficult to work with. The *logic is mixed within the UI*. Had the app
been developed in a MVC style we would be in a position to replace the
legacy UI with a modern alternative.

We make use of [SOA or Service Oriented
Architecture](http://en.wikipedia.org/wiki/Service-oriented_architecture)
at Codeweavers, therefore it seemed a natural fit to apply this to our
rewrite of our legacy application. I proposed a theory:

> **"for an application to be truly independent of the frontend and
> backend the code must be developed in different languages."**

For example, I taught myself enough PHP to make a JSON request, perform
some conditional logic and loop over a collection. With this I was able
to recreate one of our applications that was powered by our backend C\#
services. [I would not want to create an application in
PHP](http://www.codinghorror.com/blog/2012/06/the-php-singularity.html),
but using PHP as a templating language was a great fit. After all this
is one of the intentions of the language. Limiting myself to just three
simple PHP constructs I was *forced to put all logic on the service* in
question.

This complete separation of concerns is made possible due to the fact it
is simply not possible for code to leak between the layers due to the
different languages used in the implementation. This means I could
easily spin up numerous front end views while the backend remains
unchanged. Likewise we could change the back end implementation from C\#
to another language. Providing the endpoints and request/responses
match, the front end will still be functional. This full separation of
concerns is what MVC style frameworks have *failed to achieve*.

In ten years from now it is hard to say what the web will look like.
What I can guarantee is that the web will still be here. We'll still be
making HTTP requests. We'll still be making back end services that
powers much of the apps on the internet. One thing no one can really
comment on is what the web will look like. One point we all could agree
on is that HTML5 should be wide spread and no doubt "*the next big
thing*" will be on the horizon. The great thing by taking the approach
discussed previously is that Codeweavers will be in the position to
change either the front end or back end of our codebase at any time.
Precisely what the MVC pattern has failed to deliver.