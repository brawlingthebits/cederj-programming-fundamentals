# AD2 - Questão 6 - Programa auxiliar para gerar arquivos de entrada (não precisava ser escrito na avaliação)

import struct

lista = [2, 12, 18, 25, 26]

with open('valores.bin', 'wb') as valores:
    for valor in lista:
        valores.write(struct.pack('=i', valor))
