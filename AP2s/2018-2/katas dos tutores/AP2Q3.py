# AP2 - Questão 3

import struct
Produto = struct.Struct("4s d f")


# Subprogramas
def carrega(nm):
    prods = []
    with open(nm, "rb") as arqMercado:
        arqMercado.seek(0,2)
        tamanho = arqMercado.tell()
        arqMercado.seek(0)
        arqMercado.seek(0,2)
        tamanho = arqMercado.tell()
        arqMercado.seek(0)
        for i in range(tamanho//Produto.size):
            bloco = arqMercado.read(Produto.size)
            campos = Produto.unpack(bloco)
            codigo = bloco[0:4].decode("utf-8")
            prods.append([codigo, campos[1], campos[2]])
        arqMercado.close()
    return prods


def consulta(merc, codProc):
    for cod, qtd, preco in merc:
        if cod == codProc:
            print("O preço do produto", codProc,"é", preco)
            return None
    print(codProc, "não foi encontrado!!!")
    return None


# Programa Principal
nome = input()
mercado = carrega(nome)
codProcurado = input()
consulta(mercado, codProcurado)