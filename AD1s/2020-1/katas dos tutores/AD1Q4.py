# AD1 - Questão 4


# Subprograma
def mdc(a, b):
    if b == 0 or a == b:
        return a
    if a > b:
        return mdc(a - b, b)
    return mdc(a, b - a)


# Programa Principal
linha = input()
while linha != '-1 -1':
    a, b = linha.split()
    print(mdc(int(a), int(b)))
    linha = input()
