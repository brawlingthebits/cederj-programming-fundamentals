# AP1 - Questão 3 - Obs.: Este é um programa de referência. Existem outras formas de se resolver o problema.

strs = input().split()
n = int(strs[0])
m = int(strs[1])
k = 1

while n != 0 or m != 0:
    acumulado = [0] * (n + 1)
    for i in range(n):
        acumulado[i+1] = acumulado[i] + int(input())

    maior = 0
    menor = acumulado[n]
    for i in range(n-m+1):
        soma = acumulado[i+m] - acumulado[i]
        if maior < soma:
            maior = soma
        if menor > soma:
            menor = soma

    print('Cidade %d' % k)
    print('%1.2f %1.2f' % (menor / m, maior / m))
    print()

    strs = input().split()
    n = int(strs[0])
    m = int(strs[1])
    k += 1
