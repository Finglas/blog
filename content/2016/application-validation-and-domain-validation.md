Title: Application Validation and Domain Validation
Date: 2016-01-13 19:58
Author: Shaun Finglas
Tags: http://schemas.google.com/blogger/2008/kind#post, validation, DDD
Slug: application-validation-and-domain-validation

There are two types of validation in an application - application
validation and domain validation. This applies whether or not you
practice DDD. One of my mistakes in the past has been confusing or
conflating these two responsibilities at the same time.

#### Application Validation

Application validation is anything technical or anything domain experts
would likely scratch their heads at. Examples include:

-   is the input null?
-   is the input whitespace or empty?
-   is the input within ranges for the datatypes used?
-   is the length of the input suitable for the DB?

Application validation should occur in your application service, along
with other technical aspects such as transactions or configuration. This
is due to different applications having different technical
requirements. For example a HTML frontend may differ to a web service,
so application validation would need to vary also.

This form of validation is best performed using [validation
services](http://blog.shaunfinglas.co.uk/2014/09/ddd-validation.html).
The use of attributes/decorators/annotations can also be used though
[the following post will explain why this is usually a bad
idea](http://blog.shaunfinglas.co.uk/2016/01/validation-is-not-cross-cutting-concern.html).

#### Domain Validation

Domain validation is concepts the business or domain experts would
understand. Examples include:

-   "*employees can only take a holiday if they have not used their
    allowance*"
-   "*estimated delivery dates should not fall on holidays*"
-   "*users can only edit their own posts*"

Once inside your domain, validation should live as part of your domain
model or domain logic. If [value types are utilised you can safely omit
additional application
validation](http://blog.shaunfinglas.co.uk/2015/02/value-object-refactoring.html)
as each object would ensure consistency.

</p>

