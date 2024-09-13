# AP1 - Questão 2 - Obs.: Este é um programa de referência. Existem outras formas de se resolver o problema.


def perfeito(x):
    soma = 0
    for y in range(1, x):
        if x % y == 0:
            soma += y
    return x == soma


n = int(input())

for i in range(n):
    k = int(input())
    if perfeito(k):
        print("O número %d é perfeito" % k)
    else:
        print("O número %d não é perfeito" % k)
