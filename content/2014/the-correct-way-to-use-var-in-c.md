Title: The Correct Way to use var in C#
Date: 2014-02-01
Author: Shaun Finglas
Tags: programming, tutorial
Slug: 2014/02/the-correct-way-to-use-var-in-c

The .NET community is not widely controversial, though there is a strong
topic that appears to come up time and time again when I pair with other
developers - how to use `var` in C\#.

The `var` keyword was introduced in .NET 3.5. Unlike other languages
this is **still a strongly typed declaration**. For example if we
declare a string using `var` then we cannot re-assign this variable to
another type. This would be a compile time error.

There are two parties who have strong feelings about the use of `var`,
both of which are **wrong**.

### Never use var

Some developers suggest the use of `var` be denied. This leads to code
such as the following. **Overly verbose, and in some cases obscuring the
intent of the code**. This can commonly be seen when dealing with
collections or generics.

<script src="https://gist.github.com/Finglas/2050a8b2e6778eb86ebf.js"></script>
### Always use var

Other developers claim you should "*var all the things*". This leads to
code which has the opposite problem from above. **The intent of the code
can be obscured due to not knowing what type you are dealing with**.
This is especially important during code reviews or times when you are
not relying on the IDE's intellisense to remind you what you are dealing
with. After all code is read many more times than it is written.

<script src="https://gist.github.com/Finglas/9f0f755ee0879333b7f2.js"></script>
### Best of both worlds

The solution to this issue is simple. Where the type cannot be inferred
just by looking at the source code (aka the type is on the right), use a
strongly typed declaration. Where the type can be inferred, use implicit
typing. Using the same examples as above, this would look like the
following.

<script src="https://gist.github.com/Finglas/d40dba8264fd0a0a6e04.js"></script>
As with most things when it comes to software development, there is
never a black and white answer. **Always gauge decisions and patterns
based on context**. Just because automated tooling such as the excellent
Resharper suggests you use implicit typing doesn't always make it
correct.

### Bonus

Talking of Resharper, a quick `Alt+Enter` on a type/implicit declaration
will allow you to switch between modes, meaning you can be lazy and have
the IDE pull in the right type when required.