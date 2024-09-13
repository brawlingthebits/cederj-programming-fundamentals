# AP2 - Questão 2

import struct
Produto = struct.Struct("4s d f")


# Subprogramas
def produzMercado(nm):
    with open(nm, "w+b") as arqMercado:
        entrada = input()
        while entrada != "":
            infos = entrada.split()
            codigo = infos[0].encode("utf-8")
            qtd, preco = int(infos[1]), float(infos[2])
            prod = Produto.pack(codigo,qtd,preco)
            arqMercado.write(prod)
            entrada = input()
        arqMercado.close()
    return None


def mostraMercado(nm):
    with open(nm, "rb") as arqMercado:
        arqMercado.seek(0,2)
        tamanho = arqMercado.tell()
        arqMercado.seek(0)
        for i in range(tamanho//Produto.size):
            bloco = arqMercado.read(Produto.size)
            campos = Produto.unpack(bloco)
            codigo = bloco[0:4].decode("utf-8")
            print(codigo, campos[1], campos[2])
        arqMercado.close()
    return None


# Programa Principal
nome = input()
produzMercado(nome)
mostraMercado(nome)