#Rogerio Perso Filho


import os
import notaInput
import notaOpen

pasta = notaInput.pasta_alunos

if not os.path.exists(pasta):
    os.mkdir(pasta)
def main():
    op = ""
    while op != "sair":
        print("Bem vindo, digite qual operacao voce deseja realizar:\n"
          "Sair: Sair do programa\n"
          "1: Registrar a nota de um aluno\n"
          "2: Ler todas as notas armazenadas\n")
        op = input().lower()
        if op == "1":
            notaInput.registrar(notaInput.getmatricula(), notaInput.getnome(), notaInput.getnota())
        elif op == "2":
            notaOpen.menuNota()

main()


