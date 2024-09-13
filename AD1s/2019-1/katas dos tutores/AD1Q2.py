# AD1 - Questão 2


# Programa Principal
linha = input()
numeros = linha.split()

soma = 0
for i in range(len(numeros)):
    numeros[i] = float(numeros[i])
    soma += numeros[i]

if len(numeros) == 0:
    print("Nenhum número foi digitado!!!")
else:
    media = soma/len(numeros)
    print("Média :", media)
    print("Listagem dos Números Acima da Média:")
    for item in numeros:
        if item > media:
            print("\t",item)
    print("Fim da Listagem")