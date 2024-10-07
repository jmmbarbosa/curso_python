import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sistema_escolar_soul_on"
)

def excluir():
    mycursor = mydb.cursor()
    sql = "Delete From alunos Where nome = 'José Vinícius'"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "Aluno excluido!")

opcao = input("Deseja excluir o aluno José Vinícius (S/N)? ")
if opcao == 'S':
    excluir()
else:
    print("Aluno José Vinícius não excluido.")
