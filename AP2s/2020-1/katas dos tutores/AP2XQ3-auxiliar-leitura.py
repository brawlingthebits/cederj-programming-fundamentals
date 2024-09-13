# AP2X - Questão 3 - Programa auxiliar para verificar se o arquivo escrito está correto (não precisava ser entregue)

import struct

with open('meuArquivo.bin', 'rb') as arq:
    n = struct.unpack('=i', arq.read(4))[0]
    for i in range(n):
        print('Registro %d - Campo 1: %f, Campo 2: "%s"' % (i + 1, struct.unpack('=f', arq.read(4))[0], arq.read(256).decode('utf-8').rstrip(chr(0))))
