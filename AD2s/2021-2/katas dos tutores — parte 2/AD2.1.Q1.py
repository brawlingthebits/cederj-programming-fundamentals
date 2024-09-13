# AD2.1 - Questão 1
# Subprogramas
def mostraArquivo(nm):
    print("Conteúdo do arquivo", nm+":")
    dados = open(nm, "r")
    for linha in dados:
        print(linha.strip("\n"))
    dados.close()
    print()
    return None


def mostraMatriz(elems, msg):
    print(msg)
    if elems == None:
        print("Nenhuma matriz foi encontrada no arquivo!!!")
    else:
        for lin in range(len(elems)):
            for col in range(len(elems[lin])):
                print("% 4d" % elems[lin][col], end="")
            print()
        print("Quantidade de elementos:", len(elems) * len(elems[0]))
    print()
    return None


def matrizComMaisElementos(nm):
    elems = None
    dados = open(nm, "r")
    linha = dados.readline()
    if linha == "":
        dados.close()
        return None
    else:
        elems = list()
        qtdLinhas = int(linha)
        for i in range(qtdLinhas):
            elems.append(list(map(int, dados.readline().split())))
        linha = dados.readline()
        while linha != "":
            qtdLinhasAtual = int(linha)
            primeiraLinhaAtual = list(map(int, dados.readline().strip().split()))
            qtdColunasAtual = len(primeiraLinhaAtual)
            if qtdLinhasAtual * qtdColunasAtual <= len(elems) * len(elems[0]):
                for lin in range(1, qtdLinhasAtual):
                    descartada = dados.readline()
            else:
                elems = [primeiraLinhaAtual]
                for i in range(qtdLinhasAtual):
                    elems.append(list(map(int, dados.readline().strip().split())))
            linha = dados.readline()
        dados.close()
        return elems


def transposta(elems):
    if elems == None:
        return None
    else:
        elemsTransp = list()
        for lin in range(len(elems[0])):
            elemsTransp.append(list())
        for col in range(len(elems[0])):
            for lin in range(len(elems)):
                elemsTransp[col].append(elems[lin][col])
        return elemsTransp


# Programa Principal
nome = input()
mostraArquivo(nome)
elementos = matrizComMaisElementos(nome)
mostraMatriz(elementos, "Matriz com mais elementos:")
mostraMatriz(transposta(elementos), "Transposta da Matriz com mais elementos:")