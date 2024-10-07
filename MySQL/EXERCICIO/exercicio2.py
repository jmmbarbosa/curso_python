import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sistema_escolar_soul_on"
)

mycursor = mydb.cursor()
sql = "CREATE TABLE alunos (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), matricula VARCHAR(10), turma VARCHAR(10))"
mycursor.execute(sql)
print("Tabela criada com sucesso!")
