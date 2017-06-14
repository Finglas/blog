Title: TDD is a Tool
Date: 2014-02-01
Author: Shaun Finglas
Tags: programming, tdd
Slug: 2014/02/tdd-is-tool

I remember being introduced to Test Driven Development (TDD) very well.
This is because it had such an **overwhelming change on how I write code
day to day**. It was incredibly alien, difficult, yet rewarding. On this
journey for the last five years I've changed my style, learned how not
to do it and finally found [my "sweet spot" when it comes to pragmatic
TDD](http://blog.shaunfinglas.co.uk/2014/02/top-down-vs-bottom-up.html).

### Deliver Value

Writing code is fun. Developing an application or system is fun. Using
new technology is fun. Despite this **the end goal should always be to
deliver value**. Delivering business value over religiously following a
practice was a turning point in my journey. After all **the user doesn't
care about what is behind the scenes**, as long as they can use your
software, they're happy.

### When to Write Tests?

One of the guidelines when starting TDD is

> "[Never write a line of code without a failing
> test](http://c2.com/cgi/wiki?NeverWriteaLineOfCodeWithoutaFailingTest)"
> - Kent Beck

**This rule is wrong on many levels**. Firstly it cripples most
developers when starting TDD. Secondly the guideline is broken all the
time by seasoned evangelists. Writing some framework code? Writing data
access code? Writing markup? **Any of these scenarios would be wasted by
writing a failing tests first**. This rule should be reworded.

> "Writing logic? Never write a line of code without a failing test" -
> me

### It's OK to not use TDD

After adoption TDD practitioners tend to face two challenges. Other
developers looking down on non TDD practices and **feeling as if they
are "cheating" when not using TDD**. The later was an issue I struggled
with. Newbies tend to find the same problem, and this goes back to the
mantra above. One of the key lessons I've discovered over the past few
years is that **using TDD where appropriate is fine**. Not all code
needs TDD. Even Kent Beck discusses this when he refers to "[Obvious
Implementation](http://programmers.stackexchange.com/questions/108338/does-tdds-obvious-implementation-mean-code-first-test-after)".

### Spike Solutions

Another game changer in my journey was the concept of "[Spike and
Stabilize](http://lizkeogh.com/2012/06/24/beyond-test-driven-development/)".
Using this technique you can deliver business value quickly. Gather
feedback as soon as possible and either **fail fast or wrap the code in
tests and clean it up**.

### CRUD

Most of the code I (and others) write is very similar. I'd bet this is
the same for different fields of software development. That being said,
for **each CRUD app we create there is a tiny aspect of this that is
unique**. Using TDD to write yet another CRUD app is tedious. I'd
imagine this is why many ditch the practice of TDD after some time.
However the benefit comes from using TDD for that 20% of domain logic.
Here a combination of obvious implementation and spike and stabilize can
assist in the creation of the other 80%.

### It's about Design too

[TDD by
Example](http://www.amazon.co.uk/gp/product/0321146530/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&camp=1634&creative=6738&creativeASIN=0321146530&linkCode=as2&tag=bloshafin-21)
gives the impression that the practice is primarily a testing
discipline. This is not true. TDD does limit the bugs I introduce and
enforces basic correctness, however **bugs will still slip through**.
After all the quality of the code is only as good as the quality of the
tests. [Growing Object Oriented Software: Guided by
Tests](http://www.amazon.co.uk/gp/product/0321503627/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&camp=1634&creative=6738&creativeASIN=0321503627&linkCode=as2&tag=bloshafin-21)
and others introduce the concept that TDD is also a design process.
Listening to the tests is a core concept. In other words, **if something
is hard to test, chances are the code in question can be improved**.

### Follow the Risks

The final lesson I've come to realise is that even if you happen to work
with those who don't practice TDD, you can reap the benefits. Simply
**test where the risk lives**. Ignore the framework, standard library
and simply test what has risk. This might be a small, core part of your
application. Aiming for 100% code coverage is not a goal, nor one worth
aiming for.

### It's a Tool

At the end of the day, **TDD is a tool, not a goal**. In this day and
age many believe that TDD should be mandatory. While I agree, the use
should be restricted to where and when it makes sense. As for when and
where, this is up for the developer to decide. Using some of the
findings above allow me to be pragmatic, yet still have confidence in
the quality of my code.