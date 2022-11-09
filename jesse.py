import sqlite3

conn = sqlite3.connect("MeuBanco.db")
print("Conexão com o Banco de Dados aberta com sucesso!")

comando = conn.cursor()
comando.execute(""" CREATE TABLE Agenda
                (id INT PRIMARY KEY NOT NULL,
                Nome TEXT NOT NULL,
                Telefone CHAR(12));
            """)
conn.commit()
print("Tabela criada com sucesso no BD!!!")

comando = conn.cursor()
comando.execute("""INSERT INTO Agenda 
                (id,Nome, Telefone)
                VALUES ("1","Pessoa 1", "900235478")
                """)

conn.commit()

print("Inserção realizada com sucesso!!!")

comando = conn.cursor()
def imprimirBD():
    for i in comando.execute("SELECT * FROM Agenda ORDER BY id"):
        print(i)

def readDB():
    comando.execute("""SELECT * FROM Agenda """)
    for linha in comando.fetchall():
        print(linha)

id = "1"
nome_novo = "Eu"

conn.execute("""UPDATE Agenda 
            SET Nome = ?
            WHERE id = ?
            """,(nome_novo,id))

conn.commit()


from sqlite3 import OperationalError
from sqlite3 import Error
class AppBD:
    def _init_(self):
        print("construtor")
    def abrirConexao(self):
        try:
            self.connection = sqlite3.connect("CRUD.db")
            print("connected DB", self.connection)
        except (OperationalError) as error:
            if self.connection:
                print("SQlite DB error...",error)

import tkinter as tk
import sqlite3 as sqlite3

#-------------------------------------
#Programa Principal
#-------------------------------------
janela=tk.Tk()
principal=AppBD(janela)
janela.title("Bem Vindo a Tela de Cadastro")
janela.geometry("600x500")
janela.mainloop()

#-------------------------------------------

class PrincipalBD:
    def_init_(self,win)
    self.objBD = crud.AppBD(Text)
    #componentes
    self.lbCodigo=tk.Label(win, text="Código de Produto: ")