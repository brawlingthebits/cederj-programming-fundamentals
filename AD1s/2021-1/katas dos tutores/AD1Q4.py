# AD1 - Questão 4
# Programa Completo
# Subprogramas
def lerPontos():
    pts = []
    linha = input()
    while linha != "":
        x, y = linha.split()
        pts.append((int(x), int(y)))
        linha = input()
    return pts


def centroide(pts):
    xCtr = yCtr = None
    if pts != []:
        somaX = somaY = qtd = 0
        for (x, y) in pts:
            qtd += 1
            somaX += x
            somaY += y
        xCtr, yCtr = somaX / qtd, somaY / qtd
    return xCtr, yCtr


def distancia(pA, pB):
    return ((pB[0] - pA[0]) ** 2 + (pB[1] - pA[1]) ** 2) ** 0.5


def extremos(pts, xCtr, yCtr):
    ptProx = ptDist = None
    if pts != []:
        ptProx = ptDist = pts[0]
        distProx = distDist = distancia(pts[0], (xCtr, yCtr))
        for pt in pts:
            distAtual = distancia(pt, (xCtr, yCtr))
            if distAtual < distProx:
                distProx = distAtual
                ptProx = pt
            elif distAtual > distDist:
                distDist = distAtual
                ptDist = pt
    return ptProx, ptDist


# Programa Principal
pontos = lerPontos()
xCentroide, yCentroide = centroide(pontos)
if xCentroide == yCentroide == None:
    print("Nenhum ponto lido. Portanto, não há centróide!!!")
else:
    print("Centróide: (%.1f, %.1f)" % (xCentroide, yCentroide))
    ptsMaisProx, ptsMaisDist = extremos(pontos, xCentroide, yCentroide)
    print("Ponto mais próximo do Centróide: (%d, %d)" % ptsMaisProx)
    print("Ponto mais distante do Centróide: (%d, %d)" % ptsMaisDist)