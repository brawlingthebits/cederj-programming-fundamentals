# AP1X - Questão 1 - Valor 1.5

n = int(input())

def formas_subir(n):
    formas = []
    formas.append(1)
    formas.append(2)
    for i in range(2, n):
        formas.append(formas[i-1] + formas[i-2])
    return formas[n-1]

saida = formas_subir(n)

print(f"Posso subir a escada de {n} degraus de {saida} formas")