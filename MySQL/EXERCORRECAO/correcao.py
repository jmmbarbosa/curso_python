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
create_table()

