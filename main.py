#Rogerio Perso Filho

import os
import db
import notaInput
import datetime

pasta = notaInput.pasta_alunos
if not os.path.exists(pasta):
    os.mkdir(pasta)

def dbTable(x):
    menuOptions = {
            '1':db.Aluno,
            '2':db.Disciplina,
            '3':db.Inscricao
    }
    return menuOptions[x]

def objectBuilder(cls):
    if cls == db.Aluno:
        obj = cls(
            notaInput.getnome(),
            notaInput.gerarMatricula()
        )
    elif cls == db.Disciplina:
        obj = cls(
            input("Digite o nome da materia: "),
            input("Digite o codigo da materia: ")
        )

    else:
        return 0
    return obj

def tableOp(op, obj):
    opList = {
        '1': obj.insert,
        '2': obj.update,
        '3': obj.delete,
        '4': obj.select
    }
    return  opList[op]
def main():
    con = db.connectDb()
    db.defineDb(con)
    while True:
        op = ""
        table = ""
        print("Bem vindo, qual tabela voce deseja realizar essa operação:\n"
              "Sair: Sair do programa\n"
              "1-Alunos\n"
              "2-Disciplinas\n"
              "3-Inscrições\n"
              )
        table = input().lower()
        if table =="sair":
            return 0
        print("Bem vindo, digite qual operacao voce deseja realizar:\n"
          "1: Registrar uma entrada ao DB\n"
          "2: Modificar uma entrada no DB\n"
          "3: Deletar uma entrada do DB\n"
        )
        op = input().lower()

        obj = objectBuilder(dbTable(table))
        method = tableOp(op, obj)
        method(con)

if __name__ == "__main__":
    main()

