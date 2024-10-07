import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sistema_escolar_soul_on"
)

mycursor = mydb.cursor()
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
