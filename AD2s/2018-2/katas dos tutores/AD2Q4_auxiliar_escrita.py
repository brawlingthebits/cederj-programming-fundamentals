# AD2 - Questão 4 - Programa auxiliar para escrita do arquivo binário
# Obs.: Caso entregue, esse programa não será incluído na correção

import struct

with open("referencia.bin", "wb") as ref:
    palavra = input("Digite uma palavra (deixe em branco para sair): ")
    while palavra != "":
        valor = float(input("Digite o valor: "))
        ref.write(palavra[:256].ljust(256, chr(0)).encode("utf-8"))
        ref.write(struct.pack("=d", valor))
        palavra = input("\nDigite uma palavra (deixe em branco para sair): ")