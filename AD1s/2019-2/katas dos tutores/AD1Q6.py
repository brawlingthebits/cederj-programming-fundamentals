# AD1 - Questão 6

import random


# Subprogramas
def gerarMatriz(linhas, colunas):
    matriz = []
    for _ in range(linhas):
        linha = []
        for _ in range(colunas):
            linha.append(random.randint(10, 99))
        matriz.append(linha)
    return matriz


def mostraMatriz(matriz):
    for lin in range(len(matriz)):
        for col in range(len(matriz[lin])):
            print(matriz[lin][col], end=' ')
        print()
    print()


def somar(linha):  # Aqui o método somar() foi implementado. Porém, era permitido utilizar o método sum() nativo.
    soma = 0
    for valor in linha:
        soma += valor
    return soma


def particionar(matriz, inicio, fim):
    pivo = somar(matriz[inicio])
    i  = inicio + 1
    j  = fim
    while i < j:
        while i < fim and somar(matriz[i]) < pivo:
            i += 1
        while j > inicio and somar(matriz[j]) >= pivo:
            j -= 1
        if i < j: 
            matriz[i], matriz[j] = matriz[j], matriz[i]
    if pivo > somar(matriz[j]):
        matriz[inicio], matriz[j] = matriz[j], matriz[inicio]
    return j


def quickSort(matriz, inicio, fim):
    if inicio < fim:
        posPivo = particionar(matriz, inicio, fim)
        quickSort(matriz, inicio, posPivo - 1)
        quickSort(matriz, posPivo + 1, fim)


def ordenarMatriz(matriz):
    quickSort(matriz, 0, len(matriz) - 1)


# Programa Principal
l, c = map(int, input().split())
valores = gerarMatriz(l, c)
mostraMatriz(valores)
ordenarMatriz(valores)
mostraMatriz(valores)
