# AP3 - Questão 1


# Subprogramas
def qualMaisDistanteDoAtual(xA, yA, nm):
    dados = open(nm, "r")
    xP = yP = None
    dist = -1
    for linha in dados:
        x, y = map(int, linha.split())
        d = ((xA - x) ** 2 + (yA - y) ** 2) ** 0.5
        if d > dist:
            xP, yP, dist = x, y, d
    dados.close()
    return xP, yP, dist


def maisDistantes(nm):
    dados = open(nm, "r")
    pA = pB = None
    distAB = -1
    for linha in dados:
        xAtual, yAtual = map(int, linha.split())
        xMD, yMD, distAtualMD = qualMaisDistanteDoAtual(xAtual, yAtual, nm)
        if distAtualMD > distAB:
            pA = (xAtual, yAtual)
            pB = (xMD, yMD)
            distAB = distAtualMD
    dados.close()
    return pA, pB, distAB


# Programa Principal
nome = input()
ptA, ptB, dist = maisDistantes(nome)
print("Pontos Mais Distantes:", ptA, "e", ptB)
print("Distância entre eles (com precisão de uma casa decimal):", "%.1f" % dist)
