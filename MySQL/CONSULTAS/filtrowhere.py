import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()

#sql = "Select * From customers Where address = 'São Paulo, SP'"
sql = "Select * From customers Where address Like '%SP%'"

mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
