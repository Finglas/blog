Title: Waste: Write Less Code
Date: 2015-09-01
Author: Shaun Finglas
Tags: retro
Slug: 2015/09/waste-write-less-code

One of the biggest [forms of
waste](https://en.wikipedia.org/wiki/Lean_manufacturing#Types_of_waste)
is code. [An estimated 80% of features in a software project are never
or rarely
used](http://www.amazon.co.uk/Implementing-Lean-Software-Development-Addison-Wesley-ebook/dp/B00HNB3VQE).
This makes code the software development equivalent of inventory. Having
a warehouse full of inventory is not a benefit, neither is having a
repository full of code.

#### How to Have Less Code?

##### Delete it!

As much as you can within reason of course, tests must pass and features
must still work. Deleting feels great when you can successfully remove
some legacy code. You'll be surprised at what can be removed. Commented
out code, unused classes and methods are the obvious first candidates.

##### Say *No* To Features by Default

Only add them if the benefit outweighs planning, designing, development,
testing and maintenance costs combined. Even then, do you really need
it? The advice here is [do not listen to your customers regarding which
features to
add](http://www.amazon.com/ReWork-Change-Way-Work-Forever-ebook/dp/B003ELY7PG/),
instead listen to their problems.

##### Libraries/Frameworks

Try and see if a library or framework can handle your use case. They may
not be a perfect fit, but if isolated correctly the use of third party
code can mean a massive reduction in code you need to write. You still
need to maintain and configure third party code however.

#### Benefits of Less Code

-   Quicker to compile/parse.
-   Tests run quicker.
-   Easier on-boarding - less to understand and familiarise with.
-   Less chance of bugs - more code is more likely to have bugs.
-   Potential performance related problems should be reduced.

Remember - code is a liability. The job of software developer is not to
write code, it is to solve problems. Sometimes this takes thousands of
lines of code, other times it can take a simple conversation.