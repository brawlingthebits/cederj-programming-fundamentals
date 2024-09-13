# APX1 - Questão 2


# Sub-programas
def perfeito(x):
    soma = 1
    for divisor in range(2, 1 + x // 2):
        if x % divisor == 0:
            soma += divisor
    return x > 1 and soma == x


# Programa Principal
valores = list(map(int, input().split()))
if valores == []:
    print("Nenhum Número Foi Lido!!!")
else:
    print("Relação de Números Perfeitos:")
    for valor in valores:
        if perfeito(valor):
            print(valor)
    print("Fim da Relação.")