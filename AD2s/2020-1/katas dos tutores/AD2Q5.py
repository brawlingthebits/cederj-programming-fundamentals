# AD2 - Questão 5


# Subprogramas
def converter(x):
    if x != 0:
        return x % 2 + 10 * converter(x // 2)
    else:
        return 0


def multiplicar(x, y):
    if x != 0:
        return y + multiplicar(x - 1, y)
    else:
        return 0


def calcular(x):
    if x != 1:
        return 1.0/x + calcular(x - 1)
    else:
        return 1.0


# Programa Principal
a = int(input())
b, c = map(int, input().split())
n = int(input())

print(converter(a))
print(multiplicar(b, c))
print(calcular(n))