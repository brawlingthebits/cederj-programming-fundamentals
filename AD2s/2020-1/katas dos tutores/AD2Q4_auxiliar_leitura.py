# AD2 - Questão 4 - Programa auxiliar para leitura do arquivo binário
# Obs.: Caso entregue, esse programa não será incluído na correção

import struct

with open("imposto.bin", "rb") as res:
    print(struct.unpack("d", res.read(8))[0])