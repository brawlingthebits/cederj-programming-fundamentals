# AD2 - Questão 4 - Programa auxiliar para escrita do arquivo "valores.bin". Este programa não faz parte da solução.

import struct

with open("valores.bin", "wb") as arqValores:
    n = int(input("Indique quantos registros existirão em seu arquivo: "))
    arqValores.write(struct.pack("=i", n))

    for i in range(n):
        v1 = int(input("Informe o valor inteiro #%d: " % (i + 1)))
        arqValores.write(struct.pack("=i", v1))
        v2 = float(input("Informe o valor em ponto flutuante #%d: " % (i + 1)))
        arqValores.write(struct.pack("=f", v2))
