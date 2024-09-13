import struct
cliente = struct.Struct("20s 50s 50s 100s")


def main():
    try:
        with open("cliente.txt", "r") as arquivoTxt:
            with open("cliente.bin", "wb") as arquivoBin:
                for linha in arquivoTxt:
                    entrada = linha.split('#')
                    if len(entrada) > 1:
                        pais = entrada[0]
                        cidade = entrada[1]
                        aeroporto = entrada[2]
                        cias = entrada[3]

                        bloco = cliente.pack(pais.encode("utf-8"), cidade.encode("utf-8"), aeroporto.encode("utf-8"), cias.encode("utf-8"))
                        arquivoBin.write(bloco)
        print("Arquivo binário criado.")
    except IOError:
        print('Arquivo txt não encontrado.')


main()
