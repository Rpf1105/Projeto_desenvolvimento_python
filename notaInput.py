pasta_alunos = "alunos"

def registrar(nome: str, nota: str):
    filename = pasta_alunos + "/" + nome + ".txt"
    texto = "Nota: " + nota
    try:
        file = open(filename, "x")
        file.write(texto)
        file.close()
    except FileExistsError:
        print("O arquivo ja existe, deseja substitui-lo, se sim digite s")
        if input().lower() == 's':
            file = open(filename, "w")
            file.write(texto)
            file.close()
            print("O arquivo foi sobreescrito")
        else:
            print("Os novos valores nao foram salvos")
    except PermissionError:
        print("O arquivo não pode ser acessado")

def getnome():
    try:
        print("Digite o nome do aluno")
        nome = input()
        nomevalido(nome)
        return nome
    except ValueError as e:
        msgerro(e)
        return getnome()


def getnota():
    try:
        print("Qual é a nota do aluno")
        nota = input()
        notavalida(nota)
        return nota
    except ValueError as e:
        msgerro(e)
        return getnota()

def nomevalido(nome):
    if not nome:
        raise ValueError("Nao foi digitado nenhum nome")
    if any(char.isnumeric() for char in nome):
        raise ValueError("O nome contem digitos")

def notavalida(nota):
    if not nota:
        raise ValueError("Nao foi digitada nenhuma nota")
    try:
        float(nota)
    except ValueError:
        raise ValueError("Nao foi digitado um numero")
    if not 0 <= float(nota) <= 10:
        raise ValueError("A nota digitada deve ser entre 0 e 10")

def msgerro(erro):
    print("Ocorreu um erro: ")
    print(erro)
    print("\n" + "-"*40)


