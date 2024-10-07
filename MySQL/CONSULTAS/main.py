import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()
mycursor.execute("Select * From customers")
'''
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
'''
myresult = mycursor.fetchone()
print(myresult)
