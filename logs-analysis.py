
from dbconn import get_log_data


##*****************************************************************************
##***Question #1 Below***
##*****************************************************************************
strSQLIn = "Select articles.title, COUNT(log.id) as ArticleCount from log left outer join articles on replace(path, '/article/','') = articles.slug GROUP BY articles.title, log.path HAVING log.path like '/article/%' ORDER BY ArticleCount DESC limit 3;"

aryResults = get_log_data(strSQLIn)
print("1. What are the most popular three articles of all time? Which articles have been accessed the most?")

print("")

for i in range(len(aryResults)):
    strResult = ""
    num = 0
    for j in range(len(aryResults[i])):
        if num == 0:
            num += 1
            strResult = "- " + str(aryResults[i][j])
        else:
            num += 1

            strCurrent = str("{:,}".format(aryResults[i][j]))
            strResult = strResult + " -- " + strCurrent + " Views"

    print(strResult)

print("")
print("")

##*****************************************************************************
##***Question #2 Below***
##*****************************************************************************

##****Query below is just a placeholder. Needs to be updated to correct query!
strSQLIn = "Select articles.title, COUNT(log.id) as ArticleCount from log left outer join articles on replace(path, '/article/','') = articles.slug GROUP BY articles.title, log.path HAVING log.path like '/article/%' ORDER BY ArticleCount DESC limit 3;"

aryResults = get_log_data(strSQLIn)

print("2. Who are the most popular article authors of all time?")
print("")

for i in range(len(aryResults)):
    strResult = ""
    num = 0
    for j in range(len(aryResults[i])):
        if num == 0:
            num += 1
            strResult = "- " + str(aryResults[i][j])
        else:
            num += 1
            strCurrent = str("{:,}".format(aryResults[i][j]))
            #strCurrent = str(aryResults[i][j])
            strResult = strResult + " -- " + strCurrent + " Views"

    print(strResult)

print("")
print("")

##*****************************************************************************
##***Question #3 Below***
##*****************************************************************************

##****Query below is just a placeholder. Needs to be updated to correct query!
strSQLIn = "Select articles.title, COUNT(log.id) as ArticleCount from log left outer join articles on replace(path, '/article/','') = articles.slug GROUP BY articles.title, log.path HAVING log.path like '/article/%' ORDER BY ArticleCount DESC limit 3;"

aryResults = get_log_data(strSQLIn)

print("3. On which days did more than 1 percent of requests lead to errors?")
print("")

for i in range(len(aryResults)):
    strResult = ""
    num = 0
    for j in range(len(aryResults[i])):
        if num == 0:
            num += 1
            strResult = "- " + str(aryResults[i][j])
        else:
            num += 1
            strCurrent = str(aryResults[i][j])
            strResult = strResult + " -- " + strCurrent + "% Errors"

    print(strResult)
