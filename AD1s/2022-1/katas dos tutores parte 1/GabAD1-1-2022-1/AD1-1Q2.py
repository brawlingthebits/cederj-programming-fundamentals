# Programa Completo - AD1-1Q2

# Subprogramas
def processa(numTeste, tam, min, max):
    print("Teste %d:" % numTeste)
    print("   Intervalo [%.1f, %.1f]"%(min, max))
    qtdMenores = qtdEntre = qtdMaiores = soma = 0
    for i in range(tam):
        valorLido = float(input())
        if valorLido < min:
            qtdMenores += 1
        elif valorLido > max:
            qtdMaiores += 1
        else:
            qtdEntre += 1
            soma += valorLido
    print("   Abaixo do Intervalo: %d, No Intervalo: %d, Acima do Intervalo: %d." % (qtdMenores, qtdEntre, qtdMaiores))
    print("   Soma dos Valores Dentro do Intervalo: %.1f"%soma)
    print()
    return None

# Principal
qtdTestes = int(input())
tamanhoCadaTeste = int(input())
valorMinimo = float(input())
valorMaximo = float(input())
for teste in range(1, qtdTestes+1):
    processa(teste, tamanhoCadaTeste, valorMinimo, valorMaximo)
