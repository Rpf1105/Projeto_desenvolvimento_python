import os
import notaInput
pasta = notaInput.pasta_alunos
def readAll():
    print("Lista de notas dos alunos:")
    for filename in os.listdir(pasta):
        with open(os.path.join(pasta, filename)) as f:
            nome_aluno = f.name
            nome_aluno = nome_aluno.strip(".txt")
            nome_aluno = nome_aluno.removeprefix("alunos\\")
            nome_aluno = nome_aluno.capitalize()
            print(nome_aluno)
            print(f.read() + "\n")
            f.close()