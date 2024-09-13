# AD1 - Questão 5
# Programa Completo
# Subprogramas
def lerCandidatosNumeros():
    qtdCands = int(input())
    listaCandsNumsVots = []
    for i in range(qtdCands):
        nome, numero = input().split("#")
        listaCandsNumsVots.append([nome, int(numero), 0])
    listaCandsNumsVots.append(["Brancos", 0, 0])
    listaCandsNumsVots.append(["Nulos", None, 0])
    return listaCandsNumsVots


def mostra(listaVs):
    for i in range(len(listaVs) - 2):
        print(listaVs[i][0], "-", listaVs[i][1], "- com", listaVs[i][2], "voto(s)")
    qtdVotosBrancos = listaVs[len(listaVs) - 2][2]
    qtdVotosNulos = listaVs[len(listaVs) - 1][2]
    print("Brancos - com", qtdVotosBrancos, "voto(s)")
    print("Nulos - com", qtdVotosNulos, "voto(s)")
    return None


def localiza(v, listaVs):
    for i in range(len(listaVs) - 1):
        if v == listaVs[i][1]:
            return i
    return len(listaVs) - 1


def processaVotacao(listaCandsNumsVots):
    voto = int(input())
    while voto >= 0:
        onde = localiza(voto, listaCandsNumsVots)
        listaCandsNumsVots[onde][2] += 1
        voto = int(input())
    return None


# Programa Principal
listaCandidatosNumerosVotos = lerCandidatosNumeros()
processaVotacao(listaCandidatosNumerosVotos)
mostra(listaCandidatosNumerosVotos)