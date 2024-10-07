import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE sistema_escolar_soul_on")
print("Database criado com sucesso!")
