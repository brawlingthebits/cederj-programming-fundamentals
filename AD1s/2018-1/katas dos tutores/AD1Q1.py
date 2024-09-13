"""
Q1: Leia números inteiros do teclado até que um número negativo seja teclado. Escreva, caso
existam, quais os cinco maiores números lidos. Caso menos que cinco números sejam lidos,
mostre todos os números lidos.
Restrição: Não é permitido manter em memória mais que seis números lidos.
"""


# Subprogramas
def removerMenor(nums):
    if len(nums) > 0:
        ondeMenor = localizaMenor(nums)
        nums.pop(ondeMenor)
    return None


def localizaMenor(nums):
    pos = 0
    for i in range(len(nums)):
        if nums[i] < nums[pos]:
            pos = i
    return pos


def mostrar(nums):
    if len(nums) == 0:
        print("Nenhum número lido, apenas o delimitador de fim!!!")
    else:
        print("O(s) " + str(len(nums)) + " maior(es) número(s) lido(s):")
        for num in nums:
            print(num)
    return None


# Programa Principal
numerosMaiores = []
lido = int(input())

while lido >= 0:
    numerosMaiores.append(lido)
    if len(numerosMaiores) > 5:
        removerMenor(numerosMaiores)
    lido = int(input())

mostrar(numerosMaiores)