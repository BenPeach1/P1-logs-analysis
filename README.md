# News Article Logs Analysis

## Overview
This analytical tool is designed to analyze log data from a news site, specifically, extrapolating user and reader data, as well as identifying errors.


## Running the application
This logs analysis application can be run from the command line by changing to the corresponding directory ("P1-logs-analysis") and running the ```python3 logs-analysis.py``` command.

This application runs queries against the 'news' psql database. In order to run this application, you will
need to download the newsdata.sql file and import it via the following command: ```psql -d news -f newsdata.sql```.


## _Questions_
This analytical tool is designed to answer the following questions:

1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.


2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)

## _Database Views & Queries_
This analysis application does not leverage any database views. Instead, each analysis question is answered with a single SQL query. See the queries for each analysis question below:

### _QUERY: Question 1_

```
SELECT articles.title, COUNT(log.id) as ArticleCount
FROM log LEFT OUTER JOIN articles on replace(path, '/article/','') = articles.slug
GROUP BY articles.title, log.path
HAVING log.path like '/article/%'
ORDER BY ArticleCount DESC limit 3;
```

### _QUERY: Question 2_

```
SELECT authors.name, COUNT(log.id) as ArticleCount
FROM log INNER JOIN articles on replace(path, '/article/','') = articles.slug
INNER JOIN authors on articles.author = authors.id
GROUP BY authors.name
ORDER BY ArticleCount DESC;
```

### _QUERY: Question 3_

```
SELECT L1.time::timestamp::date as LogDate, ROUND((cast(ErrorCount as numeric)/TotalCount)*100,2)
FROM (SELECT time::timestamp::date, Count(id) as TotalCount
      FROM log group by time::timestamp::date) L1
INNER JOIN (SELECT time::timestamp::date, count(id) as ErrorCount
      FROM log GROUP BY time::timestamp::date, log.status
      HAVING log.status = '404 NOT FOUND') L2
ON (L1.time::timestamp::date = L2.time::timestamp::date)
WHERE cast(ErrorCount as numeric)/TotalCount > .01;
```
