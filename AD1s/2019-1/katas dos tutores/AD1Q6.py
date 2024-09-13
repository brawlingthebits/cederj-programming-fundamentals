# AD1 - Questão 6


# Subprogramas
def gerar(nLins, nCols, min, max):
    from random import randint
    vals = [None] * nLins # outra possibilidade seria o uso de append dentro do laço
    for i in range(nLins):
        vals[i] = [0] * nCols # outra possibilidade seria o uso de append dentro do laço
        for j in range(nCols):
            vals[i][j] = randint(min, max)
    return vals


def mostrar(vals, linMin, linMax, colMin, colMax):
    for i in range(linMin, linMax):
        for j in range(colMin, colMax):
            print(vals[i][j], end=" ")
        print()
    print()
    return None


def mostrarSubMatrizes(vals):
    for i in range(1, len(vals) - 1):
        for j in range(1, len(vals[i]) - 1):
            if todosAdjacentesMaiores(i, j, vals):
                mostrar(vals, i - 1, i + 2, j - 1, j + 2)
    return None


def todosAdjacentesMaiores(l, c, vals):
    for i in range(l - 1, l + 2):
        for j in range(c - 1, c + 2):
            if (i != l or j != c) and vals[i][j] <= vals[l][c]:
                return False
    return True


# Programa Principal
qtd = input().split()
qtdLinhas = int(qtd[0])
qtdColunas = int(qtd[1])
valores = gerar(qtdLinhas, qtdColunas, 10, 99)
mostrar(valores, 0, qtdLinhas, 0, qtdColunas)
mostrarSubMatrizes(valores)