import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()
sql = "Update customers Set address = 'Manaus, AM' Where address = 'Palmas, TO'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "linha(s) afetada(s).")
