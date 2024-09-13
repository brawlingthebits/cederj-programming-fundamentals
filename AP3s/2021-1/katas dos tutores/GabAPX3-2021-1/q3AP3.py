# Programa AP3X - Questão 3
# Subprogramas
def mostra(nm):
    dados = open(nm, "r", encoding="utf-8")
    print("Conteúdo do Arquivo:", nm)
    for linha in dados:
        print(linha, end="")
    print()
    dados.close()
    return None

def produz(nm, minimo, maximo):
    dicioPals = dict()
    dados = open(nm, "r", encoding="utf-8")
    for linha in dados:
        linha = linha.upper().replace(",","").strip("\n")
        palavras = linha.split()
        for pal in palavras:
            if minimo <= len(pal) <= maximo:
                if dicioPals.get(pal) == None:
                    dicioPals[pal] = 1
                else:
                    dicioPals[pal] += 1
    dados.close()
    return dicioPals

def mostraDicionarioOrdenado(dicioPals):
    print("Dicionário de Palavras com Contagem de Ocorrências:")
    for pal, vezes in sorted(dicioPals.items()):
        print(pal, "ocorreu", vezes, end = " ")
        if vezes == 1:
            print("vez")
        else:
            print("vezes")
    print()
    return None

# Principal
nome = input()
tamanhoMinimo, tamanhoMaximo = map(int, input().split())
mostra(nome)
dicionarioDePalavrasComFrequencia = produz(nome, tamanhoMinimo,tamanhoMaximo)
mostraDicionarioOrdenado(dicionarioDePalavrasComFrequencia)
