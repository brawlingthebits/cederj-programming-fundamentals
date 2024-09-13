# AD2 - Questão 1


# Subprogramas
def repete(vals):
    listaRepetidos = []
    for x in vals:
        if (x not in listaRepetidos) and vals.count(x) > 1:
            listaRepetidos.append(x)
    return listaRepetidos


def ordena(vals):
    for i in range(len(vals)-1):
        ondeMenor = i
        for j in range(i+1, len(vals)):
            if vals[j] < vals[i]:
                ondeMenor = j
        vals[i], vals[ondeMenor] = vals[ondeMenor], vals[i]


def mostra(vals):
    for x in vals:
        print(x)


# Programa Principal
listaNomesSobrenomes = []
nome = input()
while nome != "":
    partes = nome.split()
    for x in partes:
        if len(x) > 2:
            listaNomesSobrenomes.append(x)
    nome = input()
listaNomesSobrenomesComMaisQueUmaOcorrencia = repete(listaNomesSobrenomes)
ordena(listaNomesSobrenomesComMaisQueUmaOcorrencia)
mostra(listaNomesSobrenomesComMaisQueUmaOcorrencia)
