Title: Do you really need a Microservice?
Date: 2015-06-01
Author: Shaun Finglas
Tags: microservices, retro
Slug: 2015/06/do-you-really-need-microservice

Lately there has been two sets of advice around the use of
Microservices. [Some advise that Microservices should be built after the
fact](http://martinfowler.com/bliki/MonolithFirst.html). [Others advise
the opposite
solution](http://www.martinfowler.com/articles/dont-start-monolith.html).
In conjunction there is a third option that deserves more attention. Do
you even need a Microservice at all? A [recent
tweet](https://twitter.com/natpryce/status/593763168977088513) sparked
off the exact thought I have found myself conveying.

Creating a Microservice is no easy feat. Despite the limited code or
functionality that is involved. There is a whole host of things that
need consideration; source control, project setup, databases, project
conventions, monitoring, logging, deployment, hosting and security to
name a few.

The so called monolith or "application" as it was known before is a
tried and tested way of structuring applications. One of the big
criticisms levelled against monolithic applications is coupling. Having
worked with some terribly coupled applications I agree fully with this
complaint, but there are steps you can take to prevent this.

A whole application does not need to live inside one logical project,
but instead can be split appropriately. In DDD a Bounded Context makes
sense. Using this model you would end up with a Customer and Products
project rather than a single project containing both.

An easy step is the [correct use of namespaces that are structured by
features rather than technology
choices](https://blog.shaunfinglas.co.uk/2014/07/i-need-to-stop-misusing-namespaces.html).

Education is also important, simply put in agreements across teams such
as "*nothing from the customer project will directly reference the
products functionality*". This can be taken a step further by
introducing assertions into the build process that will fail if
"*project A references project B*".

There is no correct answer on whether you should or should not start
with a Microservice architecture. Each team will need to judge and base
their answer on their needs which will most likely vary over time. As it
has been said before - [if you can't structure a monolith what makes you
think you can structure Microservices any
better?](http://www.codingthearchitecture.com/2014/07/06/distributed_big_balls_of_mud.html)