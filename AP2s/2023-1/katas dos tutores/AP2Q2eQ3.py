# Subprograma(s)
def menu():
    print("Entrada dos Pontos via teclado (T) ou via arquivo (A)?: ")
    return input()[0]


def lerPontos(op):
    if op not in "TtAa":
        return None
    else:
        lidos = []
        if op in "Tt":
            ptLido = input()
            while ptLido != "":
                x, y = ptLido.split()
                x, y = int(x), int(y)
                lidos.append((x, y))
                ptLido = input()
        else:
            nomeArquivo = input("Escolha o nome do arquivo que contém os pontos: ")
            arquivo = open(nomeArquivo, "r")
            for ptLido in arquivo:
                x, y = ptLido.split()
                x, y = int(x), int(y)
                lidos.append((x, y))
            arquivo.close()
        return lidos


def mostrar(pts):
    if pts == None:
        print("Opção Inválida!!! - Nenhum Ponto a Mostrar.")
    else:
        print("Listagem doos Pontos Lidos:")
        for pt in pts:
            print("     ", pt)
        print("Fim da Listagem")
    return None


def distancia(ptA, ptB):
    return ((ptB[0] - ptA[0]) ** 2 + (ptB[1] - ptA[1]) ** 2) ** 0.5


def maisDistante(p, pts):
    ptMaisDist = pts[0]
    distMaisDist = distancia(p, ptMaisDist)
    for ptCandidato in pts:
        distCandidato = distancia(p, ptCandidato)
        if distCandidato > distMaisDist:
            ptMaisDist = ptCandidato
            distMaisDist = distCandidato
    return ptMaisDist, distMaisDist

def pegaInfos(pts):
    pA = pts[0]
    pB, distAB = maisDistante(pA, pts)
    for pAtual in pts:
        pMaisDistAtual, distAtual = maisDistante(pAtual, pts)
        if distAtual > distAB:
            pA = pAtual
            pB = pMaisDistAtual
            distAB = distAtual
    return pA, pB, distAB


def mostrarDoisPontosMaisDistantesEDistanciaEntreEles(pts):
    if pts == None or pts == []:
        print("Não existem pontos mais distantes!")
    else:
        ptA, ptB, distanciaEntreAeB = pegaInfos(pts)
        print("Pontos Mais Distantes:", ptA, "e", ptB, "com distância: %.2f" % distanciaEntreAeB)
    return None


# Principal
opcao = menu()
pontos = lerPontos(opcao)
mostrar(pontos)
mostrarDoisPontosMaisDistantesEDistanciaEntreEles(pontos)
