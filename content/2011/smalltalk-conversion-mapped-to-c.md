Title: Smalltalk Conversion mapped to C#
Date: 2011-10-01
Author: Shaun Finglas
Tags: programming
Slug: 2011/10/smalltalk-conversion-mapped-to-c

Lately the team has been making some rather drastic changes and
re-designs to our codebase in an attempt to minimise friction to change.
In other words, we've identified areas that are painful or tedious to
work in and have hopefully rectified them by re-writing the code. The
proof of this should be felt as we begin adding new features, the newly
improved code is certainly faster and more optimised.

Regardless, one area that remains troublesome in my opinion is object
mapping (or the correct term of conversion) code. While I've not
personally been involved with this reworking of the codebase, I have
recently just finished reading Kent Beck's - [Smalltalk Best Practice
Patterns](http://www.amazon.co.uk/Smalltalk-Best-Practice-Patterns-Kent/dp/013476904X).
Many of the developers I follow on Twitter have been blogging about this
book and I figured it was time to give it a go. After all it gets
massive praise whether or not you use
[Smalltalk](http://en.wikipedia.org/wiki/Smalltalk). While reading this
book a few key points regarding object conversion are discussed and I
found them incredibly relevant.

So should you read the book? I would say yes. I don't program in
Smalltalk. I don't plan on programming Smalltalk. Nor had I read a line
of Smalltalk before. But you should still read this book. The first half
is incredibly relevant to any OO programming language. Granted I found
the second half is less useful, but the gems I've picked up in the first
half more than make up for this. In fact, pages 28 to 30 are so good I
figured it would be worth sharing.

I've been convinced for a while that creating separate objects to
convert objects is unnecessary, and in fact adds to the amount of code
you need to write and maintain, thus increasing resistance for change.
So if we remove this unecesary, intermediate object, how do we create a
new object from another object? The answer is conversion. This answer
strangely comes from a book all about Smalltalk. The answer also
strangely comes from a book over ten years old. Pages 28 - 30 cover the
topic of conversion. The following is quoted heavily from the book, but
I recommend reading the pages in full.

### **Conversion**

> **Question** - How do you convert information from one object's format
> to another's?

> **Answer** - Convert from one object to another rather than overwhelm
> any one object's protocol.

What this is getting at is we could using [C\#
extension](http://msdn.microsoft.com/en-us/library/bb383977.aspx)
methods do the following to the String class.

<script src="https://gist.github.com/Finglas/1eb9482e9dfff30922bb.js"></script>
This would be abusing the String class. If we want a postcode from a
string, we should have the Postcode object create us a Postcode from a
string, not the other way around. There could be hundreds of conversions
from strings to a new object, but we would violate the string class if
we did this. In turn, Kent goes on to say "*Conversions that return
similar responsibilities should use a Convert Method. To convert to an
object with different protocol use a Converter Constructor Method*".

### **Converter Method**

> **Question** - How do you represent simple conversion of an object to
> another object with the same protocol but different format?

> **Answer** - Provide a method in the object to be converted that
> converts to the new object. Name the method by pre-appending "as" to
> the class of the object returned.

In C\# this would be:

<script src="https://gist.github.com/Finglas/9c14d32dbf69e57f2ba0.js"></script>
In C\# the convention is to use `To` rather than `As` for converter
methods. For example we could do quotes.ToArray() on a List of Quotes.
We still have the same protocol, a collection of quotes, we are just
storing them in a different format. The rule for adding such methods is
that there should only be one sensible way to perform this conversion,
and the source and destination share the same protocol.

### **Converter Constructor Method**

> **Question** - How do you represent the conversion of an object to
> another with different protocol?

> **Answer** - Make a constructor method that takes the object to be
> converted as an argument

<script src="https://gist.github.com/Finglas/f5445a00b9bf8e8e14d0.js"></script>
In our codebase we have a `RegistrationDate `object. We have a
constructor that takes a string representation of the date (from the
outside world) and constructs a `RegistrationDate `. This very same
principle can be applied to other, more complex objects. For example
consider an active record style approach below. Here
`QuoteRecord `represents our database object, with `Quote `representing
a domain object. The following would be the converter constructor
method. In other words, we create (or convert) our quote from the quote
record. No separate mapper. No intermediate object. Less resistance for
change.

<script src="https://gist.github.com/Finglas/46bc94e12209385fc9ff.js"></script>
The benefit here is that we have minimised friction. If the requirements
for this code changes we will need up to update at worst, the record and
the domain object. Had we used a separate object to perform the mapping
we would end up with a third place to maintain if we decided to add a
new property to our `QuoteRecord`.

I'll admit to having only used this technique for a week or so, though
so far it has worked a treat and I expect it to continue working
considering these techniques have stood the test of time.