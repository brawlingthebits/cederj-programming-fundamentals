# AP3X - Questão 3

import struct


# Subprogramas
def ler_produtos(nome_arquivo):
    registros = dict()
    with open(nome_arquivo, 'rb') as arq:
        arq.seek(0, 2)
        num_registros = arq.tell() // (13 + 50 + 4)
        arq.seek(0)
        for _ in range(num_registros):
            codigo_de_barras = arq.read(13).decode('utf-8')
            nome = arq.read(50).decode('utf-8').rstrip(chr(0))
            preco = struct.unpack('=f', arq.read(4))[0]
            registros[codigo_de_barras] = (codigo_de_barras, nome, preco)
    return registros


def ler_compras(nome_arquivo):
    registros = dict()
    with open(nome_arquivo, 'rb') as arq:
        arq.seek(0, 2)
        num_registros = arq.tell() // (10 + 256)
        arq.seek(0)
        for _ in range(num_registros):
            codigo_da_compra = arq.read(10).decode('utf-8')
            comprador = arq.read(256).decode('utf-8').rstrip(chr(0))
            registros[codigo_da_compra] = (codigo_da_compra, comprador)
    return registros


def substituir_compra(nome_arquivo, codigo_da_compra_procurada, codigo_de_barras_produrado, nova_quantidade):
    with open(nome_arquivo, 'a+b') as arq:
        arq.seek(0, 2)
        num_registros = arq.tell() // (10 + 13 + 4)
        arq.seek(0)
        for _ in range(num_registros):
            codigo_da_compra = arq.read(10).decode('utf-8')
            codigo_de_barras = arq.read(13).decode('utf-8')
            _ = struct.unpack('=i', arq.read(4))[0]
            if codigo_da_compra == codigo_da_compra_procurada and codigo_de_barras == codigo_de_barras_produrado:
                arq.seek(-(10 + 13 + 4), 1)
                break
        arq.write(codigo_da_compra_procurada.encode('utf-8'))
        arq.write(codigo_de_barras_produrado.encode('utf-8'))
        arq.write(struct.pack('=i', nova_quantidade))
