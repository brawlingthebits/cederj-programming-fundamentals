# AD1 - Questão 3


# Subprogramas
def lerMatriz():
    vals = []
    numeros = list(map(float, input().split()))
    while numeros != []:
        vals.append(numeros)
        numeros = list(map(float, input().split()))
    return vals


def mostra(vals):
    print("Conteúdo da Matriz:")
    for lin in range(len(vals)):
        for col in range(len(vals[lin])-1):
            print("%.2f"%vals[lin][col], end = " ")
        print("%.2f"%vals[lin][len(vals[lin])-1])
    print()


def extremos(vals):
    pequeno = grande = vals[0]
    for x in vals:
        if x < pequeno:
            pequeno = x
        elif x > grande:
            grande = x
    return pequeno, grande


# Programa Principal
valores = lerMatriz()
mostra(valores)
menor = maior = valores[0][0]
for i in range(len(valores)):
    menorNaLinha, maiorNaLinha = extremos(valores[i])
    print("Menor e Maior da Linha %d: %.2f e %.2f" % (i + 1, menorNaLinha,
maiorNaLinha))
    if menorNaLinha < menor:
        menor = menorNaLinha
    if maiorNaLinha > maior:
        maior = maiorNaLinha
print("Menor e Maior de Toda a Matriz: %.2f e %.2f" % (menor, maior))