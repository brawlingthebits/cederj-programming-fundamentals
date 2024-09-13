# AD2 - Questão 1


# Subprogramas
def numerica(pal):
    for letra in pal:
        if letra not in "0123456789-+.":
            return False
    return pal.count(".") < 2 and \
           (pal.count("-") + pal.count("+") == 0 or \
           (pal.count("-") + pal.count("+") == 1 and pal[0] == "-" and len(pal) > 1)) or \
           (pal.count("-") + pal.count("+") == 1 and pal[0] == "+" and len(pal) > 1)


# Programa Principal
stringsNumericas = []
linha = input()
while linha != "":
    if numerica(linha):
        stringsNumericas.append(linha)
    linha = input()
print("Lista de Números Válidos Lidos =", stringsNumericas)
