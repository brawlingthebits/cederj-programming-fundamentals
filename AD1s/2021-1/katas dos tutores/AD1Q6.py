# AD1 - Questão 6
# Programa Completo
# Subprogramas
def palindrome(frase):
    if len(frase) < 2:
        return True
    else:
        return frase[0] == frase[len(frase) - 1] and palindrome(frase[2:len(frase) - 2])


# Programa Principal
linha = input()
while linha != "":
    if palindrome(linha):
        print(linha)
    linha = input()