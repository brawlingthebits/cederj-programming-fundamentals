# AP2 - Questão 1


# Subprogramas
def temRepetida(pal):
    for letra in pal:
        if pal.count(letra) > 1:
            return True
    return False


# Programa Principal
conjuntoDeStringsComCaracteresRepetidos = set()
nomeArquivo = input()
dados = open(nomeArquivo, "r")
for linha in dados:
    palavras = linha.strip().split()
    for pal in palavras:
        if temRepetida(pal):
            conjuntoDeStringsComCaracteresRepetidos.add(pal)
dados.close()
if conjuntoDeStringsComCaracteresRepetidos == set():
    print("Nenhuma palavra com caracteres repetidos foi encontrada!!!")
else:
    print("Palavras com caracteres repetidos = ", conjuntoDeStringsComCaracteresRepetidos)