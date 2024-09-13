# AP2X - Questão 1


# Subprogramas
def processa(nm, distMaxima):
    dados = open(nm, "r")
    metros = 0
    x1, y1 = map(int, dados.readline().split())
    for proximaLinha in dados:
        x2, y2 = map(int, proximaLinha.split())
        metros += ((x1-x2)**2+(y1-y2)**2)**0.5
        x1, y1 = x2, y2
    dados.close()
    if metros > distMaxima:
        print(nm, "percorreu:", metros, "metros")
    return metros


def acimaEMedia(nm):
    dados = open(nm, "r")
    somaDasDistancias = qtdCelulares = 0
    for celular in dados:
        qtdCelulares += 1
        somaDasDistancias += processa(celular.strip(), 500)
    dados.close()
    print("Média das Distâncias Percorridas:", somaDasDistancias/qtdCelulares)


# Programa Principal
nome = input()
acimaEMedia(nome)