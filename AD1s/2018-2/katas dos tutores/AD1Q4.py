# AD1 - Questão 4


# Subprogramas
def lerCidades():
    n = int(input())
    cidades = [None] * n
    for i in range(n):
        par = input().split()
        cidades[i] = (par[0], int(par[1]))
    return cidades


def obterPopulacao(cidades, nome):
    n = len(cidades)
    for i in range(n):
        atual, populacao = cidades[i]
        if nome == atual:
            return populacao
    return -1


def obterCidadesGrandes(cidades, populacaoMinima):
    n = len(cidades)
    grande = [None] * n
    for i in range(n):
        _, populacao = cidades[i]
        grande[i] = populacao >= populacaoMinima
    return grande


def imprimirNomes(cidades, quais):
    n = len(cidades)
    for i in range(n):
        if quais[i]:
            nome, _ = cidades[i]
            print(nome)


# Programa Principal
print("Informe os dados de entrada:")
tuplas = lerCidades()

print("Indique o nome de uma cidade a ser consultada: ", end="")
consulta = input()
print("A população é de", obterPopulacao(tuplas, consulta),
      "pessoa(s).")

print("Indique a população mínima requerida: ", end="")
consulta = int(input())
imprimirNomes(tuplas, obterCidadesGrandes(tuplas, consulta))
