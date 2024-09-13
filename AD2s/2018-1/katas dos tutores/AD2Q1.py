# AD2 - Questão 1

# Subprogramas para ordenação de candidatos


def selecionarVencedor(vals, inicio):
    escolhido = inicio
    for pos in range(inicio + 1, len(vals)):
        if vals[pos][2] > vals[escolhido][2] or (  # Decição por média
                vals[pos][2] == vals[escolhido][2] and vals[pos][1] > vals[escolhido][1]) or (  # Decisão por idade
                vals[pos][2] == vals[escolhido][2] and vals[pos][1] == vals[escolhido][1] and vals[pos][0] < vals[escolhido][0]):  # Decisão por nome
            escolhido = pos
    return escolhido


def ordenarCandidatos(lista):
    for ind in range(len(lista) - 1):
        vencedo = selecionarVencedor(lista, ind)
        lista[ind], lista[vencedo] = lista[vencedo], lista[ind]


# Programa principal

# Ler pesos
pesos = input().split()
for k in range(5):
    pesos[k] = float(pesos[k])

# Ler dados dos candidatos
candidatos = []
n = int(input())
for i in range(n):
    linha = input().split()
    nome = linha[0]
    idade = int(linha[1])
    media = 0
    for k in range(5):
        media += pesos[k] * float(linha[k + 2]) / 10
    candidatos.append((nome, idade, media))

# Ordernar candidatos utilizando Selecion Sort (algoritmo reescrito de forma enxuta)
ordenarCandidatos(candidatos)

# Exibir resultado
for i in range(n):
    print(candidatos[i][0])
