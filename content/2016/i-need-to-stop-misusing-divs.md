Title: I Need to Stop Misusing Divs
Date: 2016-07-31 16:25
Author: Shaun Finglas
Tags: CSS, http://schemas.google.com/blogger/2008/kind#post, HTML, miuse
Slug: i-need-to-stop-misusing-divs

I a certainly not a skilled or expert front end developer. While I'm
more than capable of creating pages I lack any design magic to make them
look half decent. Despite this one area where improvement can be made is
in my markup itself.

Over the past few months I've spent most of my time getting to grips
with recent additions and changes in the HTML5 and CSS3 space. During
this one area stood out, my misuse of the division element or
&lt;div&gt;.

Before the addition of the newer elements pages nested with div after
div was normal. However this is no longer the case. From this point
onwards I will be ensuring that every time I introduce a div element I
question whether a more appropriate element should be used.

> The HTML div element (or HTML Document Division Element) is the
> generic container for flow content, which does not inherently
> represent anything. It can be used to group elements for styling
> purposes (using the class or id attributes), or because they share
> attribute values, such as lang. It should be used only when no other
> semantic element (such as article or nav) is appropriate.

#### Semantic Meaning

Two huge side effects that are often overlooked when ignoring semantic
markup is device compatibility with screen readers or other input
methods and future proofing content.

Many people wrongly assume that all users are either keyboard/mouse or
mobile (touch) users. By using semantic elements, users of other input
methods get a much smoother experience. It is possible to jump to
navigation or content without having to page through dozens of unrelated
sections added only for stylistic purposes. Having used such devices
first hand, the joy such simple changes make are outstanding.

Using semantic elements also helps future proof content. Screen scraping
and other technologies can be simplified massively if content is
correctly marked up. The thought that pages of content written now will
still be used and accessible decades from now is incredible.

#### Lessons

The lesson here is an easy one. Every time you write a generic division
element, stop and ask yourself is there an element with more semantic
meaning that will do the same job?

</p>

