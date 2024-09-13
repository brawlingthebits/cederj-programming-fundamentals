# AP1 - Questão 1


# Subprogramas
def contagemParDeVogais(p):
    total = 0
    for letra in p:
        if letra.upper() in "AEIOU":
            total += 1
    return total % 2 == 0


def inverte(p):
    resposta = ""
    for letra in p:
        resposta = letra + resposta
    return resposta


def processa(frase):
    palavras = frase.split()
    for pal in palavras:
        if contagemParDeVogais(pal):
            print(pal, end=" ")
        else:
            print(inverte(pal), end=" ")
    print("\n")
    return None


# Programa Principal
stringLida = input()
while stringLida != "":
    processa(stringLida)
    stringLida = input()