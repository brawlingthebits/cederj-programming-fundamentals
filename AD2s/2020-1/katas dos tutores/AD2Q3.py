# AD2 - Questão 3


# Subprogramas
def calcula(nm):
    somaX = somaY = qtdPts = 0
    dados = open(nm, "r")
    for linha in dados:
        qtdPts += 1
        x, y = map(float, linha.split())
        somaX += x
        somaY += y
    dados.close()
    if qtdPts == 0:
        return 0, 0
    else:
        return somaX/qtdPts, somaY/qtdPts


def processa(r, ptCtr, nm):
    def distancia(xA,yA,xB,yB):
        return ((xA-xB)**2+(yA-yB)**2)**0.5

    dados = open(nm, "r")
    xC, yC = ptCtr
    for linha in dados:
        x, y = map(float, linha.split())
        if distancia(xC,yC,x,y) < r:
            print(linha.strip())
    dados.close()


# Programa Principal
raioString, nomeArqPts = input().split()
raio = float(raioString)
centroide = calcula(nomeArqPts)
print("Centróide: (%.1f, %.1f)"%centroide)
print("Listagem de Pontos dentro da Circunferência de Raio", raioString+":")
processa(raio, centroide, nomeArqPts)
