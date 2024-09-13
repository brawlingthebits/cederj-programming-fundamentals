# AD1 - Questão 2


# Subprogramas
def primo(dado):
    if dado < 2:
        return False
    else:
        for divisor in range(2, 1 + int(dado ** 0.5)):
            if dado % divisor == 0:
                return False
        return True


# Programa Principal
numeros = list(map(int, input().split()))
if numeros == []:
    print("Nenhum Número Foi Lido!!!")
else:
    print("Relação dos Primos(s):")
    for x in numeros:
        if primo(x):
            print(x)
    print("Fim da Relação.")