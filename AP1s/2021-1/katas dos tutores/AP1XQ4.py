# AP1X - Questão 4 - Valor 3.5
# Programa Completo
# Subprogramas
def converteParaPonto3D(string):
    return tuple(map(float, string.split()))


def lerPontos3D():
    pts = []
    linha = input()
    while linha != "":
        ponto = converteParaPonto3D(linha)
        pts.append(ponto)
        linha = input()
    return pts


def atualizado(pA, pB, dist):
    ptResp = []
    for i in range(len(pA)):
        if pB[i] == pA[i]:
            ptResp.append(pB[i])
        elif pB[i] > pA[i]:
            ptResp.append(pB[i] - dist)
        else:
            ptResp.append(pB[i] + dist)
    return tuple(ptResp)


def desloca(pt, delta, pts):
    for i in range(len(pts)):
        pts[i] = atualizado(pt, pts[i], delta)
    return None


def distancia(pA, pB):
    return ((pB[0] - pA[0]) ** 2 + (pB[1] - pA[1]) ** 2 + (pB[2] - pA[2]) ** 2) ** 0.5


def mostraComSomaDeDistancias(msg, ptDef, pts):
    somaDistancias = 0
    print(msg)
    for pt in pts:
        somaDistancias += distancia(ptDef, pt)
        print("    (%.2f, %.2f, %.2f)" % pt)
    print("Soma das Distâncias para o Ponto (%.2f, %.2f, %.2f): %.2f" % (ptDef[0], ptDef[1], ptDef[2], somaDistancias))
    print()
    return None


# Programa Principal
pontos = lerPontos3D()
pontoDeterminadoPeloUsuario = converteParaPonto3D(input())
mostraComSomaDeDistancias("Pontos Originais:", pontoDeterminadoPeloUsuario, pontos)
qtdDeCiclos = int(input())
deltaDeslocamento = float(input())
for ciclo in range(qtdDeCiclos):
    mensagem = "Listagem de Pontos no Ciclo %d, com Delta de Deslocamento %.2f:" % (ciclo + 1, deltaDeslocamento)
    desloca(pontoDeterminadoPeloUsuario, deltaDeslocamento, pontos)
    mostraComSomaDeDistancias(mensagem, pontoDeterminadoPeloUsuario, pontos)