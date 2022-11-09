# Conectando com o BD e criando (CREATE) uma tabela “Agenda”.

import psycopg2

conn = psycopg2.connect(database="postgres, user="postgres", password="postgres4321", port="5432")
print("Conexao com o banco de dados aberta com sucesso!")

comando = conn.cursosr()
comando.execute(""" CREATE TABLE Agenda
                (id INT PRIMARY KEY NOT NULL,
                NOME TEXT NOT NULL,
                TElefone CHAR(12));
                """)
conn.commit()
print("Tabela criada com sucesso no DB!")
conn.close()


