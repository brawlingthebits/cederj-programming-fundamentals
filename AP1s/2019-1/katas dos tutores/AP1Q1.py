# AP1 - Questão 1


# Subprograma

def mostrar(vts):
    listagemVazia = True
    for i in range(len(vts)):
        if vts[i] != 0:
            listagemVazia = False
            print("Candidato", i, "obteve", vts[i], "voto(s)")
    if listagemVazia:
        print( "Nenhum voto ocorreu!!!")
    return None


# Programa Principal
votos = [0]*10
linha = input()
while linha != "":
    votos[int(linha)] += 1
    linha = input()
mostrar(votos)