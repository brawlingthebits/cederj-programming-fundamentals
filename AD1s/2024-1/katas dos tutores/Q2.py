# Programa AD1Q2
# Subprogramas
# Principal
qtdNumeros = int(input())
numLido = int(input())
soma = menor = maior = numLido
for i in range(qtdNumeros-1):
    numLido = int(input())
    soma += numLido
    if numLido < menor:
        menor = numLido
    elif numLido > maior:
        maior = numLido
print("Menor dos", qtdNumeros, "números lidos:",  menor)
print("Maior dos", qtdNumeros, "números lidos:", maior)
print("Média dos", qtdNumeros, "números lidos:",  "%.2f"%(soma/qtdNumeros))
