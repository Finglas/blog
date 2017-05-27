Title: Dont Tie Yourself to a Framework
Date: 2014-07-22 19:19
Author: Shaun Finglas
Tags: http://schemas.google.com/blogger/2008/kind#post, design, hexagonal-architecture
Slug: dont-tie-yourself-to-a-framework

<ul>
<li>
Programming is great

</li>
<li>
Software development is the crap bit. You'll spend more time
configuring, integrating and faffing rather than writing logic most of
the time.

</li>
<li>
Test Driven Development makes development easier as it forces you to
decouple your code.

-   Your core logic should be pure, dependency free C\#, Java, Python
    etc.
-   Your frameworks and libraries should be on the edge of the system.

</li>
<li>
Most people do this for some of their code, e.g. your data access.

</li>
<li>
What about the other parts of a system?

</li>
-   Web frontend
-   REST api's
-   Console applications
-   Desktop clients

<li>
Why should we couple our applications with these layers?

</li>
</ul>
### Hexagonal Architecture

<ul>
<li>
[Hexagonal
Architecture](http://alistair.cockburn.us/Hexagonal+architecture) is a
solution to limit coupling

</li>
<ul>
<li>
Easily switch out your delivery mechanism, e.g. test runner adapter for
testing, HTML adapter for production.

</li>
<li>
[Great
example](http://silkandspinach.net/2005/03/22/the-middle-hexagon-should-be-independent-of-the-adapters/)
from Kevin Rutherford.

</li>
<li>
[Excellent video](https://www.youtube.com/watch?v=WpkDN78P884) by Uncle
Bob though terminology differs.

</li>
<li>
Implementation details should be hidden behind adapters.

</li>
-   Tested manually in the majority of cases
-   Few integration tests for comfort
-   Third party code after all.

<li>
Inner hexagon should only communicate via ports (interfaces) - keeps
domain pure.

</li>
</ul>
</ul>
### Why?

<ul>
<li>
Last few major projects involved with were due to the delivery mechanism
becoming out of date.

</li>
-   Flash to Web
-   Web to Mobile

<li>
Easier to test

</li>
<li>
Easier to change

</li>
</ul>
### Why not?

-   CRUD apps - sometimes it's just CRUD.
-   Lightweight projects might not need hexagonal architecture
-   SOA or Microservices could mean hexagonal architecture actually
    introduces overhead or complexity - judge on context.

</p>

