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