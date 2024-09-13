# AP3 - Questão 3

# Subprograma
def mdc(a, b):
    if b > 0:
        return mdc(b, a % b)
    else:
        return a


# Programa Principal
import struct

with open("valores.bin", "rb") as arq:
    n = struct.unpack("=i", arq.read(4))[0]
    for i in range(n):
        val1 = struct.unpack("=i", arq.read(4))[0]
        val2 = struct.unpack("=i", arq.read(4))[0]
        print(mdc(val1, val2))
