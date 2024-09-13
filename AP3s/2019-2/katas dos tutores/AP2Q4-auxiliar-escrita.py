# AP3 - Questão 4 - Programa auxiliar para escrever arquivos binários compostos por valores em ponto flutuante

import struct

with open('entrada.bin', 'wb') as arq:
    n = int(input('Informe a quantidade de números no arquivo: '))
    for i in range(1, n + 1):
        valor = float(input('Informe o valor %d: ' % i))
        arq.write(struct.pack('=d', valor))
