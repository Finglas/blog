Title: The N+1 Problem
Date: 2016-02-01
Author: Shaun Finglas
Tags: tutorial
Slug: 2016/02/the-n1-problem

The N+1 problem is when multiple queries are executed against a
persistent store when a reduced amount could serve the same purpose.
This degrades performance, uses more memory and can cause complexity to
be added to the code that processes the results. Most sources of the
problem come from the poor use of ORMs or developers thinking
procedurally instead of in terms of how the underlying database
operates.

#### Example

Consider a collection of posts that each contain zero or more comments.

      Post
        Comment
        Comment
      Post
        Comment
        Comment
        Comment
        Comment
        Comment
      Post

To retrieve a selection of ten posts including their comments, one
option would be to query all posts then perform a query for each
individual posts' comments. This would result in a total of eleven
queries. While this solution works it is far from ideal. Disturbingly
this solution is easily introduced when developers execute queries
against databases using loops or misconfigured ORMs.

#### Solutions

Solutions to solving the N+1 problem are remarkably straightforward. In
the case of manual queries such changes are usually easy to implement.

##### Single Query

Use a join operation to perform a single query. This one query would
pull back all posts and their matching comments. This would be the ideal
fix for the example described above.

##### Query and Stitch

Sometimes there is no clear grouping or relation between sets of data.
This is often the case when normalized data needs to be denormalized
prior to retrieval. In these cases the query and stitch method can be
used.

-   One query to grab master set.
-   Another query to grab the related set.

Then simply match on a key in code. The key would be something that
groups the data and is present in both sets or is the result of
additional programming logic. Query and stitch is useful for paging or
when relational thinking and grouping does not fit. This tends to be the
case for REST APIs where data is aggregated or composed from multiple
sources, or needs further processing after retrieval.

Despite two queries here, it is often possible to return separate
datasets within a single query prior to stitching the data together as a
further optimisation and simplification.

##### ORMs or Tooling

When ORMs are used discovering the N+1 problem is more obscured without
logging the underlying queries that are performed. Once an issue is
discovered it is usually a case of consulting documentation on what the
fix is - often configuration related. Due to this it is worth enabling
logging during development so queries can be analysed.