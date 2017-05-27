Title: Dependency Injection (DI) Containers
Date: 2014-11-06 19:07
Author: Shaun Finglas
Tags: DI, http://schemas.google.com/blogger/2008/kind#post, programming, c#
Slug: dependency-injection-di-containers

Strengths
---------

One place for configuration
:   Rather than scattered through out the system. Most DI containers
    have some sort of "module" system where you group associated
    components together.

Scoping
:   Different types of lifestyle can be achieved. Per request, per
    thread, singleton and others. Usually other frameworks have the
    ability to plug into these containers, meaning such features
    integrate nicely.

Feature rich
:   Included along with the basic DI components is usually a large
    amount of additional features which may or may not be needed.

------------------------------------------------------------------------

Weaknesses
----------

Heavyweight
:   Usually in the form of frameworks or libraries. DI is a simple
    concept, but such containers can make getting to grips with it
    tremendously difficult.

Config
:   Configuration can be difficult. Rather than just applying DI you
    need to learn the tooling. XML configuration has widely fell out of
    favour, but even code based configurations can be costly to setup.

Runtime errors
:   Any errors that might have occurred at compile time (in a static
    language) now become runtime errors. Circular references are easily
    introduced if you are not careful. Made a mistake during
    configuration? The system will be out of action. If you're lucky the
    stacktrace can point you in the right direction, but usually these
    are vague and/or confusing.

Magic
:   With the container in charge you lose control of what should be an
    easy part of your development process. The more convention based
    configuration you apply, the more chance things can go wrong. Simple
    changes such as multiple implementations of an interface can prove
    difficult to configure without breaking previous conventions. Much
    of the time adding a new class to the system feels risky - you won't
    know until runtime if you've got it working.

------------------------------------------------------------------------

Alternatives
------------

KISS
:   Keep your dependency wiring at your application root - most likely
    main. This is my preferred, default approach to begin with.

<script src="https://gist.github.com/Finglas/db42de9f16000e638315.js"></script>

KISS - Modules
:   If this configuration starts to get out of hand - use modules. Need
    to modify how the kitchen is built? Just open up KitchenModule.cs.
    With direct access to the references of these dependencies you can
    control scoping. For example you can re-use the same kitchen
    instance between house instances.

<script src="https://gist.github.com/Finglas/f93f595960e8158ba8f2.js"></script>

Refacator
:   As always you can [refactor towards an DI
    container](http://blog.thecodewhisperer.com/2011/12/07/refactor-your-way-to-a-dependency-injection-container/)
    if you feel the need to use one.

</p>

