# AP2 - Questão 1


# Subprogramas
def mostra(nm):
    dados = open(nm, "r")
    for linha in dados:
        print(linha, end = "")
    dados.close()


def produz(nmEnt1, nmEnt2, nmSai):
    dados1 = open(nmEnt1,"r")
    dados2 = open(nmEnt2, "r")
    dadosSaida = open(nmSai, "w")
    linha1 = dados1.readline()
    linha2 = dados2.readline()
    while linha1 != "" and linha2 !="":
        pontos1 = int(linha1.split()[0])
        pontos2 = int(linha2.split()[0])
        if pontos1 >= pontos2:
            dadosSaida.write(linha1)
            linha1 = dados1.readline()
        else:
            dadosSaida.write(linha2)
            linha2 = dados2.readline()
    while linha1 != "":
        dadosSaida.write(linha1)
        linha1 = dados1.readline()
    while linha2 != "":
        dadosSaida.write(linha2)
        linha2 = dados2.readline()
    dados1.close()
    dados2.close()
    dadosSaida.close()


# Programa Principal
nomeEntrada1, nomeEntrada2, nomeSaida = input().split()
produz(nomeEntrada1, nomeEntrada2, nomeSaida)
mostra(nomeSaida)