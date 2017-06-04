Title: Ten Things a graduate will experience during their first year at Codeweavers
Date: 2011-08-01
Author: Shaun Finglas
Tags: retro
Slug: 2011/08/ten-things-graduate-will-experience

1.  **Kanban**

    The importance of value and flow are the heart of day to day running
    at Codeweavers. During my time I've read books such as [The
    Goal](http://www.amazon.co.uk/Goal-Process-Ongoing-Improvement/dp/0566086654)
    and [The Toyota
    Way](http://www.amazon.co.uk/Toyota-Way-Management-Principles-Manufacturer/dp/0071392319)
    in which the likes of the [Theory of
    Constraints](http://en.wikipedia.org/wiki/Theory_of_Constraints) and
    the [Toyota Production
    System](http://en.wikipedia.org/wiki/Toyota_Production_System) are
    discussed. I was also lucky enough to visit Toyota to see these
    practices in play.

2.  **Pair Programming**

    A big part of our day to day work is done via pair programming.
    There are huge benefits to pair programming, but being a graduate
    within an organisation where pair programming is the norm is a huge
    benefit. Graduates usually enter the workplace with no experience in
    the business domain and limited technical experience. Being set
    loose initially would be a disaster. Graduates therefore typically
    shadow other developers often spending anywhere from weeks to months
    until they able to commit any code without supervision. With
    Codeweavers this was not an issue. From day one I was committing
    code despite being the least knowledgeable member of the team. In
    fact, my earliest memory of my first day involved fixing a defect in
    a codebase of which I knew nothing about. Thanks to my partner, this
    lack of knowledge was not an issue.

3.  **Feature Toggles**

    The concept of a [Minimal Marketable Feature
    (MMF)](http://www.upstarthq.com/2010/04/introduction-to-minimum-marketable-features-mmf/)
    can be a catch 22 scenario. We want to develop tiny incremental
    features for rapid feedback, yet our customers want feature X in its
    entirety. In order to deliver features in this manner the concept of
    feature toggles are essential. Essentially code which will toggle a
    feature on or off is often deployed with any new features we
    provide. This means if something goes wrong we can instantly disable
    the feature without a new deployment being required. Likewise the
    ability to toggle features enables half finished features to be
    demoed to a customer within a live environment. Once a feature is
    deemed stable, these toggles can be removed.

4.  **Work in Parallel**

    Somewhat tied to feature toggles is the concept of working in
    parallel or being "system green". In other words the mainline trunk
    from which we develop from should be deployable at any time. A
    benefit of working in this manner is if a feature needs disabling
    the old code is always ready to be enabled, likewise if an emergency
    fix needs deploying this can be delivered as soon as possible. There
    are day to day benefits from working in parallel as well. By making
    changes in parallel, at any one time the checked out code is only
    briefly in a state of being un-buildable, if we developed in a big
    bang approach, there could be hundreds upon hundreds of compiler
    errors to wade through. The important concept when working in
    parallel is to ensure the old code which is being extended, or
    replaced is cleared away once the new feature is live. The last
    thing we want is old code rotting with developers too afraid to
    delete it.

5.  **Best Practices**

    It is fair to say that all the developers at Codeweavers want to
    develop the best code they can. Due to this practices such as
    [SOLID](http://en.wikipedia.org/wiki/SOLID_%28object-oriented_design%29)and
    other best practices are discussed, carried out and encouraged.
    While I'd say that via books, the internet and other resources I
    have been exposed to these practices working in a industry scenario
    makes these concepts much more important and realistic. We all know
    what a "perfect" solution would be, however with deadlines and other
    limiting factors sometimes a more pragmatic solution is required,
    despite the inner perfectionists inside us all wanting to spend
    hours refactoring to a better solution.

6.  **Failure**

    There have been times when I have out rightly failed. One of my
    biggest regrets comes from a feature in which I let the database
    schema dictate the business logic. Needless to say as the business
    requirements evolved, the code which was so dependent on how the
    database persisted the data became near impossible to refactor
    without a rewrite. This rewrite never occurred due to deadlines
    meaning the feature had to go live despite myself feeling rather
    ashamed at how badly things had become. Despite this failure, it
    proved to be a huge learning experience and something I do not plan
    on repeating. Every time I have failed, it has helped.

7.  **Starting Again - "a graceful retreat"**

    Prior to Codeweavers had I been stuck on a particular task I would
    have slogged away at it until the problem was resolved. Often this
    would mean fighting my way through a task into the early hours of
    the morning. By applying the principle of a "graceful retreat" I can
    very easily delete code and start fresh. Very quickly you will be
    back where you were before but in a much better condition, having
    learned from past experiences.

8.  **Spike Solutions**

    A [spike
    solution](http://www.extremeprogramming.org/rules/spike.html) is
    essentially a throw away prototype developed before we begin a MMF
    in order to learn more about the problem at hand, or to test various
    solutions. The name refers to the fact that if you were to plot your
    velocity on a graph, after having produced a prototype you should
    have reduced the risk to the project, thus implement the feature for
    real easier and quicker. Every time we have developed a spike
    solution prior to an MMF developers often comments on how it helped,
    either by providing a learning experience or simply enabling the
    feature to be split into further MMF's. It is because of these
    benefits I am becoming to the conclusion that every new feature
    should have a quick spike solution prior to production work
    beginning, after all it is not easy to write tests for code you are
    not quite sure you know how to implement. Spikes enable this
    confusion to be cleared away upfront, allowing the production
    implementation to run smoothly.

9.  **Conferences**

    For the most part I enjoyed university immensely. With regards the
    educational aspects I would find that after an interesting lecture a
    huge sense of motivation and interest within the subject. Spending
    additional time outside of a lecture discussing concepts with others
    was both valuable and fun. Having finished university I am a strong
    believer that I should maintain this inspiration and motivation.
    Thankfully Codeweavers provides the ability to further ourselves,
    and I've been lucky to attend several conferences this past year.

10. **Practice**

    Having experienced one year of Codeweavers the old saying of
    "*Practice practice practice*" still holds true. Whether it be from
    books, conferences or general day to day work. No one can stop
    learning or furthering themselves if they wish to continue day to
    day software development. For this very reason I'm grateful, but
    this rule bears repeating and I look forward to another year of
    practice and improvement.