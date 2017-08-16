Title: Code Smell: Time Span Embedded in Variable
Date: 2017-08-08
Author: Shaun Finglas
Tags: code, tutorial
Slug: 2017/01/code-smell-time-span-embedded-in-variable

A common code smell that tends to go unnoticed is embedding a time span within a variable name. While developers recognize that embedding types into names is redundant they often fail to see this smell.

You often need a variable to trigger on a set period, such as every fifteen minutes. For example:

    BlogPostFeedPollingIntervalInSeconds = 900

In this example, what is 900? Without the variable name this is hard to reason about. This is even harder when the value is external and replaced on deployment. Often the value will be found with a comment explaining what the figure is relative to other time periods. This is another hint that you have a time span embedded into a variable.

This smell also becomes harder for more exotic or unfamiliar intervals. In other words most developers are familiar that 1 second in milliseconds is 1000, but not other common ranges or periods. Most standard libraries or lower level functions have fixed intervals which compound the problem. For example a data access libraries tend to use seconds as their highest unit of time, this may not be appropriate in some cases.

## Solution

The fix for this code smell is to use time spans. The previous example can be expressed in the following form.

    BlogPostFeedPollingInterval = "00:15:00"

The value here is expressed in the form HH:MM:SS. Time spans can include days or levels of precision lower than a single second. Different languages may have alternative forms of specifying time spans but the principle is the same. Consult the documentation for more info. When the code reads this value the string time span will be converted. Using C# as an example:

    var blogPostFeedPollingInterval = TimeSpan.Parse(timeSpan);

The use of time spans have a variety of benefits. Notice that the variable name has had the time component removed. This allows the value to increase or decrease without needing to change the variable name.

Additionally time spans are human readably without the need to convert or do maths in your head.

Time spans also offer type safety if the underlying code is doing further work with the value. This is in stark
contrast to doing numerical work with simple integers. Another example would include the ability to use higher time periods for clarity and then simply convert to the total number of minutes/seconds when required.

It is worth bearing in mind that for time periods such as "12 months" or "every 3 weeks on Friday" an alternative is required. Some languages may offer this by default, others may require a third party library. This is due to the fact that a time span does not respect the calendar system. For example, over several months the number of days in each month can vary. For days, hours, minutes or seconds your standard libraries time span should be more than capable.

#### Lessons

- Don't embed time spans in variables.
- Whenever you include a time span in a variable name consider using a time span.
- Check the documentation for your language as time span formats can differ or be tricky to remember.
- For periods of time (every 3 months on the 1st) time spans are not appropriate by default.
- For business rules that must trigger on on particular dates as previously use the calendar to work this out.