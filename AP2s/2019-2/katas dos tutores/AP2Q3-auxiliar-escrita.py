# AP2 - Questão 3 - Programa auxiliar para escrever arquivos binários compostos por valores inteiros ordenados

import struct, random

nome_arquivo = input('Informe o nome do arquivo binário a ser gerado: ')
with open(nome_arquivo, 'wb') as arq:
    n = int(input('Informe a quantidade de números no arquivo: '))
    for valor in sorted([random.randint(-100, 100) for _ in range(n)]):
        arq.write(struct.pack('=i', valor))
