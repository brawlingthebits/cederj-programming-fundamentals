# AP3 - Questão 4

import struct

# Programa Principal
with open('entrada.bin', 'rb') as entrada:
    with open('saida1.txt', 'w') as saida1:
        with open('saida2.txt', 'w') as saida2:
            buffer = entrada.read(8)
            while buffer != b'':
                valor = struct.unpack('=d', buffer)[0]
                if valor == int(valor):
                    saida1.write('%1.0f\n' % valor)
                else:
                    saida2.write('%1.4f\n' % valor)
                buffer = entrada.read(8)
