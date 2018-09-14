# News Article Logs Analysis

## Overview
This analytical tool is designed to analyze log data from a news site, specifically, extrapolating user and reader data, as well as identifying errors.

## _Questions_
This analytical tool is designed to answer the following questions:

1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.


2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)

## _Database Views_
This analysis application leverages the following database views to more easily aggregate and present the data in question:

### _View 1_

CREATE VIEW QUERY:
```
CREATE VIEW vw1 as SELECT .....
```

### _View 2_

QUERY:
```
CREATE VIEW vw2 as SELECT .....
```
