Title: Consistency
Date: 2015-02-01
Author: Shaun Finglas
Tags: retro
Slug: 2015/02/consistency

Striving for consistency within a codebase is a **good thing**. I'm very
much someone who believes in applying a consistent formatting style,
patterns and practices. However there are two sides to this view.

One colleague used to hate different apps that used different
frameworks, styles and conventions. This is a fair point, it made
switching between them harder. In their eyes, a change to the
development process should cascade across all applications.

Another colleague used to state that without breaking consistency then
improvements and progress would never happen. An equally fair point.
However this lead to scenarios where some of the code would be in
differing states of consistency, or improvements were avoided because
they were too large to implement safely.

Like most things in software development, there is **rarely a true
answer**. The best of both worlds is to apply both concepts at varying
levels.

Applying consistency at package/assembly/module/namespace level works
well from my experience. **Different boundaries can have different
consistency rules**.

This approach allows incremental evolution, but still keeps consistency
within a boundary. This enables both benefits of favouring consistency,
while still allowing the code to evolve over time.
[Ratcheting](http://blog.shaunfinglas.co.uk/2014/11/ratcheting.html) can
be used to ensure future work is aligned consistently. Rather than big
bang implementation, you can perform larger, long term changes steadily.

Remember; software development is like gardening, it takes time to see
the results sometimes and blindly applying a coding convention to
conform to consistency requires thought.