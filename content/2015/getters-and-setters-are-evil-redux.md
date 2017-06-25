Title: Getters and Setters are Evil - Redux
Date: 2015-04-01
Author: Shaun Finglas
Tags: programming, tutorial
Slug: 2015/04/getters-and-setters-are-evil-redux

Back in early 2011 I wrote one of my [most viewed and commented posts at
the time - Getters and Setters are
Evil](https://blog.shaunfinglas.co.uk/2011/04/getters-and-setters-are-evil.html).
Four years later it's time to review this.

The feedback within the team was generally positive. Production code was
written in this style to great success. The core benefit was
encapsulation was preserved as Business Objects were the sole source of
domain logic. As an additional side effect testing was easier.

However not everyone within the team agreed that the benefits were worth
the extra hassle or believed in the benefits of encapsulation. I always
found the addition of an `IRender` interface or similar broke the SRP,
even if you moved the logic to a separate class. The OCP suffered too,
if view requirements changed, you need dig out your business object. The
biggest failing is that legacy code and frameworks still require public
getters/setters to function.

Overtime I found myself and others slipping back to the "old ways" of
applying getters/setters without thought.

#### 2015

[I now simply use two models, where the used to be
one](https://blog.shaunfinglas.co.uk/2015/04/cqrs-simplest-introduction.html).
Changes go to the domain model in the form of commands. Queries get
returned as view models. The big change here is to simply split commands
from queries and embrace the second model, everything else falls into
place. This style works without a rich domain model also. The commands
can be expressed as Transaction Scripts or similar if desired.

<script src="https://gist.github.com/Finglas/a9bdd46c394ac06032fe.js"></script>
This is not new, I've applied this style in the past, but the big
difference is the business object is never mapped or converted into a
view model. There is no relationship between the two. They are two
distinct paths in the code. This is the difference that CQRS brings -
limited coupling.

#### Benefits

Encapsulation is preserved as before, but the view model can be tailored
to requirements. SOLID principles are not broken, while still having the
huge benefit of playing nicely with frameworks due to exposing public
getter/setters in order to facilitate model binding.

Getters and Setters are not evil as I've concluded before. It just turns
out there are better ways of embracing the benefits of thinking they are
evil.

------------------------------------------------------------------------

The term Business Object is also known as Domain Object. The later being
my preferred term now. I stuck with the original terminology to match
the original post's code example.