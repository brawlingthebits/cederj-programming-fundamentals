# AP3 - Questão 2


# Subprogramas
def produz(nm):
    vals = dict()
    dados = open(nm, "r", encoding="utf-8")
    for linha in dados:
        pals = linha.strip().split()
        for p in pals:
            if vals.get(p) == None:
                vals[p] = 1
            else:
                vals[p] += 1
    dados.close()
    return vals


def mostraOrdenado(vals):
    valores = list(vals)
    # Ordenar Vetor por Seleção
    for i in range(len(valores) - 1):
        ondeMenor = i
        for j in range(i + 1, len(valores)):
            if valores[j] < valores[ondeMenor]:
                ondeMenor = j
        valores[i], valores[ondeMenor] = valores[ondeMenor], valores[i]
    # Mostra Ordenado
    for p in valores:
        if vals[p] == 1:
            print(p, "ocorreu", vals[p], "vez")
        else:
            print(p, "ocorreu", vals[p], "vezes")


# Programa Principal
nome = input()
dicionarioPalavrasContagens = produz(nome)
mostraOrdenado(dicionarioPalavrasContagens)
