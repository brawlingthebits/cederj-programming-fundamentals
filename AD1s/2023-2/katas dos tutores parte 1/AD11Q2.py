# Programa AD11Q2 - 2023.2
# Subprogramas
# Principal
qtdPares = qtdImpares = somaPares = somaImpares = 0
menor = maior = None
linhaLida = input()
while linhaLida != "":
    numeroLido = int(linhaLida)
    if menor == maior == None:
        menor = maior = numeroLido
    elif numeroLido < menor:
        menor = numeroLido
    elif numeroLido > maior:
        maior = numeroLido
    if numeroLido % 2 == 0:
        qtdPares += 1
        somaPares += numeroLido
    else:
        qtdImpares += 1
        somaImpares += numeroLido
    linhaLida = input()
print("Menor:", menor)
print("Maior:", maior)
if qtdPares == 0:
    print("Média dos Pares: 0.00")
else:
    print("Média dos Pares: %.2f" % (somaPares / qtdPares))
if qtdImpares == 0:
    print("Média dos Ímpares: 0.0")
else:
    print("Média dos Ímpares: %.1f" % (somaImpares / qtdImpares))
