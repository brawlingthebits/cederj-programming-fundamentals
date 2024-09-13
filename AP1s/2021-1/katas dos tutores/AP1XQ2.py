# AP1X - Questão 2 - Valor 1.5
# Programa
# Subprogramas
def converte(nmCompleto):
    eliminaveis = ["e", "de", "da", "das", "do", "dos"]
    for tirar in eliminaveis:
        nmCompleto = nmCompleto.replace(" " + tirar + " ", " ")
    partes = nmCompleto.split()
    for i in range(1, len(partes) - 1):
        partes[i] = partes[i][0] + "."
    nmCompleto = ""
    for p in partes:
        nmCompleto = nmCompleto + p + " "
    return nmCompleto[0:len(nmCompleto) - 1]


# Programa Principal
nome = input()
while nome != "":
    print(converte(nome))
    nome = input()