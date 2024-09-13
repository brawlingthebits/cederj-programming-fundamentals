# AP2 - Questão 3 - Programa auxiliar para gerar arquivos de entrada (não precisava ser escrito na avaliação)

import struct

dados = [10.0, 15.5, 16.9, 30.5, 44.0, 60.0]

with open("entrada_questao3.bin", "wb") as entrada:
    for valor in dados:
        bloco = struct.pack("=d", valor)
        entrada.write(bloco)
