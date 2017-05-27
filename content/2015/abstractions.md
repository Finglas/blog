Title: Abstractions
Date: 2015-04-22 17:19
Author: Shaun Finglas
Tags: best-practices, http://schemas.google.com/blogger/2008/kind#post, abstractions-series, code-quality
Slug: abstractions

This is the first part of my series on abstractions.

-   Part 2 - [Reused Abstraction
    Principle](http://blog.shaunfinglas.co.uk/2015/03/reused-abstraction-principle.html)
-   Part 3 - [Dependency Elimination
    Principle](http://blog.shaunfinglas.co.uk/2015/03/dependency-elimination-principle.html)

------------------------------------------------------------------------

Coupling is one of the enemies of a healthy code base. One way to combat
high coupling is to introduce abstractions.

Too few abstractions is bad. Your code can become coupled. Some of the
worst code I've worked with was highly coupled to either the database,
UI or both. Working with such code is difficult.

Too many abstractions is equally as bad. Abstraction behind abstraction
can become so difficult to work with the benefit of abstracting in the
first place is lost. Some of the worst code I've worked with was so
convoluted with needless abstractions it made any development a tricky
process.

[Most abstractions are not really abstractions at
all](http://blog.ploeh.dk/2010/12/02/Interfacesarenotabstractions/), but
nothing more than simple indirection. Indirection is sometimes required,
though it is wrong to confuse with abstraction. `IFileWriter` is not an
abstraction. `IReciept` that happens to write to the file system when
implemented as `FileSystemReceipt` is an abstraction. `IFileWriter`
*could* be an abstraction if the software we were writing involved
working directly with the file system, such as a text editor. In the
case of printing receipts, where they are printed is simply an
implementation detail.

Finding a balance between the right level of abstraction can be tricky.
From my experience there a few techniques that can be used.

#### Techniques

##### Embrace Coupling

[Udi Dahan](http://www.udidahan.com/?blog=true) makes this point in his
presentations. If you have a traditional application with a UI, domain
and data layer why bother adding further layers to abstract these? If we
wish to retrieve a new field from the database and display the value we
have three places to change, adding further models and mapping layers
does nothing but increase coupling. [Applying namespaces
correctly](http://blog.shaunfinglas.co.uk/2014/07/i-need-to-stop-misusing-namespaces.html)
can also help here, if everything that needs to change at the same time
is logically grouped, such changes are easier.

##### Apply YAGNI

[Do you truly need a database model mapped into a domain model, mapped
into a view model and back?](http://codeopinion.com/simplify-your-code/)
Applying YAGNI can limit many abstractions by simply not worrying about
"*what if*" scenarios until they actually occur.

##### CQRS

[Command Query Responsibility Separation or
CQRS](http://martinfowler.com/bliki/CQRS.html) deserves an explanation
on its own, but for now applying CQRS reduces unnecessary coupling by
embracing it. For querying data and displaying it on a screen my default
choice is to use CQRS to simply read from the database and populate a
view model. This limits abstractions and helps keep the code focused,
flexible and open to change. [I will expand on CQRS in a future
post](http://blog.shaunfinglas.co.uk/2015/04/cqrs-simplest-introduction.html).

</p>

