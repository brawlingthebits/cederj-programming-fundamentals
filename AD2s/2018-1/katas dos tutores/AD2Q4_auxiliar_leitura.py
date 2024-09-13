# AD2 - Questão 4 - Programa auxiliar para leitura do arquivo "valores.bin". Este programa não faz parte da solução.
#
#                   Observação: É possível que o valor impresso na saída padrão não seja exatamente o mesmo
#                               informado na criação do arquivo devido a erro de arredondamento na representação por
#                               ponto flutuante (https://pt.wikipedia.org/wiki/Erro_de_arredondamento)

import struct

with open("valores.bin", "rb") as arqValores:
    n = struct.unpack("=i", arqValores.read(4))[0]
    print(n, end=" ")

    for i in range(n):
        v1 = struct.unpack("=i", arqValores.read(4))[0]
        v2 = struct.unpack("=f", arqValores.read(4))[0]
        print(v1, v2, end=" ")
print()
