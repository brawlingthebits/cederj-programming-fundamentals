# AD1 - Questão 5


# Subprogramas
def inverter(colecao):
    if len(colecao) > 1:
        colecao[0], colecao[-1] = colecao[-1], colecao[0]
        colecao[1:-1] = inverter(colecao[1:-1])
    return colecao


def menorEMaior(colecao):
    if len(colecao) > 1:
        r = menorEMaior(colecao[1:])
        if r[0] > colecao[0]:
            r[0] = colecao[0]
        if r[1] < colecao[0]:
            r[1] = colecao[0]
    elif len(colecao) == 1:
        r = [colecao[0], colecao[0]]
    else:
        r = [None, None]
    return r


def imprimir(colecao):
    if len(colecao) != 0:
        print(colecao[0], end=" ")
        imprimir(colecao[1:])
    else:
        print()


# Programa Principal
valores = input().split()
for i in range(len(valores)):
    valores[i] = int(valores[i])

imprimir(inverter(valores))
imprimir(menorEMaior(valores))
