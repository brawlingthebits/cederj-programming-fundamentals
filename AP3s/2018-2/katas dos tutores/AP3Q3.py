# AP3 - Questão 3

import struct
Produto = struct.Struct("4s d f")


# Subprogramas
def localiza(arqBin, inicio, tam):
    resposta = inicio
    arqBin.seek(inicio*Produto.size)
    bMenor = arqBin.read(Produto.size)
    codigoMenor = bMenor[0:4].decode("utf-8")
    for i in range(inicio+1, tam//Produto.size):
        bAtual = arqBin.read(Produto.size)
        codigoAtual = bAtual[0:4].decode("utf-8")
        if codigoAtual < codigoMenor:
            codigoMenor = codigoAtual
            resposta = i
    return resposta


def ordenaMercado(nm):
    with open(nm, "r+b") as arqMercado:
        arqMercado.seek(0,2)
        tamanho = arqMercado.tell()
        for i in range(tamanho//Produto.size - 1):
            ondeMenor = localiza(arqMercado, i, tamanho)
            if ondeMenor != i:
                arqMercado.seek(i*Produto.size)
                bloco = arqMercado.read(Produto.size)
                arqMercado.seek(ondeMenor*Produto.size)
                blocoMenor = arqMercado.read(Produto.size)
                arqMercado.seek(i*Produto.size)
                arqMercado.write(blocoMenor)
                arqMercado.seek(ondeMenor*Produto.size)
                arqMercado.write(bloco)
        arqMercado.close()
    return None


def mostraMercado(nm):
    print("----- Mercado -----")
    with open(nm, "rb") as arqMercado:
        arqMercado.seek(0,2)
        tamanho = arqMercado.tell()
        arqMercado.seek(0)
        for _ in range(tamanho//Produto.size):
            bloco = arqMercado.read(Produto.size)
            campos = Produto.unpack(bloco)
            codigo = bloco[0:4].decode("utf-8")
            print(codigo, campos[1], "%.2f"%campos[2])
        arqMercado.close()
    print()
    return None


# Programa Principal
nome = input()
mostraMercado(nome)
ordenaMercado(nome)
mostraMercado(nome)