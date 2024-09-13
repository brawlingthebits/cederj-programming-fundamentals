# AD2 - Questão 3


# Subprogramas
def calculaCentroGeometrico(nm):
    cGeo = None # se o arquivo estiver vazio retorna None - Desnecessário pelo enunciado.
    dados = open(nm, "r")
    linha = dados.readline()
    if linha != "":  # possui pelo menos um ponto x, y no arquivo - Assegurado pelo enunciado.
        x, y = map(float, linha.split())
        somaX = x
        somaY = y
        qtdLinhas = 1
        for linha in dados: # Itera do segundo ponto do arquivo, até o final.
            x, y = map(float, linha.split())
            somaX += x
            somaY += y
            qtdLinhas += 1
        cGeo = (somaX / qtdLinhas, somaY / qtdLinhas)
    dados.close()
    return cGeo


def distancia(pt1, pt2):
    return ((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2) ** 0.5


def pontoMaisProximo(nm, centroide):
    dados = open(nm, "r")
    linha = dados.readline()
    xMaisProximo, yMaisProximo = map(float, linha.split())
    distMaisProximo = distancia(centroide, (xMaisProximo, yMaisProximo))
    for linha in dados:
        x, y = map(float, linha.split())
        dist = distancia(centroide, (x, y))
        if dist < distMaisProximo:
            distMaisProximo, xMaisProximo, yMaisProximo = dist, x, y
    print("Ponto Mais Próximo:", "(%.1f, %.1f)"%(xMaisProximo, yMaisProximo))
    dados.close()
    return None


# Programa Principal
nome = input()
centroide = calculaCentroGeometrico(nome)
if centroide != None:
    print("Centróide:", "(%.1f, %.1f)"%centroide)
    pontoMaisProximo(nome, centroide)