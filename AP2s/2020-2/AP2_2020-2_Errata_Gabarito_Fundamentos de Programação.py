# AP2X 2020.2 Questão 2

# Subprogramas
def processa(nm):
    def localiza(p, tabMeds):
        for i in range(len(tabMeds)):
            if tabMeds[i][3] == p:
                return i
        return -1

    def insere(medal, vals):
        if medal == "ouro":
            return (vals[0] + 1, vals[1], vals[2], vals[3])
        elif medal == "prata":
            return (vals[0], vals[1] + 1, vals[2], vals[3])
        else:
            return (vals[0], vals[1], vals[2] + 1, vals[3])

    tabMedalhas = []
    dados = open(nm, "r", encoding="utf-8")
    for linha in dados:
        pais, medalha, modalidade = linha.split("#")
        onde = localiza(pais, tabMedalhas)
        if onde == -1:
            tabMedalhas.append(insere(medalha, (0, 0, 0, pais)))
        else:
            tabMedalhas[onde] = insere(medalha, tabMedalhas[onde])
    dados.close()
    return tabMedalhas

def ordena(vals):
    def seleciona(p, vs):
        pos = p
        for i in range(p + 1, len(vs)):
            if vs[i] > vs[pos]:
                pos = i
        return pos

    vals = list(vals)
    for i in range(len(vals) - 1):
        posMenor = seleciona(i, vals)
        vals[i], vals[posMenor] = vals[posMenor], vals[i]
    return vals

def mostra(vals):
    print("Tabela:")
    for x in ordena(vals):
        print(x)
    print()
    return None


# Programa Principal
nome = input()
tabela = processa(nome)
mostra(tabela)
