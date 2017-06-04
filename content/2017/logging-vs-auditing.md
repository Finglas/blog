Title: Logging vs Auditing
Date: 2017-05-02
Author: Shaun Finglas
Tags: summary
Slug: 2017/05/logging-vs-auditing

The difference between logging and auditing is a subtle yet important
distinction.

### Logging

-   Technical in nature. Deals with technical concerns, stacktraces or
    errors.
-   Additional levels such as DEBUG, INFO, WARN, ERROR, FATAL for
    classification.
-   Logging can be simple such as traditional stdout statements, or more
    complex with semantic/structured logging.
-   Should not cause a runtime failure if logging is defective, fail
    silently.
-   System should work with or without logging enabled from both a
    technical and system view.
-   No need for automated testing, simply ensure this works afterwards.
    No need for interfaces or abstractions, use the logging library
    directly.

The primary users of logging should be the development team when
developing and testing. Additional the team should use logging for daily
monitoring and support. Effective log monitoring can produce trends or
highlight problem areas well before users report them as issues. The use
of a good monitoring system can also remove and reduce the need for
complex and unstable system tests, this will be the subject of a future
post.

### Auditing

-   Domain specific. Deals with domain concerns for audit trails.
-   Always one level, though context is important. Different audit roles
    for different actions, for example, user makes a payment. User logs
    in. User performs action. All three of these examples are unique and
    should be treated as such.
-   Auditing is important, it must occur. Should cause a runtime failure
    if auditing is defective. Never fail silently.
-   System cannot operate at 100% if auditing is not operating.
-   Testable and should be considered a first class feature.
    Abstractions useful to provide different implementations and to aid
    testing.

Auditing is a feature in itself. There is no point introducing this
additional complexity unless the system requires this. Other concerns
auditing introduces include where to store the data? For how long? And
what potentially sensitive data can be stored?

The key lesson here is that logging and auditing are two very distinct
concepts and should be treated as such.