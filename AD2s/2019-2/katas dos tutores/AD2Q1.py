# AD2 - Questão 1


# Subprogramas
def palindromo(palavra):
    if len(palavra) < 2:
        return True
    else:
        return palavra[0] == palavra[len(palavra) - 1] and palindromo(palavra[1:len(palavra) - 1])


def mostraPalindromos(nm):
    dados = open(nm, "r")
    for linha in dados:
        palavras = linha.strip("\n").split()
        for pal in palavras:
            if palindromo(pal):
                print(pal)
    dados.close()
    return None


# Programa Principal
nome = input()
mostraPalindromos(nome)