# dbteste.py

import sqlite3

connection = sqlite3.connect("bdfile.db") # definimos o banco de dados

csr = connection.cursor()

# csr.execute("""CREATE TABLE Pessoa
#                (id integer primary key, nome text)
#             """)

csr.execute("""INSERT INTO Pessoa
               VALUES(1, "Ada")
            """)

csr.execute("""INSERT INTO Pessoa
               VALUES(2, "Bete")
            """)

csr.execute("""INSERT INTO Pessoa
               VALUES(3, "Celso")
            """)            

csr.execute("""INSERT INTO Pessoa
               VALUES(4, "Dario")
            """)            

print csr.execute("""SELECT * FROM Pessoa""").fetchall()

rows = csr.execute("""SELECT * FROM Pessoa WHERE id = 3""")

for row in rows:
    print "id = " + str(row[0])
    print "nome = " + row[1]

