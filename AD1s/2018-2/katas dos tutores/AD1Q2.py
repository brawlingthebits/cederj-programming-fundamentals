# AD1 - Questão 2


# Subprogramas
def contarVogaisDigitos(pals):
    qVogs, qDigs = 0, 0
    for p in pals:
        for letra in p:
            if letra in "0123456789":
                qDigs += 1
            elif letra.upper() in "AEIOU":
                qVogs += 1
    return qVogs, qDigs


def mostraPalavrasComQtdVogaisPares(pals):
    for p in pals:
        qVogs = 0
        for letra in p:
            if letra.lower() in "aeiou":
                qVogs += 1
        if qVogs > 0 and qVogs % 2 == 0:
            print(p)
    return None


# Programa Principal
frase = input()  # lê a primeira frase
while frase != "":
    palavras = frase.split()
    print("Palavras contidas:", len(palavras))
    qtdVogais, qtdDigitos = contarVogaisDigitos(palavras)
    print("Total de Vogais:", qtdVogais)
    print("Total de Dígitos:", qtdDigitos)
    mostraPalavrasComQtdVogaisPares(palavras)
    print()
    frase = input()  # lê a próxima frase