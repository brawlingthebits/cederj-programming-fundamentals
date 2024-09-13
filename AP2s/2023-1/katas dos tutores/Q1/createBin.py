import struct
cartoes = struct.Struct("20s 20s f")


def main():
    try:
        with open("conversoes.txt", "r") as arquivoTxt:
            with open("conversoes.bin", "wb") as arquivoBin:
                for linha in arquivoTxt:
                    entrada = linha.split('#')
                    if len(entrada) > 1:
                        moeda1 = entrada[0]
                        moeda2 = entrada[1]
                        valor = float(entrada[2])

                        bloco = cartoes.pack(moeda1.encode("utf-8"), moeda2.encode("utf-8"), valor)
                        arquivoBin.write(bloco)
        print("Arquivo binário criado.")
    except IOError:
        print('Arquivo txt não encontrado.')


main()
