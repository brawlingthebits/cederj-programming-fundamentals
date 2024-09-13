# Programa AD12.Q2


# Subprograma(s)
def pegaProdutos():
    print("Início das Inserções de Produtos!!!")        # mensagem não cobrada
    print("Formato: código#descrição#quantidade#preço") # mensagem não cobrada
    listaProdutos = []
    linhaLidaDoTeclado = input()
    while linhaLidaDoTeclado != "":
        cod, desc, qtd, preco = linhaLidaDoTeclado.split("#")
        qtd = int(qtd)
        preco = float(preco)
        listaProdutos.append((cod, desc, qtd, preco))
        linhaLidaDoTeclado = input()
    print("Fim das Inserções de Produtos!!!")           # mensagem não cobrada
    return listaProdutos


def localiza(cod, prods):
    for pos in range(len(prods)):
        if cod == prods[pos][0]:
            return pos
    return None


# Principal
# Inicialização
produtos = pegaProdutos()
# Processamento
print("Início das Buscas pelo Código!!!")               # mensagem não cobrada
codigoProcurado = input()
while codigoProcurado != "":
    onde = localiza(codigoProcurado, produtos)
    if onde == None:
        print("Código %s não localizado na lista de produtos!!!" % codigoProcurado)
    else:
        print("Produto Localizado:", produtos[onde])
    codigoProcurado = input()
# Finalização
print("Obrigado por utilizar nosso sistema!!!")
