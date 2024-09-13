# Programa AD11.Q2


# Subprograma(s)
def lerPonto():
    coordenadaX, coordenadaY = input().split()  # ou simplesmente map(float, input().split())
    coordenadaX = float(coordenadaX)
    coordenadaY = float(coordenadaY)
    return coordenadaX, coordenadaY


def distancia(xA, yA, xB, yB):
    return ((xB - xA) ** 2 + (yB - yA) ** 2) ** 0.5


# Principal
# Inicialização
qtdPontosPraLer = int(input())
distanciaPercorrida = 0
# Processamento
for vez in range(qtdPontosPraLer):
    xAtual, yAtual = lerPonto()
    if vez == 0:
        xAntes, yAntes = xAtual, yAtual
    else:
        distanciaPercorrida = distanciaPercorrida + distancia(xAntes, yAntes, xAtual, yAtual)
        xAntes, yAntes = xAtual, yAtual
# Finalização
if qtdPontosPraLer < 2:
    print("Tem menos de dois pontos o percurso. Portanto distância nula!!!")
else:
    print("Distância percorrida entre os %d pontos lidos: %.1f" % (qtdPontosPraLer, distanciaPercorrida))
