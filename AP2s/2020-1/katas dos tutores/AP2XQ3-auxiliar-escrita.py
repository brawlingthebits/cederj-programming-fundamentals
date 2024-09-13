# AP2X - Questão 3 - Programa auxiliar para escrever um aquivo de entrada (não precisava ser entregue)

import struct

with open('meuArquivo.bin', 'wb') as arq:
    n = int(input('Informe a quantidade de registros: '))
    arq.write(struct.pack('=i', n))
    for i in range(n):
        print('\nRegistro %d' % (i + 1))
        arq.write(struct.pack('=f', float(input('Campo 1: '))))
        arq.write(input('Campor 2: ')[:256].ljust(256, chr(0)).encode('utf-8'))
