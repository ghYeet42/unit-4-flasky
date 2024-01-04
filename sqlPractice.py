import pymysql
import pymysql.cursors
from pprint import pprint as print


con = pymysql.connect(
    database = "world",
    user = "cscarlett",
    password = "228941274",
    host = "10.100.33.60",
    cursorclass = pymysql.cursors.DictCursor
)

cursor = con.cursor()

cursor.execute("SELECT `Name`, `HeadOfState` FROM `country`")

results = cursor.fetchall()

print(results)

print(results[0])

print(results[0]["HeadOfState"])

print(results[0]["HeadOfState"])

for allHeadNames in results:
    print(allHeadNames["HeadOfState"])