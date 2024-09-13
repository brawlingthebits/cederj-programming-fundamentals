# Programa AP2Q1
# Subprogramas
def carrega(nm):
    listaDeListas = list()
    arquivo = open(nm, "r")
    for linhaDoArquivo in arquivo:
        listaDeListas.append(list(map(int, linhaDoArquivo.split())))
    arquivo.close()
    return listaDeListas


def passaNaRestricao(lin, col, listaDeListas):
    for linha in [lin - 1, lin, lin + 1]:
        for coluna in [col - 1, col, col + 1]:
            if 0 <= linha < len(listaDeListas) and 0 <= coluna < len(listaDeListas[0]) and \
                    (linha, coluna) != (lin, col) and listaDeListas[lin][col] >= listaDeListas[linha][coluna]:
                return False
    return True


def adjacentesMaioresQueCelula(listaDeListas):
    for linha in range(len(listaDeListas)):
        for coluna in range(len(listaDeListas[linha])):
            if passaNaRestricao(linha, coluna, listaDeListas):
                print("Linha %d, Coluna %d, Valor = %d" % (linha + 1, coluna + 1, listaDeListas[linha][coluna]))
    return None


# Principal
nomeArquivo = input()
valores = carrega(nomeArquivo)
adjacentesMaioresQueCelula(valores)
