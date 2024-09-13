# AP2X - Questão 2


# Subprogramas
def carrega(nm):
    vals = []
    dados = open(nm, "r")
    for linha in dados:
        vals.append(list(map(int, linha.split())))
    dados.close()
    return vals


def maiores(vals):
    def maior(vs):
        vMaior = vs[0]
        for x in vs:
            if x > vMaior:
                vMaior = x
        return vMaior
    numLinha = 0
    for linha in vals:
        numLinha += 1
        print("Maior da Linha", str(numLinha)+":", maior(linha))
    return None


def media(vals):
    qtd = len(vals)*len(vals[0])
    soma = 0
    for linha in vals:
        for valor in linha:
            soma += valor
    return soma/qtd


def acima(cota, vals):
    print("Linha(s) com média(s) acima da Média Geral:")
    for linha in vals:
        if media([linha]) > cota:
            for x in linha:
                print(x, end = " ")
            print()


# Programa Principal
nome = input()
valores = carrega(nome)
maiores(valores)
mediaGeral = media(valores)
print("Média Geral:", mediaGeral)
acima(mediaGeral, valores)