# AD2 - Questão 2

# Subprogramas
def distancia(ptA, ptB):
    return ((ptA[0] - ptB[0]) ** 2 + (ptA[1] - ptB[1]) ** 2) ** 0.5


def pontoMaisDistanteDeste(pt, nmArq):
    pts = open(nmArq, "r")
    linha = pts.readline()
    coords = linha.split()
    ptMaisDist = (float(coords[0]), float(coords[1]))
    distMaior = distancia(pt, ptMaisDist)
    for linha in pts:
        coords = linha.split()
        ptAtual = (float(coords[0]), float(coords[1]))
        distAtual = distancia(pt, ptAtual)
        if distAtual > distMaior:
            distMaior = distAtual
            ptMaisDist = ptAtual
    pts.close()
    return ptMaisDist, distMaior


def maisDistantes(nm):
    pontos = open(nm, "r")
    linha = pontos.readline()
    coords = linha.split()
    pt1 = (float(coords[0]), float(coords[1]))
    pt2, maiorDist = pontoMaisDistanteDeste(pt1, nm)
    for linha in pontos:
        coords = linha.split()
        pt1Atual = (float(coords[0]), float(coords[1]))
        pt2Atual, distAtual = pontoMaisDistanteDeste(pt1Atual, nm)
        if distAtual > maiorDist:
            pt1 = pt1Atual
            pt2 = pt2Atual
            maiorDist = distAtual
    return pt1, pt2, maiorDist


# Programa Principal
nome = input()
coordenadasPontoA, coordenadasPontoB, distanciaEntreEles = maisDistantes(nome)
print("Ponto Inicial =", coordenadasPontoA)
print("Ponto Final =", coordenadasPontoB)
print("Distância entre eles =", distanciaEntreEles)