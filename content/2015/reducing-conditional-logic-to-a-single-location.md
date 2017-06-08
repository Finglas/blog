Title: Reducing Conditional Logic to a Single Location
Date: 2015-12-01
Author: Shaun Finglas
Tags: programming, tutorial
Slug: 2015/12/reducing-conditional-logic-to-single

[My Anti If Campaign
post](http://blog.shaunfinglas.co.uk/2013/05/the-anti-if-campaign.html)
still generates a lot of questions and discussion. In summary:

-   Conditional statements are not bad. They are a core programming
    construct.
-   If you are working in an OO language, type checks are probably not
    the best solution to your problem. Rely on polymorphism.
-   You need to perform conditional checks somewhere. In my first
    example the conditional check was pushed into routing. The
    conditional statement in this case had been offloaded to the
    consumer.

A recent real world example was refactored which highlighted the points
previously, but inverts the problem and solution. How do you remove
conditional statements if your system itself has to make the decisions
internally?

#### Example

The simplified example shows the result of invoking a third party
service. This result contained a flag indicating either success or
failure. Effectively there were two hidden types here. Finally the
result was returned based on the HTTP status code.

<script src="https://gist.github.com/Finglas/9c27094d9728ec85a6f7.js"></script>
After the result of the third party call, the domain would decide how to
respond.

<script src="https://gist.github.com/Finglas/6f11ea92b82c82a032e3.js"></script>
Both the client and the domain logic was split over multiple source
files. This made noticing the duplication tricky. Both the client and
the domain also knew the fact that the result of the third party call
can succeed or fail.

Sadly the domain violates the SRP at a method level. While not a
requirement yet, if further status codes are required or the contents of
responses controlled flow, we are in trouble. The type flag would need
to evolve from a boolean to something more complex. The contents of the
responses may also need to be provided. This solution could leak HTTP
details down into the domain unless careful.

#### Solution

Recognise the boolean flag is actually hidden two types. Remove the flag
and introduce a concrete type for each path. Each concrete type performs
the right operation. In this case executing the relevant methods within
the domain.

<script src="https://gist.github.com/Finglas/997b68262b19b4d73912.js"></script>
Each concrete type is easy to test, change or throw away. In this
example an interface is provided. This contains just the necessary
methods that the process requires. The domain is now simplified. The
domain instance itself is simply provided as an argument. The concrete
instance of each result will perform the right operation.

<script src="https://gist.github.com/Finglas/03e2b8b6f3ada56479ad.js"></script>
#### Benefits

-   Now possible to add and remove additional redemption handling
    easily.
-   The procedural code remains on the boundary of the system. There is
    no need to try an use OO concepts here. Keep it simple.
-   The domain becomes flexible and removes the procedural checks. OO
    concepts can be applied as much as you like here.
-   The redemption service works with anything that can play the role of
    a redeemer. Open to refactoring.

#### Closing

Stick the procedural code on the edge of your system and be done with
it. Just ensure that you only perform such checks once.

Just because you are not performing explicit type checks, the use of
boolean flags usually indicates at least two hidden types.

The anti if campaign is not the removal of all conditional checks. They
need to happen somewhere. Just try to limit them.