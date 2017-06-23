Title: DDD - Events
Date: 2016-11-01
Author: Shaun Finglas
Tags: tutorial
Slug: 2016/11/ddd-events

The act of something happening is one of the most crucial aspects of implementing Domain Driven Design (DDD). I missed the importance of domain events when first exploring DDD.

### Why

Most requirements come in the form <q>when something happens, do this</q>. <em>Something</em> in this case would be an action, and *this* would be the result taken afterwards. Most domain events can be discovered when requirements use this sort of language.

Another important consideration is that most requirements are evolutionary. They are often added as the feature is developed. What may start off as a single piece of behaviour, may evolve into something much more complex. Events allow this evolution in a decoupled manner.

### Example

When a blog post is published, update the authors statistics</q>. In code this may have a signature similar to:

<script src="https://gist.github.com/Finglas/514772dbb07895410be283fa71067b97.js"></script>

The publish method is responsible for the publishing of the post. This entity holds responsibility for the pre-conditions and post conditions of such action. Also the method takes a domain service that will update the authors statistics as this is not the responsibility of the `Post` entity itself.

A new requirement may be to automatically send out a tweet with the post title and description. Without events this could be added in a similar manner.

<script src="https://gist.github.com/Finglas/ad891cd9cb64cae26f18470bd15b7e6e.js"></script>

Again the service will do the right thing once invoked, in this case send a tweet out. As you can see we could repeat this sort of enhancement over and over. While this does indeed complete the functionality that the business requires, the solution is far from elegant. A much better solution is to rely upon domain events.

### Solution

<script src="https://gist.github.com/Finglas/8b5bd981aa9e0ba33ae041122a6a448b.js"></script>

The difference here is the publish method does nothing other than its internal logic. However it does publish (raise) an event to indicate a post has been published. Subscribers (listeners) to this event can then perform their corresponding actions.

Using the previous example two subscribers would be configured to send tweets and update author statistics. Each of these subscribers (handlers) would run in process by default, so their internal implementation should be as simple as possible. In other words record the request, and process this in the background. <a href="http://udidahan.com/2009/06/14/domain-events-salvation/">The code to raise the event is relatively simple</a>, and can simply forward to any registered subscribers based upon a type. Any failure should not cause the publish to fail. Alternatively external subscribers could also handle this event, though this implementation would require the use of resilient and durable storage such as message queues or databases.

Ultimately domain events allow for extremely loosely coupled code, that is open for extension. Each handler can be developed and tested in isolation. The use of composition means that new features should become easy additions, with low risk.

One aspect that may stand out is that the use of this pattern uses a static class to publish events. While in most cases this would be poor for testing, this is not the case here. For tests prior to each step executing you can simply clear any registered handlers and configure what is required. If no handlers are configured, then nothing occurs. Also test handlers that simply report that fact a message has been raised are more than adequate.

### Downsides

While this refactored example is loosely coupled, and open for extension, the intent of what happens after a publish is somewhat lost. Before it was clearer to see what the <code>Publish</code> method would do. This is a trade off, though the pros outweigh the cons here. Most IDE's have a way of showing you the use of all types, so we could easily see any handlers that consume the `PostPublishedEvent`.

Even with IDE/editor support, the loosely coupled nature of Domain Events can be tricky to debug at runtime. For example I once accidentally configured a game engine to handle events triggered from player movement. This meant that each frame of the game executed the collision detection algorithm twice, instead of once. Without a clear audit of what handlers are being executed upon what events, the use of domain events can be tricky to debug.

### Lessons

- Domain Events are a key area of DDD.
- Use events to write loosely coupled code.
- Ensure you have a method of auditing with handlers respond to which events.