# AD2 - Questão 2


# Subprogramas
def constroi(nome):
    lista = []
    dados = open(nome, "r")
    for linha in dados:
        campos = linha.strip().split()
        lista.append((campos[0], int(campos[1]), float(campos[2])))
    dados.close()
    return lista


def mostra(valores, msg):
    print("----- Listagem dos Produtos " + msg + " -----")
    for produto in valores:
        print(produto)
    print("-"*(34+len(msg)))


def localiza(vs, inicio, campo):
    locMenor = inicio
    for p in range(inicio+1, len(vs)):
        if vs[p][campo] < vs[locMenor][campo]:
            locMenor = p
    return locMenor


def ordena(vals, qual):
    for i in range(len(vals)):
        ondeMenor = localiza(vals, i, qual)
        vals[i], vals[ondeMenor] = vals[ondeMenor], vals[i]


def ordenaPelosCamposEMostra(valores):
    for campo in range(len(valores[0])):
        ordena(valores, campo)
        mostra(valores, "Ordenados Pelo Campo: "+str(campo+1))


# Programa Principal
nomeDoArquivo = input()
tabela = constroi(nomeDoArquivo)
if tabela == []:
    print("Arquivo:", nomeDoArquivo, "está vazio!!!")
else:
    mostra(tabela,"Lida do Arquivo: "+nomeDoArquivo)
    ordenaPelosCamposEMostra(tabela)
