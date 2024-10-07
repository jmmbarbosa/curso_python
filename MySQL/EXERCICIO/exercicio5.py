import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sistema_escolar_soul_on"
)

mycursor = mydb.cursor()
sql = "Update alunos Set turma = 'BCW25' Where nome = 'Carlos Augusto'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "linha(s) alterada(s)!")
