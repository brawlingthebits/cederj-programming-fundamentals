# AD2 - Questão 4 - Programa auxiliar para exibir a saída (não precisava ser entregue)

import struct

with open('saida.bin', 'rb') as saida:
    bloco = saida.read(4)
    while bloco != b'':
        valor = struct.unpack('=i', bloco)[0]
        print(valor)
        bloco = saida.read(4)
