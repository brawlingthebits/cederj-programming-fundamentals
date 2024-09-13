# Programa - AD1.1Q2
# Subprogramas
# Principal
qtd = int(input())
soma = menor = maior = int(input())
for i in range(1, qtd):
    numero = int(input())
    soma += numero
    if numero < menor:
        menor = numero
    elif numero > maior:
        maior = numero
print("Soma:", soma)
print("Média: %.2f"%(soma/qtd))
print("Menor:", menor)
print("Maior:", maior)
