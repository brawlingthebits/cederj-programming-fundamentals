# AD2 - Questão 4

import struct

v1Entrada = int(input("Informe ao valor inteiro de entrada: "))
v2Entrada = float(input("Informe ao valor em ponto flutuante de entrada: "))

with open("valores.bin", "r+b") as arqValores:
    n = struct.unpack("=i", arqValores.read(4))[0]
    for i in range(n):
        v1 = struct.unpack("=i", arqValores.read(4))[0]
        v2 = struct.unpack("=f", arqValores.read(4))[0]

        arqValores.seek(-8, 1)

        if v1 < v1Entrada:
            arqValores.write(struct.pack("=i", -1))
        else:
            arqValores.write(struct.pack("=i", v1))

        if v2 > v2Entrada:
            arqValores.write(struct.pack("=f", 9999.0))
        else:
            arqValores.write(struct.pack("=f", v2))
