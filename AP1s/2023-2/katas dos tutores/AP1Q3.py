# Subprogramas
def converteParaInteiros(nums):
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    return None


# Principal
numeros = input().split()
converteParaInteiros(numeros)
qtdPares = qtdImpares = somaPares = 0 #somaImpares = 0
menor = maior = None
for numero in numeros:
    if menor == maior == None:
        menor = maior = numero
    elif numero < menor:
        menor = numero
    elif numero > maior:
        maior = numero
    if numero % 2 == 0:
        qtdPares += 1
        somaPares += numero
#    else:
#        qtdImpares += 1
#        somaImpares += numero
print("Menor:", menor)
print("Maior:", maior)
if qtdPares == 0:
    print("Média dos Pares: 0.0")
else:
    print("Média dos Pares: %.1f" % (somaPares / qtdPares))
#if qtdImpares == 0:
#    print("Média dos Ímpares: 0.0")
#else:
#    print("Média dos Ímpares: %.1f" % (somaImpares / qtdImpares))
