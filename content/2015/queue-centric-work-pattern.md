Title: Queue Centric Work Pattern
Date: 2015-08-01
Author: Shaun Finglas
Tags: microservices, distributed-systems, SOA
Slug: 2015/08/queue-centric-work-pattern

The [Queue Centric Work Pattern
(QCWP)](http://www.asp.net/aspnet/overview/developing-apps-with-windows-azure/building-real-world-cloud-apps-with-windows-azure/queue-centric-work-pattern)
is simple. Send a message declaring the intent of the command,
acknowledge the message and proceed. All work takes place in a
background process so the user is not kept waiting for the request to
return. Acknowledgement usually takes the form of persistence to ensure
that no messages are lost. Real life examples of the QCWP in action
would be the sending of an email or the confirmation of an order being
accepted from an online retailer.

The QCWP will introduce the concept of [eventual
consistency](https://en.wikipedia.org/wiki/Eventual_consistency), which
surprisingly is not an issue in most cases. The queue itself should be
implemented via some form of message queue that handles some of the more
complicated technical issues regarding message meta data, routing,
persistence and so on. Once a message queue has been chosen the code
required to implement QCWP does not differ to far from simple
request-response examples in terms of both complexity and lines of code.

#### Benefits

##### Reduced Latency

Transferring the message, confirming acknowledgement and returning to
user with some form of confirmation can be very quick. If the process is
long running, it can be vastly quicker to use the QCWP. Even for low
latency scenarios, the use of the QCWP introduces other benefits.

##### Retry

If something fails you can retry the command in a background process.
Nothing is lost when one or more systems are down. If the command fails
consistently, then you can simply notify the user or perform some other
compensating action.

##### Decoupled

If one system is offline the message is just stored and the queue builds
up. Once back online the queue will be emptied. The temporal coupling
between the two systems is now removed. Coupling has been reduced so
much that you can switch consumer with another system and the client
would be unaware as long as the message formats remain the same. This
allows different languages to read and populate the queues.

##### Scaling

To increase throughput you can simple introduce a competing consumer
until the appropriate amount of messages is handled within a SLA
boundary. The inverse is also true. The QCWP allows throttling. Rather
than peak load from web server traffic hitting the back end services,
these can be scaled independently. As the consumer of the messages will
handle each message at its own pace, there is no chance that other
dependencies such as databases would become overwhelmed.

#### Downsides

These benefits don't come for free however. The main issue with the QCWP
is the time it takes to get to grips with this change of conceptual
model. Testing asynchronous code is a lot harder, introducing problems
such as polling shared resources for changes. The very same issue means
simply debugging asynchronous systems can be challenging even with good
monitoring and auditing in place.

#### Conclusion

QCWP was a real change in terms of how I think about two services
communicating. This change in pattern is not hard, merely different.
Once you adjust to the challenges, the benefits enable some truly
resilient systems when communication must occur out of process.