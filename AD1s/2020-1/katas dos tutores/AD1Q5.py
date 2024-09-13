# AD1 - Questão 5

from random import randint


# Subprograma
def busca_com_sentinela(valores, procurado):
    indice = 0
    while valores[indice] != procurado:
        indice = indice + 1
    if indice == len(valores) - 1:
        local = -1
    else:
        local = indice
    return local


# Programa Principal
n = int(input())
numeros = []
for i in range(n):
    numeros.append(randint(0, 10))

k = randint(0, 10)
numeros.append(k)

indice = busca_com_sentinela(numeros, k)

print('Valores: ', end='')
for i in range(n):
    print(numeros[i], end=' ')
print()

print('K: %d' % k)

if indice != -1:
    print('Índices: %d' % indice)
else:
    print('Valor não encontrado')