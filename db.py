import sqlite3
import sqlite3 as conector


def defineDb(conexao5):
    cursor = conexao.cursor()
    query = '''CREATE TABLE IF NOT EXISTS Pessoa(
	nome varchar(255) NOT NULL,
	cpf varchar(255) NOT NULL,
	nascimento date NOT NULL,
	oculos boolean NOT NULL,
	PRIMARY KEY(cpf)
    )'''
    try:
        queryTest(cursor, query)
    except ValueError as e:
        print(f"Erro: {e}")
    cursor.close()

def connectDb():
    try:
        conexao = conector.connect("./meu_banco.db")
        return conexao
    except conector.DatabaseError as err:
        print("Erro de banco de dados", err)
        connectDb()

def insertTable(conexao, table):
    cursor = conexao.cursor()
    query = f'''
        INSERT INTO {table} (cpf, nome, nascimento, oculos) VALUES
        (
        {input("Digite o cpf:")}, 
        "{input("Digite o nome:")}", 
        {input("Digite a data de nascimento em YYYY/MM/DD\n")},
        {input("Digite se usa oculos 0-nao, 1-sim:")}
        )
        '''
    try:
        queryTest(cursor, query)
    except ValueError as e:
        print(f"Erro: {e}")
    finally:
        cursor.close()


def queryAll(conexao):
    cursor = conexao.cursor()
    query = '''SELECT * FROM Pessoa'''
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()

def queryTest(cursor, query):
    try:
        print(query)
        cursor.execute(query)
        conexao.commit()
    except sqlite3.IntegrityError:
        raise ValueError("Erro de integridade")


def closeDb(conexao):
    if conexao:
        conexao.close()

conexao = connectDb()
defineDb(conexao)
insertTable(conexao, "Pessoa")
#queryAll(conexao)
closeDb(conexao)