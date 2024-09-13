# Programa AP2Q2
# Subprogramas
def produz(nomeArq):
    primeiros = dict()
    ultimos = dict()
    arquivo = open(nomeArq, "r", encoding="utf-8")
    for nomeLido in arquivo:
        partesNome = nomeLido.strip("\n").split()
        prim = partesNome[0]
        ult = partesNome[len(partesNome) - 1]
        if prim in primeiros:
            primeiros[prim] += 1
        else:
            primeiros[prim] = 1
        if ult in ultimos:
            ultimos[ult] += 1
        else:
            ultimos[ult] = 1
    arquivo.close()
    return primeiros, ultimos


def listagemModa(msg, dicionario):
    print(msg, "da Moda:")
    vezesModa = 0
    for vezes in dicionario.values():
        if vezes > vezesModa:
            vezesModa = vezes
    for candidato in dicionario:
        if dicionario[candidato] == vezesModa:
            print("\t", candidato)
    return None


# Principal
nomeArquivo = input()
primeirosNomes, ultimosNomes = produz(nomeArquivo)
if len(primeirosNomes) == len(ultimosNomes) == 0:
    print("Arquivo Vazio!")
else:
    listagemModa("Nome(s)", primeirosNomes)
    listagemModa("Sobrenome(s)", ultimosNomes)
