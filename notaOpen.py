import os

import notaInput
pasta = notaInput.pasta_alunos

def menuNota():
    print("O que voce deseja ver:"
          "\n1- Lista de todos alunos"
          "\n2- Nota de um aluno especifico"
          "\n0- Voltar")
    op = input()
    match op:
        case "1":
            readAll()
        case "2":
            readChoose()
        case "0":
            return 0
        case _:
            raise ValueError("Escolha invalida")

def readAll():
    print("Lista de notas dos alunos:")
    for filename in os.listdir(pasta):
        with open(os.path.join(pasta, filename)) as f:
            for line in f:
                print(line.strip())
            print("-" *50)
            f.close()

def readChoose():
    print("Digite a matricula do aluno que voce quer ver")
    matricula = notaInput.getmatricula()

