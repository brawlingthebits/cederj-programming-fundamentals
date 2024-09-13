# APX1 - Questão 1


# Sub-programas
def maisVogaisMinusculasQueDigitos(x):
    qtdVogaisMinusculas = qtdDigitos = 0
    for letra in x:
        if letra in "aeiou":
            qtdVogaisMinusculas += 1
        elif letra in "0123456789":
            qtdDigitos += 1
    return qtdVogaisMinusculas > qtdDigitos


# Programa Principal
qtdLidas = qtdLidasMaisVogaisQueDigitos = 0
lida = input()
while lida != "":
    qtdLidas += 1
    if maisVogaisMinusculasQueDigitos(lida):
        qtdLidasMaisVogaisQueDigitos += 1
        print(lida)
    lida = input()
print("Total de linhas lidas:", qtdLidas)
print("Total de linhas com mais vogais que dígitos:", qtdLidasMaisVogaisQueDigitos)