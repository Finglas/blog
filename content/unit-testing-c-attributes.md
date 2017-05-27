Title: Unit Testing C# attributes
Date: 2014-08-17 15:19
Author: Shaun Finglas
Tags: testing, http://schemas.google.com/blogger/2008/kind#post
Slug: unit-testing-c-attributes

For a recent coding session I needed to handle an exception being thrown
when some Json was incorrectly bound to a view model. With the framework
we were using ([ASP.NET](http://www.asp.net/mvc "ASP.NET MVC2") MVC2) I
was unable to handle the exception at the controller level, nor could I
handle it at the "global" level when the framework carries out its
bindings. Another way ASP.NET MVC handles [exceptions is via
attributes](http://msdn.microsoft.com/en-us/library/system.web.mvc.handleerrorattribute.aspx)
to catch errors you specify. The resulting exception is strongly typed
and then can be passed into a view, from which you have full control of
what to do. Typically we would log the error, display a friendly message
and so forth.

In the past these attributes have been simply applied without a test -
the general consensus being this was a framework specific thing which
had no value in being tested. I agreed with those statements up until
several minutes ago. Having fixed a defect in which the user was not
seeing a friendly error message I carried on with a new feature only to
find somehow the error handling had broken. It turned out I had indeed
broken the attribute by providing an incorrect parameter.

As luck would have it there is a very nice, quick way to [unit test
attributes as discussed on
StackOverflow](http://stackoverflow.com/questions/2007434/how-to-nunit-test-for-a-methods-attribute-existance).
In the end I created several tests to check the following:

-   The type of the attribute is correct
-   The attributes properties were correctly set

The tests ended up ensuring that my action does indeed handle certain
exceptions, redirecting the user to the correct view. The nice thing
about these tests are they will only take minutes to write next time,
yet save me a long time figuring out why the error handling has broken.
Plus being unit tests they execute in the blink of an eye, no need to
write a regression test to check the redirection has been carried out.
These tests are therefore more "documentation" of how the system should
behave.

</p>

