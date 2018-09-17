# "Database code" for the newsdata logs analysis.

import psycopg2

DBNAME = "news"

def get_log_data(strQuery):
    db = psycopg2.connect(database=DBNAME)
    c=db.cursor()
    c.execute(strQuery)
    strReturn = c.fetchall()
    db.close()
    return strReturn
