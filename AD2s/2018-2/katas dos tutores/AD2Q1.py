# AD2 - Questão 1

# Subprograma
def processa(nm):
    dados = open(nm, "r")
    primeiraLinha = dados.readline()
    if primeiraLinha == "":
        menorValor = maiorValor = mediaDeTodosValores = None
    else:
        menorValor = maiorValor = somaTodos = float(primeiraLinha)
        qtdNumeros = 1
        for linha in dados:
            valor = float(linha)
            somaTodos += valor
            qtdNumeros += 1
            if valor < menorValor:
                menorValor = valor
            elif valor > maiorValor:
                maiorValor = valor
        mediaDeTodosValores = somaTodos/qtdNumeros
    dados.close()
    return menorValor, mediaDeTodosValores, maiorValor


# Programa Principal
nome = input()
menor, media, maior = processa(nome)
print("Menor Valor =",menor)
print("Média dos Valores =", media)
print("Maior Valor =", maior)