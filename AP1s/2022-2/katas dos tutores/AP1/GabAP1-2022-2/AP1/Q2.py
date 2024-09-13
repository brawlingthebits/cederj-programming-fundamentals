# Programa AP1Q2 - 2022.2 - Contagem de Vogais e Frase com Mais Vogais
# Subprogramas
def contaVogais(frase):
    total = 0
    for letra in frase:
        if letra in "aeiouAEIOU":
            total += 1
    return total

# Principal
lida = input()
if lida == "":
    print("Nenhuma linha lida com conteúdo!")
else:
    posicaoLinha = 0
    comMaisVogais = lida
    qtMaisVogais = contaVogais(lida)
    while lida != "":
        posicaoLinha += 1
        qtAtual = contaVogais(lida)
        print("A linha %d possui %d vogais"%(posicaoLinha, qtAtual))
        if qtAtual > qtMaisVogais:
            qtMaisVogais = qtAtual
            comMaisVogais = lida
        lida = input()
    print("Portanto, a linha lida com mais vogais foi:")
    print(comMaisVogais)
