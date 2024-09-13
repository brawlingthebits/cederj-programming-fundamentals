# AP2 - Questão 2


# Subprogramas
def produz(nm):
    vals = dict()
    dados = open(nm, "r")
    for linha in dados:
        palavras = linha.strip().split()
        for palavra in palavras:
            if vals.get(palavra) == None:
                vals[palavra] = 1
            else:
                vals[palavra] += 1
    dados.close()
    return vals


def maisFrequente(vals):
    if vals == {}:
        print("Nenhuma palavra no arquivo!!!")
    else:
        maisOcorre = None
        vezesMaisOcorre = -1
        for palavra in vals:
            if vals[palavra] > vezesMaisOcorre:
                maisOcorre = palavra
                vezesMaisOcorre = vals[palavra]
        print("Mais Frequente foi:", maisOcorre, "ocorreu", vezesMaisOcorre, "vez(es)")


def mostraConjuntoDasPalavrasOrdenado(vals):
    def mostrar(vs):
        for p in vs:
            print(p)

    def ordenar(vs):        # Selection Sort - Ordenação por Seleção
        for i in range(len(vs) - 1):
            posMenor = i                              # Seleciona
            for j in range(i+1, len(vs)):             # Seleciona
                if vs[j] < vs[posMenor]:              # Seleciona
                    posMenor = j                      # Seleciona
            vs[i], vs[posMenor] = vs[posMenor], vs[i] # Troca

    palavras = list(vals)
    ordenar(palavras)
    mostrar(palavras)


# Programa Principal
nome = input()
pares = produz(nome)
mostraConjuntoDasPalavrasOrdenado(pares)
maisFrequente(pares)