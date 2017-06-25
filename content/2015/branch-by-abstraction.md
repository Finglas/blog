Title: Branch by Abstraction
Date: 2015-06-01
Author: Shaun Finglas
Tags: tutorial, programming
Slug: 2015/06/branch-by-abstraction

Feature toggles are great for new features or features that are either
enabled or disabled. Branch by Abstraction offers the [same benefits as
feature
toggles](https://blog.shaunfinglas.co.uk/2015/06/feature-toggles.html)
but the seam to introduce the change is the abstraction itself. Unlike
Feature Toggles, the use of Branch by Abstraction allows a gradual
transition to new functionality.

Start by duplicating the type or implementing a new version of the
abstraction. The work in progress changes can be made safely while the
system is using the original implementations. In order to demonstrate
the new functionality, rely on automated tests or wire up the new
version. Once fully integrated and tested, simply remove the old
implementation. The addition or removal of implementations acts as the
toggle in this case.

<script src="https://gist.github.com/Finglas/779dc06ff19e7e842ff6.js"></script>
To extend the `SimpleReceiptWriter` a new version is made. This work in
progress implementation has no limit on the time to complete. The new
implementation will only take effect once configured.

<script src="https://gist.github.com/Finglas/bfe505e8f7946fa9b2fc.js"></script>
Configuration takes the form of composition root or dependency injection
container changes. Given your code does not know the concrete
implementation (apart from tests) you should be fine to make these
switches.

[If no abstraction exists you can introduce one if
valid](https://blog.shaunfinglas.co.uk/2015/02/abstractions.html). If no
valid abstraction exists you can simply fallback to feature toggles.

Branch by Abstraction plays nicely with [Walking
Skeletons](https://blog.shaunfinglas.co.uk/2015/05/walking-skeleton.html).
Your first implementation will most likely be a simple first pass
attempt. Overtime these can be replaced with more fleshed out versions.

Anytime you feel the need to create a branch in source, Branch by
Abstraction can be a valid alternate in most cases. [UI changes are
better suited as Feature
Toggles](https://blog.shaunfinglas.co.uk/2015/06/feature-toggles.html)
due to the nature of the code.