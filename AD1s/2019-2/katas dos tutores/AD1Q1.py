# AD 1 - Questão 1


lida = input()
if lida == "":
    print("Quantidade de Números: 0")
else:
    qtdLidasNaoVazias = 0
    somaNumeros = 0
    maior = float(lida)
    while lida!="":
        qtdLidasNaoVazias += 1
        numeroAtual = float(lida)
        if numeroAtual > maior:
            maior = numeroAtual
        somaNumeros += numeroAtual
        lida = input()
    print("Quantidade de Números:", qtdLidasNaoVazias)
    print("Média dos Números:", somaNumeros/qtdLidasNaoVazias)
    print("Maior:", maior, "\n")