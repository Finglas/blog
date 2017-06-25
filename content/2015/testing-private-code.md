Title: Testing Private Code
Date: 2015-05-01
Author: Shaun Finglas
Tags: testing, tdd, unit-testing
Slug: 2015/05/testing-private-code

A common problem many people ask is - should you test private code? In
short, you shouldn't. You should always test the public api of your code
where possible. This is not always easy. Based on the context of the
code in question there are a few options available.

##### Don't Test

Either don't test the private code or rely on manual testing. This will
not be ideal in many cases, but if the code is covered in higher level
tests you may be able to get away with it. If the code will be stable,
short lived or low risk you can default to this option.

##### Test via Public Tests

Simply test the private code by adding assertions or verifications to
exisiting public behaviour tests. If the setup requires a lot of work,
many edge cases or much duplication you may want to avoid this
technique.

##### Make the Code Public

Once public, the code is easily testable. Are we making this code public
just for the sake of an automated test? Yes, but there are valid times
to do this. Providing the behaviour is logically part of the object in
question there is no harm, the single responsibility principle is not
violated.

[Interfaces can be used to control visibility
here](http://blog.ploeh.dk/2011/02/28/Interfacesareaccessmodifiers/).
For testing you always use a concrete instance, while your production
code should hold references to interfaces only. To simply hide the
method, don't add it to the interface. For dynamic langauges this is as
simple as "*don't invoke it*" or relying on naming conventions to
denoate implementation details.

##### Make a Public Class

When single responsibility principle would be violated in the technique
above, this is your other option. [Beware the power of just adding a new
class and making it
public](https://blog.shaunfinglas.co.uk/2014/12/stop-making-everything-public.html).
While it will allow testing in one place, [each public dependency you
introduce further increases
coupling](https://blog.shaunfinglas.co.uk/2014/12/limit-amount-of-dependencies-you-use.html).

If the code that needs testing is a service, the act to introduce a
public object should be considered thoughtfully. Once the class is
pubic, you simply need to verify the use of the class, rather than what
it does. However [Value Objects can help limit the tests you need to
write](https://blog.shaunfinglas.co.uk/2015/02/value-object-refactoring.html)
entirely and should be used whenever possible.