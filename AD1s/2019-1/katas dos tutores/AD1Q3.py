# AD1 - Questão 3


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


def valoresPosicoesMenorMaior(valores):
    if valores == []:
        print("Matriz vazia, não existem valores menor e maior!!!")
    else:
        posMenor, posMaior = (0, 0), (0, 0)
        valorMenor = valorMaior = valores[0][0]
        for i in range(len(valores)):
            for j in range(len(valores[i])):
                if valores[i][j] < valorMenor:
                    valorMenor = valores[i][j]
                    posMenor = (i, j)
                elif valores[i][j] > valorMaior:
                    valorMaior = valores[i][j]
                    posMaior = (i, j)
        print("Menor Valor:", valorMenor, "na posição:", posMenor)
        print("Maior Valor:", valorMaior, "na posição:", posMaior)
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
valoresPosicoesMenorMaior(matrizDeNumeros)