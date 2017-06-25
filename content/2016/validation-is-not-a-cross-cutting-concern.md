Title: Validation is not a Cross Cutting Concern
Date: 2016-01-01
Author: Shaun Finglas
Tags: programming, tutorial
Slug: 2016/01/validation-is-not-cross-cutting-concern

Attributes in C\# are also known as [decorators in
Python](https://wiki.python.org/moin/PythonDecorators) or [annotations
in Java](http://docs.oracle.com/javase/tutorial/java/annotations/).
Other languages may have similar constructs. This post will use
*attribute* throughout but refers to the same concept.

------------------------------------------------------------------------

While attributes prove useful for cross cutting concerns such as
authorization or logging, they can be misused. Attributes should act as
metadata, providing no direct behaviour. Failing to do so will make DI,
testability and composition very difficult.

These flaws are especially true for validation. Despite all input
requiring validation, the manner in which validation is performed is
dependent on the entry point to the code. [Context
matters](https://blog.shaunfinglas.co.uk/2014/09/ddd-validation.html).

Consider order information that requires a billing address and by
definition, its children to be populated. An attribute works a treat
here in this simple case.

<script src="https://gist.github.com/Finglas/22749d5755b9fa3337c4.js"></script>
A problem arises if you only want the billing address validation to
activate if the billing address and delivery address differ.

Complexity quickly starts to take over. With a more fully featured
example attributes can start to overwhelm the class. This example
becomes worse if the validation is required to be performed by a third
party library or service. Finding a hook to integrate becomes
troublesome.

#### Solution

Avoid attributes for validation in all but the simplest scenarios. Even
simple scenarios lead to some churn if you do decide to switch. My
personal preference is to now avoid attributes all together, instead
opting to use a validation service.

The obvious downside to this is approach is the appearance of more code.
While this is true, composed object graphs can benefit from the ability
of reuse. Additionally in the case of attributes some degree of testing
is required. These usually fall into the category of asserting the
presence of attributes on properties which is far from ideal. The use of
validation services do not suffer this problem. Internally the
implementation can be switched, altered or refactored without fear of
breaking any tests.

#### Example

<script src="https://gist.github.com/Finglas/1100d60aa521a555c972.js"></script>
The RootValidator is a composite of zero or more actual validators. Each
validator can be specific to a particular task. The only requirement
being the interface must be the parent object. This is to ensure the
context is not lost when making decisions. The actual interface in this
case could be made to use generic types if required. The
[ValidationResults](https://gist.github.com/Finglas/ee7de5821376ce26543b)
are a simple value type representing an aggregation of validation
failures. This could be extended or modified for further enhancements.

#### Benefits

-   Composition makes it possible to provide multiple validators that
    all do one thing well.
-   Testing is much easy as you can test each validator in isolation.
-   Null validators provides easier higher level testing as you can
    provide a no-op validator. Removing the need to build up complex
    object graphs for other test cases.
-   Developers can follow, debug and understand simple conditional logic
    more so than framework specific metadata.
-   Open to extension and additions such as third party code.
-   Services never lose context which allows easy runtime decisions to
    be made.