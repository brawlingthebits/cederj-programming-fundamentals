# AP2 - Questão 1

# Subprogramas


def mostrar(nm):
    dados = open(nm, "r")
    print("------- " + nm + " -------")
    for linha in dados:
        print(linha, end="")
    dados.close()
    return None


def modifica(nm, c, q):
    valor = 0
    dados = open(nm, "r")
    auxiliar = open(nm + "aux", "w")
    for produto in dados:
        codigo, descricao, quantidade, preco = produto.split("#")
        if codigo == c:
            valor = q * float(preco)
            novaQuantidade = int(quantidade) - q
            produto = codigo + "#" + descricao + "#" + str(novaQuantidade) + "#" + preco
        auxiliar.write(produto)
    dados.close()
    auxiliar.close()
    auxiliar = open(nm + "aux", "r")
    dados = open(nm, "w")
    for produto in auxiliar:
        dados.write(produto)
    auxiliar.close()
    dados.close()
    return valor


def atualiza(nmMer, nmComp):
    totalGasto = 0
    dadosCompras = open(nmComp)
    for item in dadosCompras:
        cod, qtd = item.split("#")
        totalGasto += modifica(nmMer, cod, int(qtd))
    dadosCompras.close()
    print("Total Gastos nas Compras:", totalGasto)
    return None


# Programa Principal
nomeMercado = input("Diga o nome do arquivo do mercado: ")
nomeCompras = input("Diga o nome do arquivo de compras: ")
mostrar(nomeMercado)
mostrar(nomeCompras)
atualiza(nomeMercado, nomeCompras)
mostrar(nomeMercado)