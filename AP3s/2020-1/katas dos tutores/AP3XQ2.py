# AP3X - Questão2


# Subprogramas
def carrega(nm):
    vals = []
    dados = open(nm, "r")
    for linha in dados:
        numeros = list(map(int, linha.split()))
        vals.append(numeros)
    dados.close()
    return vals


def primo(x):
    for divisor in range(2, int(x**0.5)+1):
        if x % divisor == 0:
            return False
    return x > 1


def todosPrimos(vals):
    for x in vals:
        if not primo(x):
            return False
    return True


def listaLinhas(vals):
    for lin in range(len(vals)):
        if todosPrimos(vals[lin]):
            print("Linha", lin+1)


def listaColunas(vals):
    for col in range(len(vals[0])):
        lista = []
        for lin in range(len(vals)):
            lista.append(vals[lin][col])
        if todosPrimos(lista):
            print("Coluna", col+1)


def relaciona(nm):
    valores = carrega(nm)
    print("Relação de Linha(s) e Coluna(s) com todos elementos primos:")
    listaLinhas(valores)
    listaColunas(valores)


# Programa Principal
nome = input()
relaciona(nome)