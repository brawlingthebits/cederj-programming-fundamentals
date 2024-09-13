# AP3 - Q3
# Subprogramas
def mostra(nm):
    print("Conteúdo do Arquivo "+nm+":")
    dados = open(nm, "r")
    for linha in dados:
        print(linha, end="")
    dados.close()
    print()
    return None

def pegaPlataformas():
    dPlataformas = dict()
    qtdPlataformas = int(input())
    for p in range(qtdPlataformas):
        x, y = input().split()
        x, y = int(x), int(y)
        dPlataformas[(x,y)] = []
    return dPlataformas

def distancia(xA,yA,xB,yB):
    return ((xB-xA)**2+(yB-yA)**2)**0.5

def achaMaisProxima(xPoco,yPoco,dPlats):
    vence = distVence = None
    for (xPlat, yPlat) in dPlats:
        distAtual = distancia(xPoco,yPoco,xPlat,yPlat)
        if vence == None or distAtual < distVence:
            vence = (xPlat, yPlat)
            distVence = distAtual
    return vence

def agrupa(dPlataformas, nm):
    dados = open(nm, "r")
    for linha in dados:
        xP, yP = linha.split()
        xP, yP = int(xP), int(yP)
        vencedora = achaMaisProxima(xP,yP,dPlataformas)
        dPlataformas[vencedora].append((xP,yP))
    dados.close()
    return None

def mostraGruposPocos(dPlataformas):
    print("Listagem das Plataformas e seus Poços:")
    for plataforma in dPlataformas:
        print("   Plataforma:", plataforma)
        pocos = dPlataformas[plataforma]
        for poco in pocos:
            print("     Poço:", poco)
        print()
    return None

# Principal
dicionarioPlataformas = pegaPlataformas()
nomeArquivoPocos = input()
mostra(nomeArquivoPocos)
agrupa(dicionarioPlataformas, nomeArquivoPocos)
mostraGruposPocos(dicionarioPlataformas)
