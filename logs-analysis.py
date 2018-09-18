
from dbconn import get_log_data

# Parse Date Strings into long Dates (e.g., 2017-12-01 to December 1, 2017)


def parse_date_string(strDateIn):
    strYear = strDateIn[:4]
    strDay = strDateIn[-2:]
    # strMonth = strDateIn[5:-3]

    if strDateIn[5:-3] == "01":
        strMonth = "January"
    elif strDateIn[5:-3] == "02":
        strMonth = "February"
    elif strDateIn[5:-3] == "03":
        strMonth = "March"
    elif strDateIn[5:-3] == "04":
        strMonth = "April"
    elif strDateIn[5:-3] == "05":
        strMonth = "May"
    elif strDateIn[5:-3] == "06":
        strMonth = "June"
    elif strDateIn[5:-3] == "07":
        strMonth = "July"
    elif strDateIn[5:-3] == "08":
        strMonth = "August"
    elif strDateIn[5:-3] == "09":
        strMonth = "September"
    elif strDateIn[5:-3] == "10":
        strMonth = "October"
    elif strDateIn[5:-3] == "11":
        strMonth = "November"
    else:
        strMonth = "December"

    strDateOut = strMonth + " " + strDay + ", " + strYear
    return strDateOut


# *****************************************************************************
# ***Question #1 Below***
# *****************************************************************************
strSQLIn = "Select articles.title, COUNT(log.id) as ArticleCount "
strSQLIn = strSQLIn + \
    " FROM log LEFT OUTER JOIN articles on replace(path, '/article/','') = articles.slug "
strSQLIn = strSQLIn + \
    " GROUP BY articles.title, log.path HAVING log.path like '/article/%' "
strSQLIn = strSQLIn + " ORDER BY ArticleCount DESC limit 3;"

aryResults = get_log_data(strSQLIn)
print("1. What are the most popular three articles of all time? Which articles have been accessed the most?")

print("")

for i in range(len(aryResults)):
    strResult = ""
    num = 0
    for j in range(len(aryResults[i])):
        if num == 0:
            num += 1
            strResult = "- \"" + str(aryResults[i][j]) + "\""
        else:
            num += 1

            strCurrent = str("{:,}".format(aryResults[i][j]))
            strResult = strResult + " -- " + strCurrent + " Views"

    print(strResult)

print("")
print("")

# *****************************************************************************
# ***Question #2 Below***
# *****************************************************************************

# ****Query below is just a placeholder. Needs to be updated to correct query!
strSQLIn = "SELECT authors.name, COUNT(log.id) as ArticleCount FROM log "
strSQLIn = strSQLIn + \
    " INNER JOIN articles on replace(path, '/article/','') = articles.slug "
strSQLIn = strSQLIn + " INNER JOIN authors on articles.author = authors.id "
strSQLIn = strSQLIn + " GROUP BY authors.name ORDER BY ArticleCount DESC;"

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

# *****************************************************************************
# ***Question #3 Below***
# *****************************************************************************

# ****Query below is just a placeholder. Needs to be updated to correct query!
strSQLIn = "SELECT L1.time::timestamp::date as LogDate, "
strSQLIn = strSQLIn + \
    " ROUND((cast(ErrorCount as numeric)/TotalCount)*100,2) FROM "
strSQLIn = strSQLIn + \
    "     (SELECT time::timestamp::date, Count(id) as TotalCount "
strSQLIn = strSQLIn + "     FROM log group by time::timestamp::date) L1 "
strSQLIn = strSQLIn + " INNER JOIN "
strSQLIn = strSQLIn + \
    "     (SELECT time::timestamp::date, count(id) as ErrorCount "
strSQLIn = strSQLIn + \
    "     FROM log GROUP BY time::timestamp::date, log.status "
strSQLIn = strSQLIn + "     HAVING log.status = '404 NOT FOUND') L2 on "
strSQLIn = strSQLIn + \
    " (L1.time::timestamp::date = L2.time::timestamp::date) "
strSQLIn = strSQLIn + \
    " WHERE cast(ErrorCount as numeric)/TotalCount > .01;"

aryResults = get_log_data(strSQLIn)

print("3. On which days did more than 1 percent of requests lead to errors?")
print("")

for i in range(len(aryResults)):
    strResult = ""
    num = 0
    for j in range(len(aryResults[i])):
        if num == 0:
            num += 1
            strResult = "- " + \
                parse_date_string(str(aryResults[i][j]))
        else:
            num += 1
            strCurrent = str(aryResults[i][j])
            strResult = strResult + " -- " + strCurrent + "% Errors"

    print(strResult)

print("")
