#Rogerio Perso Filho

import os
from operator import truediv

import db
import notaInput

pasta = notaInput.pasta_alunos
if not os.path.exists(pasta):
    os.mkdir(pasta)

def main():
    con = db.connectDb()
    op = ""
    while True:
        print("Bem vindo, digite qual operacao voce deseja realizar:\n"
          "Sair: Sair do programa\n"
          "1: Registrar uma entrada ao DB\n"
          "2: Modificar uma entrada no DB\n"
          "3: Deletar uma entrada do DB\n"
        )
        op = input().lower()
        if op =="sair":
            return 0
        print("Qual tabela voce deseja realizar essa operação:\n"
              "1-Alunos\n"
              "2-Disciplinas\n"
              "3-Inscrições\n"
              )
        table = input()
        if op == "1" or op == "2":
            if table == "1":
                db.queryExec(con, op, table, db.Aluno(input("Digite o nome do aluno: "), input("Digite a matricula do aluno")))
            elif table == "2":
                db.queryExec(con, op, table, db.Disciplina(input("Digite o nome da Disciplina: "), "ARA0000"))
            elif table == "3":
                db.queryExec(con, op, table, db.Inscricao(input("Digite a matricula do aluno: "), input("Digite o codigo da disciplina:"), input("Digite o ano:"), input("Digite o semestre")))
        else:
            if table == "1":
                db.queryExec(con, op, table, {
                    "matricula": input("Digite a matricula do aluno")
                })
            elif table == "2":
                db.queryExec(con, op, table,{
                    "codigo":input("Digite o codigo da disciplina"),
                })
            elif table == "3":
                db.queryExec(con, op, table, {
                    "disciplina":input("Digite o codigo da disciplina"),
                    "aluno": input("Digite a matricula do aluno")
                })

main()


