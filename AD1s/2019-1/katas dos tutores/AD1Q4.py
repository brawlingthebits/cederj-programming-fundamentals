# AD1 - Questão 3


# Subprograma
def converte(numDecimal, base):
    if numDecimal != 0:
        numConvertido = ""
        while numDecimal > 0:
            resto = numDecimal % base
            numConvertido = str(resto) + numConvertido
            numDecimal = numDecimal // base
    else:
        numConvertido = "0"
    return numConvertido


# Programa Principal
n = int(input())
while n != -1:
    for b in range(2, 9 + 1):
        r = converte(n, b)
        print(r, end=" ")
    print()
    n = int(input())