Title: Project Setup Tax
Date: 2016-04-01
Author: Shaun Finglas
Tags: microservices, retro
Slug: 2016/04/project-setup-tax

With microservices gaining popularity, one consideration prior to
adoption is new project setup. In fact this statement holds true for any
new project that you decide to create.

Each new project requires at a minimum

-   Source control - somewhere to actually store the code.
-   A project base - API, executable, library, application etc.
-   Users, accounts and permissions.
-   Build configuration - in order to compile, package and run tests.
-   Deployment and installation - to a production like environment.

Remember this is all before you write a single line of code.

Automating as much of this away does help. Templates, conventions,
containers or similar can assist. Still nothing is free. This all
requires maintenance regardless of how you choose to optimize the
creation of a new project.

When weighing up decisions about a separate project, always factor in
the project setup tax. In my experience this tends to take longer than
expected. Often it is very easy to forget various project conventions,
configuration options or security concerns.

The lesson here is to never underestimate the time and effort required
in starting a new project. Always allocate more time. Better yet,
[question if the introduction of a new project is even
required](http://blog.shaunfinglas.co.uk/2015/06/do-you-really-need-microservice.html).