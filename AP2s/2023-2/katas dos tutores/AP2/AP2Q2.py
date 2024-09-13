# Programa AP2 - Q2
# Subprogramas
def mostra(nmArq):
    print("Conteúdo em", nmArq + ":")
    arquivo = open(nmArq, "r")
    for linha in arquivo:
        print("\t", linha, end="")
    print()
    arquivo.close()
    return None

def procuraPalavraELinhas(nmArq):
    maior = listaLinhas = None
    arquivo = open(nmArq, "r")
    contagemLinha = 0
    for linha in arquivo:
        contagemLinha += 1
        palavras = linha.strip().split()
        for p in palavras:
            if maior == listaLinhas == None:
                maior = p
                listaLinhas = [contagemLinha]
            elif len(p) > len(maior):
                maior = p
                listaLinhas = [contagemLinha]
            elif p == maior:
                if p not in listaLinhas:
                    listaLinhas.append(contagemLinha)
    arquivo.close()
    return maior, listaLinhas

def respostas(palavra, listaLinhas):
    print("Palavra de Maior Comprimento:", palavra)
    print("Qual(is) Linha(s) Ocorreu:", end="")
    for posicao in listaLinhas:
        print(" %d"%posicao, end="")
    print()
    return None

# Principal
nomeArquivo = input()
mostra(nomeArquivo)
maisLonga, numerosDasLinha = procuraPalavraELinhas(nomeArquivo)
respostas(maisLonga, numerosDasLinha)