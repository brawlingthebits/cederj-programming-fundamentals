# Programa Completo
# Subprogramas
def palindromo(frase):
    if len(frase) < 2:
        return True
    else:
        return frase[0] == frase[len(frase) - 1] and palindromo(frase[2:len(frase) - 2])


# Programa Principal
linha = input()
while linha != "":
    if palindromo(linha):
        print(linha)
    linha = input()