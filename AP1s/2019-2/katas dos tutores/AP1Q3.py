# AP1 - Questão 3


# Subprograma
def ordenar(valores):  # Esse é o método da bolha com saída rápida. O método da bolha simples também foi aceito na correção.
    tamanho = len(valores) - 1
    troquei = True
    while troquei:
        troquei = False
        for i in range(tamanho):
            if valores[i] < valores[i + 1]:
                valores[i], valores[i + 1] = valores[i + 1], valores[i]
                troquei = True
        tamanho -= 1 


# Programa Principal
palavras = []

n = int(input())
for i in range(n):
    palavras.append(input())

ordenar(palavras)

for i in range(n):
    print(palavras[i])
