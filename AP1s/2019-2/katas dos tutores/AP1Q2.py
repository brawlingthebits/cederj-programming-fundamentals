# AP1 - Questão 2


# Subprograma
def maior(vals):
    valorMaior = vals[0]
    for valorAtual in vals:
        if valorAtual > valorMaior:
            valorMaior = valorAtual
    return valorMaior


# Programa Principal
soma = qtd = 0

entrada = input()
while entrada != "":
    numeros = list(map(int, entrada.split()))
    maiorValor = maior(numeros)
    print("Maior:", maiorValor)
    soma += maiorValor
    qtd += 1
    entrada = input()

if qtd == 0:
    print("Nenhum número foi lido!!!")
else:
    print("Média dos Valores:", soma / qtd)