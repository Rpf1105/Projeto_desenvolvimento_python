import sqlite3
import sqlite3 as conector
from notaInput import getmatricula, getnota


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
        aluno varchar(255) NOT NULL,
        disciplina varchar(255) NOT NULL,
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
    def insert(self, con):
        query = '''INSERT INTO Aluno VALUES(:nome, :matricula)'''
        queryExec(con, query, self)
    def update(self, con):
        self.matricula = getmatricula()
        query = '''UPDATE Aluno SET nome = :nome WHERE matricula = :matricula'''
        queryExec(con, query, self)
    def delete(self, con):
        self.matricula = getmatricula()
        query = '''DELETE FROM Aluno WHERE matricula = :matricula'''
        queryExec(con, query ,self)
    def select(self, con):
        self.matricula = getmatricula()
        query = '''SELECT * FROM Aluno WHERE matricula = :matricula'''
        queryExec(con, query, self)

class Disciplina:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
    def insert(self, con):
        query = '''INSERT INTO Disciplina VALUES(:nome, :codigo);'''
        queryExec(con, query, self)
    def update(self, con):
        query = '''UPDATE Disciplina SET nome = :nome WHERE codigo = :codigo'''
        queryExec(con, query, self)
    def delete(self, con):
        query = '''DELETE FROM Disciplina WHERE codigo = :codigo'''
        queryExec(con, query ,self)
    def select(self, con):
        query = '''SELECT * FROM Disciplina WHERE codigo = :codigo'''
        queryExec(con, query, self)

class Inscricao:
    def __init__(self, aluno, disciplina, ano, semestre):
        self.aluno = aluno
        self.disciplina = disciplina
        self.ano = ano
        self.semestre = semestre
        self.avescolha = ""
        self.nota = ""
        self.sim1 = ""
        self.sim2 = ""
        self.av = ""
        self.avs = ""
    def insert(self, con):
        query = '''INSERT INTO Inscrição(aluno,disciplina,Ano, Semestre) VALUES(:aluno, :disciplina, :ano, :semestre)'''
        queryExec(con, query, self)
    def update(self, con):
        self.avescolha = input("Digite o nome da av a registrar a nota (sim1, sim2, av, avs): ").lower()
        self.nota = getnota()
        query = '''UPDATE Inscrição SET :avescolha = :nota WHERE disciplina = :disciplina AND aluno = :aluno'''
        queryExec(con, query, self)
    def delete(self, con):
        query = '''DELETE FROM Inscrição WHERE disciplina = :disciplina AND aluno = :aluno'''
        queryExec(con, query ,self)
    def select(self, con):
        query = '''SELECT * FROM Inscrição WHERE disciplina = :disciplina AND aluno = :aluno'''
        queryExec(con, query, self)


def connectDb():
    try:
        conexao = conector.connect("./meu_banco.db")
        return conexao
    except conector.DatabaseError as err:
        print("Erro de banco de dados", err)
        connectDb()

def queryExec(con, query, obj):
    try:
        queryTest(con, query, vars(obj))
        con.commit()
    except TypeError:
        queryTest(con, query, obj)
    except ValueError as e:
        print(f"Erro: {e}")

def queryTest(conexao, query, params=()):
    cursor = conexao.cursor()
    try:
        cursor.execute(query, params)
    except sqlite3.ProgrammingError:
        cursor.executemany(query, params)
    except sqlite3.IntegrityError:
        raise ValueError("Erro de integridade")
    finally:
        cursor.close()

def closeDb(conexao):
    if conexao:
        conexao.close()

def queryExecMany(con, query, nome):
    lista = []
    filepath = "lista_alunos"
    file = open(filepath, "r", encoding='utf-8')
    for line in file:
        line = line.strip()
        line = line.split(",")
        if nome:
            print(line[0])
        lista.append(tuple(line))
    print(lista)
    print(query)
    #queryTest(con, query, lista)

#quer = '''INSERT INTO Inscrição(aluno,disciplina,Ano, Semestre) VALUES(?, ?, 2025, 1)'''
#queryExecMany(connectDb(), quer, 1)


