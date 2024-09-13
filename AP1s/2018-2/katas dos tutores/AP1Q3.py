# AP1 - Questão 3


# Subprogramas
def obterValores():
    from random import random
    n = int(input())
    lista = []
    for _ in range(n):
        lista.append(random())
    return lista


def escreverValores(lista):
    for valor in lista:
        print("%1.2f" % valor, end=" ")
    print()


def ordenarValores(lista):
    for n in range(len(lista) - 1, 0, -1):
        for i in range(n):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]


# Programa Principal
valores = obterValores()
escreverValores(valores)
ordenarValores(valores)
escreverValores(valores)
