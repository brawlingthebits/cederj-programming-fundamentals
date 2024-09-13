# AP2 - Questão 3 - Essa é apenas uma das possibilidades de solução. Outra possibilidade consiste em concatenar ambos os arquivos de entrada e depois realizar a ordenação em disco utilizando um dos algoritmos vistos em aula.

import struct

with open('entrada1.bin', 'rb') as entrada1:
    with open('entrada2.bin', 'rb') as entrada2:
        with open('saida.bin', 'wb') as saida:
            # Ler um valor de cada arquivo de entrada
            bytes1 = entrada1.read(4)
            bytes2 = entrada2.read(4)
            # Enquanto houver valores em pelo menos um dos arquivos...
            while bytes1 != b'' or bytes2 != b'':
                # ... se primeiro arquivo chegou ao fim, escrever o valor lido do segundo arquivo
                if bytes1 == b'':
                    saida.write(bytes2)
                    bytes2 = entrada2.read(4)
                # ... se segundo arquivo chegou ao fim, escrever o valor lido do primeiro arquivo
                elif bytes2 == b'':
                    saida.write(bytes1)
                    bytes1 = entrada1.read(4)
                # ... se nenhum dos arquivos chegou ao fim, escrever o menor dos valores para garantir ordenação
                else:
                    valor1 = struct.unpack('=i', bytes1)[0]
                    valor2 = struct.unpack('=i', bytes2)[0]
                    if valor1 <= valor2:
                        saida.write(bytes1)
                        bytes1 = entrada1.read(4)  # Ler o próximo valor do primeiro arquivo
                    else:
                        saida.write(bytes2)
                        bytes2 = entrada2.read(4)  # Ler o próximo valor do segundo arquivo
