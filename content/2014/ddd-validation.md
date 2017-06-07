Title: DDD Validation
Date: 2014-09-01
Author: Shaun Finglas
Tags: programming, tutorial
Slug: 2014/09/ddd-validation

Validation within an application (specifically in terms of [Domain
Driven Design - DDD](http://en.wikipedia.org/wiki/Domain-driven_design))
can be solved in a variety of ways.

-   A validate method on the entity/value type in question
-   An IsValid property/accessor on the entity/value type in question
-   A separate service could be used

#### Validate Method

Adding a validate method would work, but the flaw with this approach is
that you lack any context of what is happening to the object in
question.

#### Validate Flag

Some sort of flag on the object that denotes whether or not the object
is in a valid state is undesirable. Firstly it forces the developer to
ensure they check this at the correct time. If the object is invalid,
exactly what do you do at this point? This approach is often used with a
combination of a validate method that returns the exact error messages.

#### Validator Services

A separate service seems less than ideal at first when you consider
developing a richer domain model, but this solution has numerous
benefits. Firstly unlike the two solutions above you always have the
context in which validation is being performed. For example, if you are
saving a customer you will most likely want to perform different
validation to what you would perform when loading up an aggregate.

An additional point to consider is that most validation is not business
logic. In other words, [checking for null references is not a business
concern. Therefore separating this from your domain objects makes a lot
of
sense.](http://blog.shaunfinglas.co.uk/2016/01/application-validation-and-domain.html)
The only logic the domain objects should contain is business logic.

As each service is a separate object, you gain the benefits of the
single responsibility principle (SRP). Meaning testing, development and
future changes are easier.

#### Example

<script src="https://gist.github.com/Finglas/e522caca787c75cdea0f.js"></script>
The beauty here is that each validator (a simple function in this case)
can be used in the correct context. E.g. when the PersonController POST
handler is invoked, we use the person saving validator.