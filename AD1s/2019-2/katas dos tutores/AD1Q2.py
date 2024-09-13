# AD 1 - Questão 2


# Subprogramas
def contar(pInicial,vals):
    total = 1
    for p in range(pInicial+1, len(vals)):
        if vals[pInicial] == vals[p]:
            total += 1
    return total


def encontraModaComFrequencia(vals):
    valorDaModa, maisFrequente = None, 0
    for i in range(len(vals)):
        qtdVezes = contar(i, vals)
        if qtdVezes > maisFrequente:
            valorDaModa, maisFrequente = vals[i], qtdVezes
    return valorDaModa, maisFrequente


# Programa Principal
numeros = list(map(float, input().split()))
if len(numeros)==0:
    print("nenhum número foi lido!!!")
else:
    moda, vezes = encontraModaComFrequencia(numeros)
    print("Valor que mais ocorreu:",moda, "que foi encontrado:", vezes, "vez(es)\n")