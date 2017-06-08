Title: ReactJS and JSHint
Date: 2015-12-01
Author: Shaun Finglas
Tags: programming, tutorial
Slug: 2015/12/reactjs-and-jshint

The [ReactJS Getting Started
Guide](http://facebook.github.io/react/docs/getting-started.html) states
that the recommended way of using React is combined with npm.

This is great but poses a problem when trying to use JSHint. The default
example outputs a single JS file containing both your code and the React
library. The end result is the bundle when linted contains code you
don't and shouldn't need to care about.

The guide does provide a solution, though not as clear as it probably
should be. Offline Transforms. These will transform your jsx files into
plain Javascript without bundling react alongside.

    babel --presets react app.js --out-file main.js

Simply take the result of the transform and perform your linting
process.

    jshint main.js

This may seem obvious but I did lose some time realising the benefit of
offline transforms.

Offline transforms do require that you either bundle the transformed
file with React, or you simply include the standalone JS scripts in your
html. This can be done after the fact. JSHint can then play nicely with
your React apps without the need for other tooling such as wrappers or
text editor extensions.