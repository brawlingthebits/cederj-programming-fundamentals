# AP2 - Questão 3 - Programa auxiliar para gerar arquivos de entrada (não precisava ser escrito na avaliação)

import struct

with open('medias.dat', 'rb') as arq:
    arq.seek(0, 2)
    num_registros = arq.tell() // (9 + 10 + 4)
    arq.seek(0)
    for _ in range(num_registros):
        matricula = arq.read(9).decode('utf-8')
        codigo = arq.read(10).decode('utf-8')
        media = struct.unpack('=f', arq.read(4))[0]
        print('Matrícula:', matricula, '; Código:', codigo, '; Média:', media)
