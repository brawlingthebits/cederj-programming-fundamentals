# AP1 - Questão 2


# Subprogramas

def converte(partes):
    numeros = []
    for item in partes:
        numeros.append(int(item))
    return numeros


def mostra(valores):
    print("----- Matriz Lida -----")
    for linha in valores:
        for valor in linha:
            print("%4d"%valor, end = " ")
        print()
    print("-----------------------")
    return None


def somar(vs, lin):
    total = 0
    for coluna in range(len(vs[lin])):
        total += vs[lin][coluna]
    return total


def linhaDeMaiorSoma(valores):
    if valores == []:
        print("Matriz vazia, não existe linha com maior soma!!!")
    else:
        linhaMaiorSoma = 0
        somaMaior = somar(valores, 0)
        for linha in range(1, len(valores)):
            somaNaLinha = somar(valores, linha)
            if somaNaLinha > somaMaior:
                somaMaior = somaNaLinha
                linhaMaiorSoma = linha
        print("Linha com maior soma foi a linha com valor(es):", str(valores[linhaMaiorSoma])+", cuja soma =", somaMaior)
    return None


def constroiMatriz():
    valores = []
    linha = input()
    while linha != "":
        linhaDeNumeros = converte(linha.split())
        valores.append(linhaDeNumeros)
        linha = input()
    return valores


# Programa Principal
matrizDeNumeros = constroiMatriz()
mostra(matrizDeNumeros)
linhaDeMaiorSoma(matrizDeNumeros)