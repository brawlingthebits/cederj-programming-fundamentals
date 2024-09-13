# Programa AP1.Q2


# Subprograma(s)
def lerPontos():
    qtdPontos = int(input())
    listaPontos = [None] * qtdPontos
    for posicao in range(qtdPontos):
        x, y = input().split()  # ou simplesmente map(float, input().split())
        x, y = float(x), float(y)
        listaPontos[posicao] = (x, y)
    return listaPontos


def lerCentroERaio():
    x, y, r = input().split()  # ou simplesmente map(float, input().split())
    x, y, r = float(x), float(y), float(r)
    return (x, y, r)


def distancia(xA, yA, xB, yB):
    return ((xB - xA) ** 2 + (yB - yA) ** 2) ** 0.5


def contidos(cR, pts):
    xC, yC, rC = cR
    print("Contidos na circunferência com centro (%.1f, %.1f) e raio %.1f:" % (xC, yC, rC))
    for (x, y) in pts:
        if distancia(xC, yC, x, y) <= rC:
            print("    ", (x, y))
    return None


# Principal
# Inicialização
pontos = lerPontos()
# Processamento
centroERaio = lerCentroERaio()
while centroERaio != (0, 0, 0):
    contidos(centroERaio, pontos)
    centroERaio = lerCentroERaio()
# Finalização
print("Obrigado por utilizar nosso sistema!!!")
