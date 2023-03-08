# _*_ coding: utf-8 _*_

# dbteste.py

import sqlite3

connection = sqlite3.connect("bdlivraria.db") # definimos o banco de dados Livraria

csr = connection.cursor()

#Criação de Tabelas
def create_tables():
    csr.execute("""CREATE TABLE IF NOT EXISTS Cliente
               (codigo integer primary key, telefone text, endereco text,
                cpf text, tipo text)
                """)

    csr.execute("""CREATE TABLE IF NOT EXISTS Livro
               (isbn integer primary key, qtde integer, assunto text, Autor text,
                codigoeditora integer)
                """)

#inclusao de clientes
def insert_Cliente(codigo, telefone, endereco, cpf, tipo):
    csr.execute("""INSERT INTO Cliente VALUES(?,?,?,?,?)""", 
                   (codigo, telefone, endereco, cpf, tipo))


#def update_Cliente(parâmetros)

#def search_Cliente(parâmetros)

#def delete_Cliente(parâmetros)

#exibe lista de clientes
def exibe_Clientes():
    rows = csr.execute("""SELECT * FROM Cliente""")

    for row in rows:
        print "codigo = " + str(row[0])
        print "telefone = " + row[1]
        print "endereco = " + row[2]
        print "cpf = " + row[3]
        print "tipo = " + row[4]
        print


# Agora eh fazer a tabela Livro

def insert_Livro(isbn, quantidade, assunto, autor, editora):
    csr.execute("""INSERT INTO Livro VALUES(?,?,?,?,?)""", 
                   (isbn, quantidade, assunto, autor, editora))     

def exibe_Livros():
    rows = csr.execute("""SELECT * FROM Livro""")

    for row in rows:
        print "ISBN = " + str(row[0])
        print "quantidade = " + str(row[1])
        print "assunto = " + row[2]
        print "autor = " + row[3]
        print "cod editora = " + str(row[4])
        print


#Aqui começa o programa principal...

create_tables()

insert_Cliente(2, "99123-1234", "Rua sem numero", "132.123.321-45", "prata")

insert_Cliente(3, "99321-3124", "Rua com numero", "144.183.381-85","prata")

insert_Livro(12345, 5, "Ficcao", "Fulano de Tal", 1) 

insert_Livro(12564, 5, "Policial", "Beltrano", 2)

exibe_Clientes()

exibe_Livros()

connection.commit()

connection.close()