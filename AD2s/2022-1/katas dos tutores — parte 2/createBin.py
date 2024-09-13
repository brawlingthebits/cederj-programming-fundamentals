import struct
cartoes = struct.Struct("20s 50s")


def main():
    try:
        with open("cartoes.txt", "r") as arquivoTxt:
            with open("cartoes.bin", "wb") as arquivoBin:
                for linha in arquivoTxt:
                    entrada = linha.split('#')
                    if len(entrada) > 1:
                        bandeira = entrada[0]
                        valor = entrada[1]

                        bloco = cartoes.pack(bandeira.encode("utf-8"), valor.encode("utf-8"))
                        arquivoBin.write(bloco)
        print("Arquivo binário criado.")
    except IOError:
        print('Arquivo txt não encontrado.')


main()
