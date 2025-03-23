pasta_alunos = "alunos"

def registrar(matricula: str, nome: str, nota: str):
    filename = pasta_alunos + "/" + matricula + ".txt"
    content = f"Matricula: {matricula} \nNome: {nome} \nNota: {nota}"
    try:
        file = open(filename, "x")
        file.write(content)
    except FileExistsError:
        print("O arquivo ja existe, deseja substitui-lo, se sim digite s")
        if input().lower() == 's':
            file = open(filename, "w")
            file.write(content)
            print("O arquivo foi sobreescrito")
        else:
            print("Os novos valores nao foram salvos")
    except PermissionError:
        print("O arquivo não pode ser acessado")
    file.close()


def getmatricula():
    try:
        print("Digite a matricula do aluno")
        matricula=input()
        matvalida(matricula)
        return str(matricula)
    except ValueError as e:
        msgerro(e)
        return getmatricula()

def getnome():
    try:
        print("Digite o nome do aluno")
        nome = input()
        nomevalido(nome)
        return nome.capitalize()
    except ValueError as e:
        msgerro(e)
        return getnome()


def getnota():
    try:
        print("Qual é a nota do aluno")
        nota = input()
        notaValida(nota)
        return nota
    except ValueError as e:
        msgerro(e)
        return getnota()

def matvalida(matricula):
    if not matricula:
        raise ValueError("Nao foi digitada nenhuma matricula")
    if len(matricula) != 8:
        raise ValueError("O tamanho da matricula esta errado")
    try:
        int(matricula)
    except ValueError:
        raise ValueError("A matricula só pode conter numeros")

def nomevalido(nome):
    if not nome:
        raise ValueError("Nao foi digitado nenhum nome")
    if any(char.isnumeric() for char in nome):
        raise ValueError("O nome contem digitos")

def notaValida(nota):
    if not nota:
        raise ValueError("Nao foi digitada nenhuma nota")
    try:
        float(nota)
    except ValueError:
        raise ValueError("Nao foi digitado um numero")
    if not 0 <= float(nota) <= 10:
        raise ValueError("A nota digitada deve ser entre 0 e 10")

def msgerro(erro):
    print(f"Ocorreu um erro: {erro}")
    print("\n" + "-"*40)


