# AD2.2022.2 - Questão 2
# Programa Completo
# Subprogramas
def produzListaPalsFreqsIniciadosPorLetras(nm, iniciais):
    def localiza(p, lPs):
        for posicao in range(len(lPs)):
            if p == lPs[posicao][0]:
                return posicao
        return None

    lPals = list()
    dados = open(nm, "r", encoding="utf-8")
    for linha in dados:
        palavras = linha.strip().split()
        for pal in palavras:
            if pal[0] in iniciais:
                onde = localiza(pal, lPals)
                if onde == None:
                    lPals.append([pal, 1])
                else:
                    lPals[onde][1] += 1
    dados.close()
    return lPals


def mostraOrdenado(lPals):
    lPals.sort()
    print("Conteúdo Ordenado das Palavras e Respectivas Ocorrências:")
    for [palavra, frequencia] in lPals:
        print(palavra, "ocorre", frequencia, end=" ")
        if frequencia == 1:
            print("vez")
        else:
            print("vezes")
    print()
    return None


# Principal
nomeArquivo = input()
listaPalsFreqs = produzListaPalsFreqsIniciadosPorLetras(nomeArquivo, "AEIOUaeiou")
mostraOrdenado(listaPalsFreqs)
