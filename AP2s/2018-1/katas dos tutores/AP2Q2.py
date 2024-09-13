# AP2 - Questão 2

# Subprogramas


def produz(nm):
    pares = dict()
    dados = open(nm, "r")
    for linha in dados:
        palavras = linha.strip().split()
        for p in palavras:
            if pares.get(p) == None:
                pares[p] = 1
            else:
                pares[p] += 1
    dados.close()
    return pares


def mostra(pares):
    for p in sorted(pares.keys()):
        if pares[p] == 1:
            print(p,"ocorre", pares[p], "vez")
        else:
            print(p,"ocorre", pares[p], "vezes")
    return None


# Programa Principal
nomeArquivo = input("Escolha o nome do arquivo: ")
dicionario = produz(nomeArquivo)
mostra(dicionario)