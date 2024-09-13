# AD1 - Questão 3


# Subprogramas
def lerConstruirMatriz(qLins, qCols):
    vals = []
    for posLinha in range(qLins):
        linhaDeNumeros = []
        linhaLida = input().split()
        for posColuna in range(qCols):
            linhaDeNumeros.append(float(linhaLida[posColuna]))
        vals.append(linhaDeNumeros)
    return vals


def mostrar(vals):
    print("Matriz Lida:")
    for linha in range(len(vals)):
        for coluna in range(len(vals[linha]) - 1):
            print("%4.1f" % vals[linha][coluna], end=" ")
        print("%4.1f" % vals[linha][len(vals[linha]) - 1])
    return None


def menorMedia(vals):
    xMenor, yMenor = 0, 0
    soma = 0
    for linha in range(len(vals)):
        for coluna in range(len(vals[linha])):
            soma += vals[linha][coluna]
            if vals[linha][coluna] < vals[xMenor][yMenor]:
                xMenor, yMenor = linha, coluna
    return (xMenor + 1, yMenor + 1), soma / (len(vals) * len(vals[0]))


def mostrarAcima(cota, vals):
    print("Posições das Células Acima da Média:")
    for linha in range(len(vals)):
        for coluna in range(len(vals[linha])):
            if vals[linha][coluna] > cota:
                print("Linha = " + str(linha + 1) + ", Coluna = " + str(coluna + 1))
    return None


# Programa Principal
dimensoes = input().split()
qtdLinhas = int(dimensoes[0])
qtdColunas = int(dimensoes[1])
valores = lerConstruirMatriz(qtdLinhas, qtdColunas)
mostrar(valores)
(xMenorValor, yMenorValor), media = menorMedia(valores)
print("Posição do Menor: Linha = " + str(xMenorValor) + ", Coluna = " + str(yMenorValor))
print("Média dos Valores: %0.1f" % media)
mostrarAcima(media, valores)