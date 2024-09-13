# AP2 - Questão 2


# Subprogramas
def produz(nome):
    palsOcs = dict()
    dados = open(nome, "r")
    for linha in dados:
        palavras = linha.strip().split()
        for pal in palavras:
            if palsOcs.get(pal) == None:
                palsOcs[pal] = 1
            else:
                palsOcs[pal] += 1
    dados.close()
    return palsOcs


def mostra(dicio, mensagem):
    if dicio == {}:
        print("O dicionário está vazio!!!")
    else:
        print(mensagem)
        for chave, ocorrencia in sorted(dicio.items()):
            print("\t", chave, "ocorreu", ocorrencia, end = " ")
            if ocorrencia == 1:
                print("vez")
            else:
                print("vezes")


def remove(dicio):
    excluirChaves = []
    for (chave, valor) in dicio.items():
        if len(chave)%2 == 0:
            excluirChaves.append(chave)
    for chave in excluirChaves:
        dicio.pop(chave)


# Programa Principal
nomeDoArquivo = input()
dicionario = produz(nomeDoArquivo)
mostra(dicionario, "Dicionário ordenado pelas palavras:")
remove(dicionario)
mostra(dicionario, "Dicionário, após remover chaves de comprimento par, ordenado pelas palavras:")