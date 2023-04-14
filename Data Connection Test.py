import mysql.connector
connection = mysql.connector.connect(user = 'root', database = 'example', password = 'R3tsq127!%tg')
cursor = connection.cursor()
testQuery = ("SELECT * FROM student")
cursor.execute(testQuery)
for item in cursor:
    print(item)
cursor.close()
connection.close()