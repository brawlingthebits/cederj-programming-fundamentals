# AD1 - Questão 1


# Subprogramas
def primo(n):
    if n < 2:
        return False
    else:
        for divisor in range(2, int(n ** 0.5) + 1):
            if n % divisor == 0:
                return False
        return True


# Programa Principal
numero = int(input())
if numero <= 0:
    print("Nenhum número maior que zero foi lido!!!")
else:
    qtdPares = qtdImpares = qtdPrimos = 0
    somaPares = somaImpares = somaPrimos = 0
    maior = numero
    while numero > 0:
        if numero % 2 == 0:
            qtdPares += 1
            somaPares += numero
        else:
            qtdImpares += 1
            somaImpares += numero
        if primo(numero):
            qtdPrimos += 1
            somaPrimos += numero
        if numero > maior:
            maior = numero
        numero = int(input())
    print("Maior Número Lido:", maior)
    if qtdPares > 0:
        print("Quantidade de Pares: %d com média: %.2f" % (qtdPares, somaPares / qtdPares))
    if qtdImpares > 0:
        print("Quantidade de Ímpares: %d com média: %.2f" % (qtdImpares, somaImpares / qtdImpares))
    if qtdPrimos > 0:
        print("Quantidade de Primos: %d com média: %.2f" % (qtdPrimos, somaPrimos / qtdPrimos))