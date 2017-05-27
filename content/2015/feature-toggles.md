Title: Feature Toggles
Date: 2015-06-09 21:42
Author: Shaun Finglas
Tags: http://schemas.google.com/blogger/2008/kind#post, development, releasing, deployment
Slug: feature-toggles

I'm a fan of regular releasing. My background and experience leads me to
release as regularly as possible. There are numerous benefits to regular
releases; limited risk, slicker release processes and the ability to
change as requirements evolve.

The problem with this concept is how can you release when features are
not functionally complete?

#### Solution

If there is still work in progress, one solution to allow frequent
releases is to use [feature
toggles](http://martinfowler.com/bliki/FeatureToggle.html). Feature
toggles are simple conditional statements that are either enabled or
disabled based on some condition.

<script src="https://gist.github.com/Finglas/89438d0ec51aff4149d0.js"></script>
This simple example shows a feature toggle for an "Edit User" feature.
If the boolean condition is false, then we only show the "New User"
feature and the "Admin" feature. This boolean value will be provided by
various means, usually a configuration file. This means at certain
points we can change this value in order to demonstrate the "Edit User"
functionality. Our demo environment could have this enabled, while the
live system would be disabled until the feature is fully complete.

If the feature to edit users took more than an ideal release cycle the
code could still be released. As long as all the tests and other release
checks pass there is no reason to defer this task. This is after all one
of the benefits of continuous integration. Any consumer of this code
base would always be working with up to date code, merge conflicts would
be next to non existent. Our new code would be integrated regularly.

Ideally feature toggles live as high as possible in the dependency graph
of your application. In most cases this would be the composition root of
the application or within UI/presentation logic. This simplifies the
addition of toggles, but you need to be careful that just because the UI
hides a feature it is not truly disabled. In scenarios where security is
a concern the feature toggles may need to live further down the stack.

It's best to remove feature toggles once the feature is complete
otherwise they can become a maintenance burden. Is this feature enabled
or disabled? Can we delete this code? These sort of questions can cause
legacy code to live unquestioned. One way to aid in their removal is to
add assertions to fail the build at a certain point in the future or
include a toggle with built in date/time logic.

Feature Toggles help with demonstrating features, but they can be more
complex. For risky features you may want to slowly ramp up the number of
users who are exposed to the feature. In this case the actual toggle may
perform some basic logic such as "*one out of ten requests*" enable the
new feature. Overtime this ratio can be increased until the feature is
fully enabled and proven.

Another technique to allow fast, regular releases is to rely on [Branch
by
Abstraction](http://blog.shaunfinglas.co.uk/2015/06/branch-by-abstraction.html).
This works great when the toggles live in the composition root or the
team have the ability to split work around features.

</p>

