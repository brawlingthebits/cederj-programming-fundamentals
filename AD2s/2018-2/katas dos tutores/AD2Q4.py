# AD2 - Questão 4

import struct

# Subprograma que remove caracteres especiais da palavra.
def limpar(arg):
    ret = ""
    for c in arg:
        if c in "abcdefghijklmnopqrstuvwxyz0123456789":
            ret += c
    return ret


# Ler valores cobrados por palavra.
referencia = dict()
with open("referencia.bin", "rb") as ref:
    palavra = ref.read(256)
    while palavra != b"":
        palavra = palavra.decode("utf-8").rstrip(chr(0)).lower()
        valor = struct.unpack("d", ref.read(8))[0]
        referencia[palavra] = [valor, 0]
        palavra = ref.read(256)

# Ler mensagem e calcular imposto.
nome = input("Informe o nome do arquivo texto que contém a mensagem: ")

imposto = 0
with open(nome, "r") as txt:
    for linha in txt.readlines():
        for palavra in linha.lower().split():
            palavra = limpar(palavra)
            par = referencia.get(palavra)
            if par is not None and par[1] < 2:
                imposto += par[0]
                par[1] += 1

# Exibir o valor do imposto.
print("O imposto cobrado é de R$%1.2f" % imposto)