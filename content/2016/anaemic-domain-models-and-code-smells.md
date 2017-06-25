Title: Anaemic Domain Models and Code Smells
Date: 2016-07-01
Author: Shaun Finglas
Tags: programming
Slug: 2016/07/anaemic-domain-models-and-code-smells

An anaemic domain model (ADM) is considered a code smell in many cases.
An ADM is present when you have a entity representing your domain, but
void of any behaviour. Any logic is separate and operated upon in
isolation. Such domain models can be thought of as simple property bags,
plain old language objects or DTO's.

#### Code Smells

With an ADM your behaviour ends up split across many domain services
instead of being grouped with the data it operates upon.

As the domain and your understanding evolves, the problem an ADM
introduces can get worse as more and more domain services are added.

A complex domain or one that evolves will end up paying a price.
Converting to and from what looks like a domain model, only to perform
domain logic separately is quite redundant. Why not ditch the domain
model altogether? If you have a simple problem, a simple solution such
as a transaction script may very well do the job.

#### Simple Problems - Simple Solutions

Sometimes you don't have a complex domain. Input, basic logic, then some
form of CRUD is incredibly common. Due to this it is easy to see why
anaemic models exist.

Rather than the cost associated with attempting to model the domain,
choose easier solutions such as transaction scripts, table gateways or
similar.

The big argument for anaemic domain models is following the SRP. Adding
behaviour to domain models does not violate SRP. There is no reason why
such additions cannot be formed from composition or delegation. Likewise
the internal representation can be private. On the flip side domain
services operating under the disguise of SRP lack cohesion, despite
*doing one thing*.

The good news is that the ADM is very easy to extend and refactor at a
later point. [Moving to a richer domain model is not
difficult](https://vimeo.com/43598193), though the process may take
time.

#### Refactoring from an ADM

Simply push behaviour onto entities, one method at a time. As you do
this, services will begin to dissolve. All of this can be done when
supported by a good suite of tests.

An [equally simple step is to being introducing value
types](https://blog.shaunfinglas.co.uk/2015/02/value-object-refactoring.html).
Over time these will act as code magnets pulling any related behaviour
towards them.

#### Lessons

-   In most cases an ADM is a code smell.
-   There may be easier solutions than a anaemic model that mimics your
    domain.
-   The ADM is not a good example of SRP.
-   Refactoring towards a rich domain model is easy and achievable at
    any stage.