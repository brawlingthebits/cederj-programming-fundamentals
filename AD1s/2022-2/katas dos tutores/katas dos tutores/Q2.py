# AD1.1.2022.2 - Questão 2

# Subprogramas
def converte(s):
    nums = []
    numsStr = s.split()
    for n in numsStr:
        nums.append(int(n))
    return nums


# Programa Principal
qtdLinhas = int(input())
if qtdLinhas == 0:
    print("Nenhum número foi lido, portanto, sem mínimo e máximo!!")
else:
    menor = maior = None
    for posLinha in range(qtdLinhas):
        lida = input()
        numeros = converte(lida)
        for valor in numeros:
            if menor == maior == None:
                menor = maior = valor
            elif valor < menor:
                menor = valor
            elif valor > maior:
                maior = valor
    print("Menor Número: %d e Maior Número: %d" % (menor, maior))
