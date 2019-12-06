Title: Testing your Composition Root
Date: 2017-06-27
Author: Shaun Finglas
Tags: tutorial, testing
Slug: 2017/06/testing-your-composition-root

Separating configuration from your code itself is a good practice. Unfortunately this can quite be
quite complex in itself. In fact it is fair to say that in many cases the use of
[DI containers](/2014/11/dependency-injection-di-containers.html) to achieve this can be overkill
for a task that should be rather basic.

Recently a project I've been involved with has struggled with the configuration of dependencies.
This lead to the dreaded runtime error, even though at compile time everything was seemingly
normal. This late feedback was compounded by the fact that getting the system up and running
locally is a chore, so in many cases it was CI that was detecting these issues after a deploy.

## Solution

The general practice states that your tests shouldn't need to use your production configuration.
However in this case the solution was to invoke the configuration and force it to resolve. This
test was odd in the sense that it does nothing other than successfully resolve. The fact that no
unhandled exception is thrown is good enough. Note there is only one new test here, all other unit
tests remain as-is, they are still separate from the use of the production configuration. All
this test does is ensure all wiring up and dependencies are satisfied. In cases where config
from an external file is used, that too will be exercised.

## Example

    [Test]
    public void ConfigurationTest()
    {
        var container = Container.Resolve();
        container.Resolve<RootType>();
    }

The actual resolution aspect on line 5 is optional. There may be other ways to force resolution,
this may vary based on what library you use. In this example only one type is resolved. If your
project includes multiple entry points such as numerous controllers you may need to include these
as well.

Hopefully the error that is thrown when this resolution fails is useful. Most DI libraries are
fairly good in this regard. Even so it may be worth documenting this test with the steps that
a developer would have to go through in order to fix.

## Dynamic Languages

Even though DI libraries are a rare thing in dynamic languages, the use of a composition root
is still needed. Therefore I'd recommend a similar test be applied to dynamic languages to keep
the feedback loop fast.

## Lessons

- Don't test your composition root in your current unit tests.
- Do include a single test that resolves your root dependencies.
- Include appropriate messaging to show how to fix the issue.
- Dynamic languages should aim to test their composition root can resolve also.