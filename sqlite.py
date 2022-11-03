import sqlite3

connection = sqlite3.connect("./mydatabase.db")
tabela = connection.cursor();

tabela.execute("""CREATE TABLE dados (nome, rg, cpf, data_nasc)""")

tabela.execute("INSERT INTO dados VALUES"
"('Leila', '00352', '23456787688', '24/09/1989')")

connection.commit()

# execute your query
tabela.execute("SELECT * FROM dados")
  
# fetch all the matching rows 
result = tabela.fetchall()
  
# loop through the rows
for row in result:
    print(row)
    print("\n")

# dados = [('Joao', '01205', '345678910', '23/05/1982')]