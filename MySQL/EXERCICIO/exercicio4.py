import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sistema_escolar_soul_on"
)

mycursor = mydb.cursor()
#sql = "Select * From alunos Order By matricula"
#sql = "Select nome, matricula From alunos Where turma = 'BCW23' Order By matricula"
sql = "Select nome From alunos Where nome Like '%Lima%' Order By matricula"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
