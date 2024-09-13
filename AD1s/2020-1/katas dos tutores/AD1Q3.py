# AD1 - Questão 3


# Subprogramas
def constroi(qL, qC, min, max):
    from random import randint
    vals = []
    for lin in range(qL):
        novaLinha = []
        for col in range(qC):
            novaLinha.append(randint(min, max))
        vals.append(novaLinha)
    return vals


def mostra(vals):
    print("Conteúdo da Matriz:")
    for lin in range(len(vals)):
        for col in range(len(vals[lin]) - 1):
            print(vals[lin][col], end=" ")
        print(vals[lin][len(vals[lin]) - 1])
    print()


def media(vals):
    soma = 0
    for linha in vals:
        for valor in linha:
            soma += valor
    return soma / (len(vals) * len(vals[0]))


def mostraValoresBordaAcimaCota(vals, cotaMinima):
    print("Relação de Valores nas Bordas Acima da Média:")
    for lin in range(len(vals)):
        for col in range(len(vals[lin])):
            if vals[lin][col] > cotaMinima and (
                    lin == 0 or lin == len(vals) - 1 or col == 0 or col == len(vals[lin]) - 1):
                print(vals[lin][col])


# Programa Principal
qtdLinhas, qtdColunas, valorMinimo, valorMaximo = map(int, input().split())
valores = constroi(qtdLinhas, qtdColunas, valorMinimo, valorMaximo)
mostra(valores)
valorMedio = media(valores)
print("Média dos Valores Sorteados:\n%.1f" % valorMedio, "\n")
mostraValoresBordaAcimaCota(valores, valorMedio)