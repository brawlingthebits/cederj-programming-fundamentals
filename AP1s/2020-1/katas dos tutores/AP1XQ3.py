# APX1 - Questão 3


# Subprograma
def metodo_da_bolha(valores):
    for tam in range(len(valores) - 1, 0, -1):
        for i in range(tam):
            if valores[i] > valores[i + 1]:
                valores[i], valores[i + 1] = valores[i + 1], valores[i]


# Programa Principal
n = int(input())
lista = list()
for i in range(n):
    palavra, numero = input().split()
    lista.append((palavra, float(numero)))

metodo_da_bolha(lista)

for palavra, numero in lista:
    print('%s %f' % (palavra, numero))