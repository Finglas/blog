Title: Program for Change
Date: 2014-08-01
Author: Shaun Finglas
Tags: retro
Slug: 2014/08/program-for-change

We should program for change AKA the [Open/Closed
Principle](http://en.wikipedia.org/wiki/Open/closed_principle). In my
opinion, the OCP is one of the lesser respected SOLID principles. One of
my biggest, and earliest failures fresh out of university was ignoring
this concept.

At the time I was applying
[YAGNI](http://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it) to some
code myself and a couple of other developers were working on. After all
agile methodologies promote this concept heavily. This made sense to me.
My solution was to solve the problem with the minimal amount of fuss,
however in doing so I strongly coupled the code we produced with the
direct business requirements.

The requirements stated that we would have three different types
expenses. So I promoted that we model these three types of expenses
directly. The UI knew about these expenses. The database knew about
these expenses. The domain logic knew about these expenses.

Everything worked well for a while. We finished early. We wrote just the
code we needed. I was happy. Until the business requirements changed.
The three types of expenses became four, then three again, then one was
replaced completely. Bugger.

The code was unusable. Everything knew just enough to get by, so when
the change came in, everything needed to change. My team was confident
this would be OK. After a few hours of analysis, we concluded the code
was a train wreck. We'd need to restart from the beginning in order to
make the proper changes we wanted. I was pretty gutted, however I
learned a very important lesson.

> YAGNI is about features, not code.

If I was to complete this feature again, I would still start with the
simplest thing that could possibly work. Most likely the code would
explicitly know about each type of expense, yet my tests would be wrote
in an agnostic manner. I would still apply YAGNI, but at a feature
level. In other words, I wouldn't write an expense logger, if all we
need to do is validate and calculate expense totals.

During each refactor stage of the TDD cycle I would remove any specific
expense knowledge. After a while I would end up with the various parts
of the application working with a generic expense algorithm. The tests
would drive us towards how the algorithm would work.

The beauty here is that if a new expense was to be introduced, this
change would be data driven. We would be able to give this the business
for "free".

I still regret this mistake, but this lesson has lived with for some
time and has proved to be a valuable experience.