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
insert_data()
