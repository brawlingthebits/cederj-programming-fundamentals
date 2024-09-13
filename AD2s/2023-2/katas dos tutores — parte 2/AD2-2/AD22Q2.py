# Programa AD22Q2 - 2023.2
# Subprogramas
def localiza(p, lista):
    for i in range(len(lista)):
        if p == lista[i][0]:
            return i
    return None

def contar(pals, nmArq):
    listaPalsOcs = []
    for pal in pals:
        listaPalsOcs.append([pal, 0])
    arquivo = open(nmArq, "r", encoding="utf-8")
    for linha in arquivo:
        palavrasNaLinha = linha.strip("\n").split()
        for pal in palavrasNaLinha:
            onde = localiza(pal, listaPalsOcs)
            if onde != None:
                listaPalsOcs[onde][1] += 1
    arquivo.close()
    return listaPalsOcs

def mostrar(listaPalsOcs):
    print("Listagem das Ocorrências das Palavras:")
    for [palavra, vezes] in listaPalsOcs:
        print("   ", palavra, "ocorreu",vezes, "vez(es)")
    return None

# Principal
nomeArquivo = input()
palavras = input().split()
listaDePalavrasComContagens = contar(palavras, nomeArquivo)
mostrar(listaDePalavrasComContagens)
