# Programa AP3Q1 - 2022.1 - Perímetro do Polígono de Pontos
# Subprogramas
def mostra(nm):
    print("Conteúdo do Arquivo de Pontos", nm + ":")
    dados = open(nm, "r")
    for pontoLido in dados:
        print(pontoLido.strip())
    dados.close()
    print()
    return None


def distancia(xA, yA, xB, yB):
    return ((xB - xA) ** 2 + (yB - yA) ** 2) ** 0.5


def calculaPerimetro(nm):
    distanciaTotal = None
    dados = open(nm, "r")
    primeiroPonto = dados.readline()
    if primeiroPonto != "":
        xP, yP = primeiroPonto.split()
        xAnterior, yAnterior = int(xP), int(yP)
        distanciaTotal = 0
        for proximoPonto in dados:
            xAtual, yAtual = proximoPonto.split()
            xAtual, yAtual = int(xAtual), int(yAtual)
            distAtual = distancia(xAnterior, yAnterior, xAtual, yAtual)
            distanciaTotal += distAtual
            xAnterior, yAnterior = xAtual, yAtual
        xPrimeiro, yPrimeiro = int(xP), int(yP)
        distanciaTotal += distancia(xAnterior, yAnterior, xPrimeiro, yPrimeiro)
    dados.close()
    return distanciaTotal


# Principal
nomeArqPontos = input()
mostra(nomeArqPontos)
perimetro = calculaPerimetro(nomeArqPontos)
if perimetro == None:
    print("Arquivo de pontos está vazio!!!")
else:
    print("Perímetro do polígono de pontos contidos no arquivo: %.2f" % perimetro)
