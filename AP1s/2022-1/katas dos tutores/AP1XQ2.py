# AP1X - Q2
# Subprograma
def processaNome(lida):
    partesDoNome = lida.split()
    print(partesDoNome[0], partesDoNome[len(partesDoNome)-1])
    return None

# Programa Principal
qtdNomes = int(input())
for i in range(qtdNomes):
    nomeCompleto = input()
    processaNome(nomeCompleto)