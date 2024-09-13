# AD 1 - Questão 3


# Subprogramas
def contruir(qL, qC, min, max):
    from random import randint
    vals = []
    for lin in range(qL):
        linhaDeValores = []
        for col in range(qC):
            linhaDeValores.append(randint(min, max))
        vals.append(linhaDeValores)
    return vals


def mostrar(vals):
    for lin in range(len(vals)):
        for col in range(len(vals[lin])-1):
            print(vals[lin][col], end = " ")
        print(vals[lin][len(vals[lin])-1])
    print()


def localizaMaior(vals):
    pos, mVal = (0,0), vals[0][0]
    for lin in range(len(vals)):
        for col in range(len(vals[lin])):
            if vals[lin][col]> mVal:
                pos, mVal = (lin, col), vals[lin][col]
    return pos, mVal


def mostraSomaDeCadaLinha(vals):
    def somar(vs):
        total = 0
        for x in vs:
            total += x
        return total

    for lin in range(len(vals)):
        print("Soma da Linha", lin, "=", somar(vals[lin]))
    print()


def mostraSomaDeCadaColuna(vals):
    def somarColuna(c, vs):
        total = 0
        for lin in range(len(vs)):
            total += vs[lin][c]
        return total

    for col in range(len(vals[0])):
        print("Soma da Coluna", col, "=", somarColuna(col, vals))
    print()


# Programa Principal
qtdLinhas, qtdColunas = map(int, input().split())
valores = contruir(qtdLinhas, qtdColunas, 100, 999)
mostrar(valores)
posicao, maior = localizaMaior(valores)
print("Posição do Maior:", posicao, "Maior Valor:", maior,"\n")
mostraSomaDeCadaLinha(valores)
mostraSomaDeCadaColuna(valores)
