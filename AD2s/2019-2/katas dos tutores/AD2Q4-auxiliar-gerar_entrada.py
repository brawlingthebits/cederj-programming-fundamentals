# AD2 - Questão 4 - Programa auxiliar para gerar arquivos de entrada (não precisava ser entregue)

import struct

dados = [10, 5, 1, 15, 5, 998, 27, 1, 88, 15, 88, 99, 5, 100, 7, 27, 998]

with open('entrada.bin', 'wb') as entrada:
    for valor in dados:
        bloco = struct.pack('=i', valor)
        entrada.write(bloco)
