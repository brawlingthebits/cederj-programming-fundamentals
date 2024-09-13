# AP2X - Questão 3

import struct

with open('meuArquivo.bin', 'r+b') as arq:
    n = struct.unpack('=i', arq.read(4))[0]
    # Leitura
    regs = []
    for i in range(n):
        campo1 = struct.unpack('=f', arq.read(4))[0]
        campo2 = arq.read(256).decode('utf-8').rstrip(chr(0))
        regs.append((campo1, campo2))
    # Ordenação
    for i in range(len(regs) - 1):
        i_menor = i
        for j in range(i + 1, len(regs)):
            if (regs[j][1] < regs[i_menor][1]) or (regs[j][1] == regs[i_menor][1] and regs[j][0] < regs[i_menor][0]):
                i_menor = j
        regs[i], regs[i_menor] = regs[i_menor], regs[i]
    # Escrita
    arq.seek(4)
    for i in range(n):
        arq.write(struct.pack('=f', regs[i][0]))
        arq.write(regs[i][1].ljust(256, chr(0)).encode('utf-8'))
