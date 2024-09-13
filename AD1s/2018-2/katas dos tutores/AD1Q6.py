# AD1 - Questão 6


# Subprogramas
def indicePrimeiro(valores, meio):
    atual = meio
    while atual > 0 and valores[atual - 1] == valores[meio]:
        atual -= 1
    return atual


def indiceUltimo(valores, meio):
    atual = meio
    while atual < (len(valores) - 1) and valores[atual + 1] == valores[meio]:
        atual += 1
    return atual


def buscar(valores, procurado):
    inicio = 0
    fim = len(valores) - 1
    meio  = (inicio + fim) // 2
    while inicio < fim and procurado != valores[meio]:
        if procurado > valores[meio]:
            inicio = meio + 1
        else:
            fim = meio - 1
        meio = (inicio + fim) // 2
    if procurado != valores[meio]:
        local = -1, -1
    else:
        local = indicePrimeiro(valores, meio), indiceUltimo(valores, meio)
    return local




# Programa Principal
lista = input().split()
for i in range(len(lista)):
    lista[i] = int(lista[i])
x = int(input())

a, b = buscar(lista, x)
print(a, b)
