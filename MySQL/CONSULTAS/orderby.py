import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()

#sql = "Select * From customers Order By name"
sql = "Select * From customers Order By name desc"

mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
    