# Programa Completo - Prova 2 - Questão 2 - 2022.1
# Subprogramas
def listaOcorrencias(pal, nm):
    print("Ocorrências da palavra", pal, "no arquivo", nm + ":")
    dados = open(nm, "r", encoding="utf-8")
    contaLinha = 0
    for linhaLida in dados:
        contaLinha += 1
        palavras = linhaLida.strip(",").strip(".").strip("\n").split()
        for contaPosicaoNaLinha in range(len(palavras)):
            if pal == palavras[contaPosicaoNaLinha]:
                print("   Linha: %d, Palavra %d nesta linha!"%(contaLinha, contaPosicaoNaLinha + 1))
    dados.close()
    print()
    return None


# Principal
nomeArquivo = input()
palavra = input()
listaOcorrencias(palavra, nomeArquivo)
