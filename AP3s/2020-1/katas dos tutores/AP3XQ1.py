# AP3X - Questão 1


# Subprogramas
def produz(nm):
    vals = dict()
    dados = open(nm, "r")
    for linha in dados:
        pals = linha.strip().split()
        for p in pals:
            if vals.get(p) == None:
                vals[p] = 1
            else:
                vals[p] += 1
    dados.close()
    return vals


def maisQueQuantasVezes(nm, qtd):
    dicionario = produz(nm)
    for pal in sorted(dicionario.keys()):
        if dicionario[pal] > qtd:
            print(pal)


# Programa Principal
nome = input()
maisQueQuantasVezes(nome, 5)