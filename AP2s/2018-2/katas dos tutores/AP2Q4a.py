# AP2 - Questão 4a - Obs.: Execute o programa para ver o resultado


def teste(v, tam):
    for k in range(tam):
        v[k] = 0


vet = [-5, 3, 2, 9, 2, 2]
j = 4

valores = 0
for i in range(j):
    if vet[i] == 2:
        valores = valores + 2

print(valores)

for i in range(6):
    vet[i] = j
    j = j - 1

for i in range(len(vet)):
    print("%i " % vet[i], end="")
print()

teste(vet, 3)
for i in range(6):
    print("%i " % vet[i], end="")