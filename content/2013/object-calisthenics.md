Title: Object Calisthenics
Date: 2013-01-01
Author: Shaun Finglas
Tags: programming
Slug: 2013/01/object-calisthenics

Recently I ran a session on [Object
Calisthenics](http://www.markhneedham.com/blog/2008/11/06/object-calisthenics-first-thoughts/).
I was first exposed to this challenge a few years ago and personally
found it a fun, yet difficult experience. This is intentional as the
challenge is designed to push the boundaries of best practices. The
instructions are simple, there are nine rules to follow that ***must***
be obeyed during a traditional kata. We chose the [Checkout
Kata](http://codekata.com/kata/kata09-back-to-the-checkout/) as the
backdrop for this session. The teams feedback is as follows.

1.  ### Use only one level of indentation per method

    The team found this easy, and we discussed that following this to
    some degree in day to day development would be beneficial. Limiting
    the amount of nested code you have can improve readability quite
    substantially.

2.  ### Don't use the else keyword

    At first this seemed a no brainier, until people realised it meant
    to favour polymorphism and not simply relying on an early return
    (implicit else).

3.  ### Wrap all primitives and strings

    The team managed well with this, one example would be a pair
    introduced an SKU (Stock Keeping Unit) to encapsulate a string and
    price. We do this well in day to day development at Codeweavers for
    domain objects, however we tend to fail in other areas such as data
    access code. This is one concept we need to try and improve at.

4.  ### Use only one dot per line

    The [Law of Demeter in
    action](http://haacked.com/archive/2009/07/13/law-of-demeter-dot-counting.aspx).
    Once we cleared up the ideas behind this it was pretty easy for the
    teams to follow. This is not a dot counting exercise, so it is worth
    being familiar with the "law". Much of our code would satisfy this
    requirement.

5.  ### Don't abbreviate

    One controversial point that came up from this was regarding the
    team who chose SKU as a class name. Some of the team disagreed with
    this naming, though in terms of the domain (a supermarket) this is a
    perfectly valid name, therefore this did not break the rule. On the
    whole our code is named well, though our legacy codebases have many
    abbreviations that can confuse and obfuscate the intent of the code.

6.  ### Keep all entities small

    For new code, this is not an issue, however we find legacy code is
    given less treatment in regards to the size of our entities. This is
    something we should try to improve, though the teams found this easy
    enough during the kata.

7.  ### Don't use any classes with more than two instance variables

    Personally I find this an odd requirement, providing you keep your
    classes small as per the previous requirement this tends to be a
    less relevant task. Of all the rules to follow, this is the one I
    could not advocate during day to day development providing you keep
    your classes small.

8.  ### Use first-class collections

    My personal favourite of the rules to abide by, and one I have since
    adopted into day to day coding. [First class collections can
    simplify, and make code easier to understand as well as
    maintain](https://blog.shaunfinglas.co.uk/2010/12/lists-or-objects.html)
    and optimize. We have numerous examples of this at play at
    Codeweavers, and we should try to increase the amount of custom
    collections we have, as opposed to relying on primitive collections.
    For example, quotes is a better object than a array of quote.

9.  ### Don't use any getters/setters/properties

    The hardest of all the rules to follow. Most of the teams tried to
    get past this rule by simply naming their getters/setters slightly
    differently. At the end of the day, there were still exposing state
    unnecessarily. We would never try to enforce such a rule for general
    development, but [for core business logic this principle actually
    makes
    sense](https://blog.shaunfinglas.co.uk/2011/04/getters-and-setters-are-evil.html).
    The areas where this falls down, is on the boundary of the system,
    for example user input or output would be such scenarios where
    getters/setters are the easiest, cleanest solutions. Each team found
    this requirement the hardest to work with, which mimics my first
    expose to the object calisthenics challenge.