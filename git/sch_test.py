import pymysql

conn = pymysql.connect(
    host="172.31.38.135",
    user="root",
    passwd="123456",
    database="todo"
)
cur = conn.cursor()

cur.execute("SELECT * FROM assignment")
x = cur.fetchall()

for i in x:
    print(i)
