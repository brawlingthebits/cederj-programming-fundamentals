# AP1 - Questão 2


# Subprogramas
def lerEConstruirMatrizDeValores(qL, qC):
    vs = []
    for posicaoLinha in range(qL):
        linha = input()
        partes = linha.split()
        for posicaoColuna in range(qC):
            partes[posicaoColuna] = int(partes[posicaoColuna])
        vs.append(partes)
    return vs


def mostrar(vs):
    print("Matriz lida:")
    for posLinha in range(len(vs)):
        for posColuna in range(len(vs[posLinha])):
            print("%4d" % vs[posLinha][posColuna], end=" ")
        print()
    print()
    return None


def primo(numero):
    for candidatoADivisor in range(2, numero // 2 + 1):
        if numero % candidatoADivisor == 0:
            return False
    return numero > 1


def mostrarPosicaoEValorDeCadaNumeroPrimo(vs):
    print("Células da matriz que contêm números primos:")
    for posLinha in range(len(vs)):
        for posColuna in range(len(vs[posLinha])):
            if primo(vs[posLinha][posColuna]):
                print("Linha = " + str(posLinha + 1) + ", Coluna = " + str(posColuna + 1) + ", Valor =",
                      vs[posLinha][posColuna])
    return None


# Programa Principal
dimensoes = input().split()
qtdLinhas = int(dimensoes[0])
qtdColunas = int(dimensoes[1])

valores = lerEConstruirMatrizDeValores(qtdLinhas, qtdColunas)

mostrar(valores)

mostrarPosicaoEValorDeCadaNumeroPrimo(valores)