# AP1 - Questão 3


# Subprograma

def ordenar(valores):  # Este é o mesmo método visto na Aula 7, porém aqui os subprogramas 'trocar' e 'selecionaMenor' foram incorporados ao subprograma 'ordenar'.
    for ind in range(len(valores) - 1):
        menor = ind
        for pos in range(ind + 1, len(valores)):
            if len(valores[pos]) < len(valores[menor]):  # A comparação é feita sobre o comprimento das strings e não sobre seu conteúdo. Entretanto, comparar o conteúdo também é válido, pois o resultado será o mesmo.
                menor = pos
        valores[ind], valores[menor] = valores[menor], valores[ind]


# Programa Principal
n = int(input())
linhas = [None] * n
for i in range(n):
    linhas[i] = input()

ordenar(linhas)

for i in range(n):
    print(linhas[i])
