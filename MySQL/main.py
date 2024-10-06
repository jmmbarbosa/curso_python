import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE mydatabase")
#print("Database criado com sucesso!")

#mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
#print("Tabela criada com sucesso!")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
#val = ("José Milton", "Av. Jorge Montenegro Barros, 3230, Sta Amelia, Maceió-AL, 57063-000")
#mycursor.execute(sql, val)
val = [
    ('Pedro', 'São Paulo, SP'),
    ('Ana Maria', 'Vitória, ES'),
    ('Débora', 'Palmas, TO'),
    ('Clara', 'São Bernardo, SP'),
    ('Sandy', 'Ubajara, CE')
]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount, "linha(s) alterada(s)!")
