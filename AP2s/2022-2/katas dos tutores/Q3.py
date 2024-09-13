# Programa - Prova 2 (AP2) - Questão 3
# Observação: o uso de encoding="utf-8" não será cobrado.

# Subprogramas
def mostrar(nmArq, texto):
    print(texto)
    arquivo = open(nmArq, "r", encoding="utf-8")
    for linha in arquivo:
        print(linha, end="")
    print()
    arquivo.close()
    return None


def atualiza(nmArq, c, q):
    total = 0
    arqAuxiliar = open(nmArq + "aux", "w", encoding="utf-8")
    arquivo = open(nmArq, "r", encoding="utf-8")
    for produto in arquivo:
        cod, desc, qtdDisp, precoUnitario = produto.split("#")
        if cod == c:
            total = int(q) * float(precoUnitario)
            qtdDisp = str(int(qtdDisp) - int(q))
        arqAuxiliar.write(cod + "#" + desc + "#" + qtdDisp + "#" + precoUnitario)
    arqAuxiliar.close()
    arquivo.close()
    arqAuxiliar = open(nmArq + "aux", "r", encoding="utf-8")
    arquivo = open(nmArq, "w", encoding="utf-8")
    for produto in arqAuxiliar:
        arquivo.write(produto)
    arqAuxiliar.close()
    arquivo.close()
    return total


def venderProdutos(nmArqVendas, nmArqMerc):
    totalGasto = 0
    arquivoVendas = open(nmArqVendas, "r")
    for produtoVendido in arquivoVendas:
        cod, qtd = produtoVendido.split("#")
        totalParcial = atualiza(nmArqMerc, cod, qtd)
        totalGasto = totalGasto + totalParcial
    arquivoVendas.close()
    print("Total Gasto: R$ %.2f" % totalGasto)
    return None


# Principal
nomeArqMercado = input()
nomeArqVendas = input()
mostrar(nomeArqMercado, "Antes das Vendas:")
mostrar(nomeArqVendas, "Relação de Vendas:")
venderProdutos(nomeArqVendas, nomeArqMercado)
mostrar(nomeArqMercado, "Depois das Vendas:")
