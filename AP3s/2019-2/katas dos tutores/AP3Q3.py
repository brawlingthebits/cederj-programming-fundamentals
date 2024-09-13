# AP3 - Questão 3


# Subprograma
def converter(num):
    if num != 0:
        if num % 2 == 0:
            return converter(num // 2) + '0'
        else:
            return converter(num // 2) + '1'
    return ''


# Programa Principal
decimal = int(input())
binario = converter(decimal)
print(binario)
