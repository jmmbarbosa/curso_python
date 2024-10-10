import mysql.connector

def create_database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE sistema_escolar_soul_on")
    print("Database criada com sucesso!")
#create_database()
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sistema_escolar_soul_on"
    )
mycursor = mydb.cursor()

def create_table():
    sql = "CREATE TABLE alunos (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), matricula VARCHAR(50), turma VARCHAR(50))"
    mycursor.execute(sql)
    print("Tabela criada com sucesso!")
#create_table()

def insert_data():
    sql = "INSERT INTO alunos (nome, matricula, turma) VALUES (%s, %s, %s)"
    val = [
        ('José Lima', 'MAT90551', 'BCW22'),
        ('Carlos Augusto', 'MAT90552', 'BCW22'),
        ('Lívia Lima', 'MAT90553', 'BCW22'),
        ('Sandra Gomes', 'MAT90554','BCW23'),
        ('João Augusto', 'MAT90555','BCW23'),
        ('Breno Lima', 'MAT90556','BCW24'),
        ('José Vinícius', 'MAT90557', 'BCW25')
    ]
    mycursor.executemany(sql,val)
    mydb.commit()
    print(mycursor.rowcount, "linha(s) alterada(s)!")
#insert_data()

def select_data():
    #sql = "Select * From alunos Order By matricula"
    #sql = "Select nome, matricula From alunos Where turma = 'BCW23' Order By matricula"
    sql = "Select nome From alunos Where nome Like '%Lima%' Order By matricula"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

#select_data()

def update_data():
    mycursor = mydb.cursor()
    sql = "Update alunos Set turma = 'BCW25' Where id = '2'"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "linha(s) alterada(s)!")

#update_data()

def delete_data():
    sql = "Delete From alunos Where id = '7'"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "linha(s) deletada(s).")

opcao = input("Deseja excluir o aluno José Vinícius (S/N)? ")
if opcao == 'S':
    delete_data()
