# AP1X - Q2
# Subprogramas
def maisFrequente(palsOcs):
    maisVezes = palsOcs[0][1]
    for i in range(len(palsOcs)):
        if palsOcs[i][1]>maisVezes:
            maisVezes = palsOcs[i][1]
    return maisVezes

def localiza(procurada, psOcs):
    for i in range(len(psOcs)):
        if procurada == psOcs[i][0]:
            return i
    return None

def atualiza(palsOcs, pal):
    onde = localiza(pal, palsOcs)
    if onde == None:
        palsOcs.append([pal, 1])
    else:
        palsOcs[onde][1] += 1
    return None

# Programa Principal
qtdLinhas = int(input())
palavrasOcorrencias = []
for i in range(qtdLinhas):
    palavras = input().split()
    for p in palavras:
        atualiza(palavrasOcorrencias, p.upper())
if palavrasOcorrencias == []:
    print("Nenhuma Palavra Foi Lida!!!")
else:
    vezesMaisFrequente = maisFrequente(palavrasOcorrencias)
    for [palavra, vezes] in palavrasOcorrencias:
        if vezes == vezesMaisFrequente:
            print(palavra)
    print("Ocorreu(ram)", vezesMaisFrequente, "vez(es)")