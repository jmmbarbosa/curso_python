import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()
sql = "Drop Table customers"

mycursor.execute(sql)
print("Tabela excluída com sucesso!")
