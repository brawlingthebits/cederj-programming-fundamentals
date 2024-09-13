# AD2 - Questão 3


# Subprogramas
def contemTodas(conjCars, palavra):
    for caracter in conjCars:
        if caracter not in palavra:
            return False
    return True


def produz(nome, conj):
    palsOcs = dict()
    dados = open(nome, "r")
    for linha in dados:
        palavras = linha.strip().split()
        for pal in palavras:
            if contemTodas(conj, pal):
                if palsOcs.get(pal) == None:
                    palsOcs[pal] = 1
                else:
                    palsOcs[pal] += 1
    dados.close()
    return palsOcs


def mostra(dicio, conj):
    if dicio == {}:
        print("O dicionário está vazio!!!")
    else:
        print("Listagem do dicionário das palavras contendo", str(conj)+":")
        for chave, ocorrencia in sorted(dicio.items()):
            print("\t", chave, "ocorreu", ocorrencia, end = " ")
            if ocorrencia == 1:
                print("vez")
            else:
                print("vezes")


# Programa Principal
nomeDoArquivo = input()
conjuntoLido = set(input())
dicionario = produz(nomeDoArquivo, conjuntoLido)
mostra(dicionario, conjuntoLido)
