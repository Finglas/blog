Title: Header Interfaces vs Role Interfaces
Date: 2015-10-01
Author: Shaun Finglas
Tags: programming, code-quality, tutorial
Slug: 2015/10/header-interfaces-vs-role-interfaces

In some languages such as C++ you must define header interfaces. These
constructs define how a public type is exposed in terms of its public
interface. Other languages take a different route. C\# or Java do not
require headers but they are still very much in circulation. This
unfortunately brings along some unwanted side effects.

#### Header Interfaces

Header interfaces are a one to one mapping of public methods that match
the type it is defining. In other words, they are recreating the
overhead of headers in languages that do not need them.

<script src="https://gist.github.com/Finglas/191d9a210e830cb61d83.js"></script>
-   Header interfaces tend to break the Interface Segregation Principle.
-   Harder to switch objects via DI as you are forced to implement all
    members even if you do not use the whole interface.
-   Prone to breakages as the one to one mapping means any change is
    breaking.

#### Role Interfaces

Role interfaces define the role an object plays. Due to various roles
having different responsibilities they are usually grouped by
functionality. Role interfaces are usually combined with composition or
interface inheritance.

The role of a `Developer` has now been introduced. This is a separate
concept from the rest of the object.

<script src="https://gist.github.com/Finglas/ae647867f27a7404720e.js"></script>
-   Easier to follow the Interface Segregation Principle.
-   Closely related to the Liskov Substitution Principle - no need for
    partial implementations.
-   Less chance of breaking changes - interfaces can be removed or added
    easily.
-   Reduced scope - anything that fulfils the role of `Developer` can be
    provided as an argument.
-   DI frameworks may take more configuration if role interfaces are
    used. This may explain the bias towards header interfaces.

#### More

-   <http://blog.ploeh.dk/2013/01/10/RoleInterfaceRoleHint>
-   <http://www.pluralsight.com/courses/encapsulation-solid>
-   <http://martinfowler.com/bliki/RoleInterface.html>