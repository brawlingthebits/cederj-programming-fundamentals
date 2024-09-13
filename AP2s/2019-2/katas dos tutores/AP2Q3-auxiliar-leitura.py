# AP2 - Questão 3 - Programa auxiliar para ler arquivos binários compostos por valores inteiros

import struct

nome_arquivo = input('Informe o nome do arquivo binário a ser lido: ')
with open(nome_arquivo, 'rb') as arq:
    buffer = arq.read(4)
    while buffer != b'':
        print(struct.unpack('=i', buffer)[0], end=' ')
        buffer = arq.read(4)
    print()
