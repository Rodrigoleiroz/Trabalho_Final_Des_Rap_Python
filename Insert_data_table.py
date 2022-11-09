#  Inserindo dados na tabela “Agenda”.
import psycopg2

conn = psycopg2.connect(database="postgres, user="postgres", password="postgres4321", port="5432")
print("Conexao com o banco de dados aberta com sucesso!")

comando = conn.cursor()
comando.execute(""" INSERT INTO AGENDA (id, Nome, Telefone))