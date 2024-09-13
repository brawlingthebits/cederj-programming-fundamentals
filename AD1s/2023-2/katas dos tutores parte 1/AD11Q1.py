# Programa AD11Q1 - 2023.2
# Subprogramas
# Principal
qtdNumeros = int(input())
qtdPares = qtdImpares = somaPares = somaImpares = 0
menor = maior = None
for cadaLeitura in range(qtdNumeros):
    numeroLido = int(input())
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
print("Menor:", menor)
print("Maior:", maior)
if qtdPares == 0:
    print("Média dos Pares: 0.00")
else:
    print("Média dos Pares: %.2f"%(somaPares/qtdPares))
if qtdImpares == 0:
    print("Média dos Ímpares: 0.000")
else:
    print("Média dos Ímpares: %.3f"%(somaImpares/qtdImpares))
