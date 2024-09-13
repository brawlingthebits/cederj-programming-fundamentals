# AD1 - Questão 1


# Programa Principal
qtdNumeros = int(input())
if qtdNumeros <= 0:
    menor = "Nenhum"
    media = "Nenhuma"
    maior = "Nenhum"
else:
    menor = maior = soma = float(input())
    for proximo in range(1, qtdNumeros):
        valor = float(input())
        soma += valor
        if valor < menor:
            menor = valor
        elif valor > maior:
            maior = valor
    media = soma / qtdNumeros
print("Menor Lido:", menor)
print("Média dos Lidos:", media)
print("Maior Lido:", maior)