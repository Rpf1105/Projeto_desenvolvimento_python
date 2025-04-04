import sqlite3
import sqlite3 as conector
from fileinput import filename


def defineDb(conexao):
    foreignkey = '''PRAGMA foreign_keys = ON;'''

    delete = '''DROP TABLE IF EXISTS Inscrição'''
    query1 = '''CREATE TABLE IF NOT EXISTS Aluno(
	    nome varchar(255) NOT NULL,
	    matricula varchar(255) NOT NULL,
	    PRIMARY KEY(matricula)
    )'''
    query2 = '''CREATE TABLE IF NOT EXISTS Disciplina(
    	nome varchar(255) NOT NULL,
    	codigo varchar(255) NOT NULL,
    	PRIMARY KEY(codigo)
    )'''
    query3 = '''CREATE TABLE IF NOT EXISTS Inscrição(
        aluno varchar(255),
        disciplina varchar(255),
    	Ano INT NOT NULL,
    	Semestre INT NOT NULL,
    	Sim1 Real,
    	Sim2 Real,
    	Av Real,
    	Avs Real,
    	NF Real,
    	FOREIGN KEY (aluno) REFERENCES Aluno(matricula),
    	FOREIGN KEY (disciplina) REFERENCES Disciplina(codigo),
    	PRIMARY KEY (aluno, disciplina)
    )'''
    try:
        #queryTest(conexao, delete)
        queryTest(conexao, foreignkey)
        queryTest(conexao, query1)
        queryTest(conexao, query2)
        queryTest(conexao, query3)

    except ValueError as e:
        print(f"Erro: {e}")

class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

class Disciplina:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo

class Inscricao:
    def __init__(self, aluno, disciplina, ano, semestre):
        self.aluno = aluno
        self.disciplina = disciplina
        self.ano = ano
        self.semestre = semestre

def connectDb():
    try:
        conexao = conector.connect("./meu_banco.db")
        return conexao
    except conector.DatabaseError as err:
        print("Erro de banco de dados", err)
        connectDb()

def queryExec(conexao, op, table, obj):
    query = getSqlQuery(op, table)
    if query == '0':
        return 0
    try:
        queryTest(conexao, query, vars(obj))
    except TypeError:
        queryTest(conexao, query, obj)
    except ValueError as e:
        print(f"Erro: {e}")

def getSqlQuery(op, key):
    try:
        querylist = {
            '1':{ #insert
            '1': '''INSERT INTO Aluno VALUES(:nome, :matricula);''',
            '2': '''INSERT INTO Disciplina VALUES(:nome, :codigo);''',
            '3': '''INSERT INTO Inscrição(aluno,disciplina,Ano, Semestre) VALUES(:aluno, :disciplina, :ano, :semestre)'''
            },
            '2':{ #update
            '1': '''UPDATE Aluno SET nome = :nome WHERE matricula = :matricula''',
            '2': '''UPDATE Disciplina SET nome = :nome WHERE codigo = :codigo''',
            '3': '''UPDATE Inscrição SET :av = :nota WHERE disciplina = :disciplina AND aluno = :aluno'''
            },
            '3':{ #delete
            '1': '''DELETE FROM Aluno WHERE matricula = :matricula''',
            '2': '''DELETE FROM Disciplina WHERE codigo = :codigo''',
            '3': '''DELETE FROM Inscrição WHERE disciplina = :disciplina AND aluno = :aluno'''
            }
        }
        return querylist[op][key]
    except KeyError:
        return '0'

def queryTest(conexao, query, params):
    cursor = conexao.cursor()
    try:
        cursor.execute(query, params)
        conexao.commit()
    except sqlite3.OperationalError:
        cursor.executemany(query, params)
    except sqlite3.IntegrityError:
        raise ValueError("Erro de integridade")
    finally:
        cursor.close()

def closeDb(conexao):
    if conexao:
        conexao.close()

def queryExecMany(con, query):
    lista = []
    filepath = "D:\\faculdade\\python\\test\\lista_alunos"
    file = open(filepath, "r")
    for line in file:
        line = line.strip()
        line = line.split(",")
        lista.append(tuple(line))
    print(lista)
    data = [
        ('Jane', '1'),
        ('Joe', '2'),
        ('John', '3'),
    ]
    queryTest(con, query, data)

#quer = '''INSERT INTO Inscrição(aluno,disciplina,Ano, Semestre) VALUES(?, ?, 2025, 1)'''
queryExecMany(connectDb(),"INSERT INTO Aluno (nome, matricula) VALUES (?, ?)")


