# AD1 - Questão 4


# Subprogramas
def converteBinarioParaDecimal(numBinario):
    k = 0
    numConvertido = 0
    for d in reversed(numBinario):
        if d == '1':
            numConvertido += 2 ** k
        k += 1
    return numConvertido


def converteDecimalParaBase(numDecimal, base):
    if numDecimal != 0:
        numConvertido = ''
        while numDecimal > 0:
            resto = numDecimal % base
            numConvertido = str(resto) + numConvertido
            numDecimal = numDecimal // base
    else:
        numConvertido = '0'
    return numConvertido


def converte(numBinario, base):
    return converteDecimalParaBase(converteBinarioParaDecimal(numBinario), base)


# Programa Principal
s = input()
while s != '-1':
    for b in range(3, 10 + 1):
        r = converte(s, b)
        print(r, end=' ')
    print()
    s = input()
