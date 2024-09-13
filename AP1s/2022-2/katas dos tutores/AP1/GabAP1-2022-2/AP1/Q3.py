# Programa AP1Q3 - 2022.2 - Maior Sequência Adjacente Crescente
# Subprogramas
def converteEmListaDeInteiros(lis):
    for i in range(len(lis)):
        lis[i] = int(lis[i])
    return None

def cresce(p, lis):
    total = 1
    for i in range(p, len(lis)-1):
        if lis[i] < lis[i+1]:
            total += 1
        else:
            return total
    return total

def achaMaiorSequencia(lis):
    comeco = tamanho = 0
    for i in range(len(lis)):
        tamAtual = cresce(i, lis)
        if tamAtual > tamanho:
            tamanho = tamAtual
            comeco = i
    return comeco, tamanho

def mostra(lis, comeco, tamanho):
    print("Maior Sequência Crescente:", end="")
    for i in range(comeco, comeco+tamanho):
        print("%4d"%lis[i], end = "")
    print()
    return None

# Principal
numeros = input().split()
converteEmListaDeInteiros(numeros)
inicioMaiorSequencia, tamanhoMaiorSequencia = achaMaiorSequencia(numeros)
mostra(numeros, inicioMaiorSequencia, tamanhoMaiorSequencia)
