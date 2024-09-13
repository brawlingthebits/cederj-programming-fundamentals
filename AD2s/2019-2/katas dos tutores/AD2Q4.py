# AD2 - Questão 4


import struct

# Programa principal
with open('entrada.bin', 'rb') as entrada:
    with open('saida.bin', 'wb') as saida:
        q = struct.unpack('=i', entrada.read(4))[0]
        e = struct.unpack('=i', entrada.read(4))[0]

        s = set()
        for i in range(e):
            si = struct.unpack('=i', entrada.read(4))[0]
            s.add(si)

        for i in range(q):
            ci = struct.unpack('=i', entrada.read(4))[0]
            if ci in s:
                bloco = struct.pack('=i', 0)
            else:
                bloco = struct.pack('=i', 1)
            saida.write(bloco)
