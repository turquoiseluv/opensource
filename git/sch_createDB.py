import pymysql

mydb = pymysql.connect(
    host="172.31.38.135",
    user="root",
    passwd="123456",
    port=3306,
    database="todo"
)
mycursor = mydb.cursor()



# mycursor.execute("CREATE DATABASE todo")



mycursor.execute("CREATE TABLE user (userCount INT AUTO_INCREMENT PRIMARY KEY, userId TEXT, userPw TEXT, userMaj TEXT, userGrd INT)")

mycursor.execute("CREATE TABLE keyword (userId TEXT, keyW TEXT)")
mycursor.execute("CREATE TABLE course (userId TEXT, crsName TEXT, crsNum TEXT)")
mycursor.execute("CREATE TABLE schedule (type TEXT, sort TEXT, userId TEXT, userMaj TEXT, crsNum TEXT, contents TEXT, deadline TEXT, sharing BOOLEAN, likes INT)")

mycursor.execute("CREATE TABLE article (type TEXT, userId TEXT, contents TEXT, viewCnt INT, srcUrl TEXT)")
mycursor.execute("CREATE TABLE assignment (type TEXT, crsName TEXT, contents TEXT, deadline TEXT)")
mycursor.execute("CREATE TABLE notice (type TEXT, crsName TEXT, contents TEXT, deadline TEXT)")
mycursor.execute("CREATE TABLE material (type TEXT, crsName TEXT, contents TEXT, deadline TEXT)")



# mycursor.execute("SHOW DATABASES")
# x = mycursor
# for i in x:
# 	print(i)

# mycursor.execute("SHOW TABLES")
# x = mycursor
# for i in x:
# 	print(i)

# # mycursor.execute("SELECT * FROM schedule")
# # result = mycursor.fetchall()
# # for i in result:
# #     print(i)

# mycursor.execute("SELECT * FROM assignment")
# result = mycursor.fetchall()
# for i in result:
#     print(i)
