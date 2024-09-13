import struct
Frete = struct.Struct("8s 5s f")

def main():
    try:
        with open("frete.txt", "r") as arquivoTxt:
            with open("frete.bin", "wb") as arquivoBin:
                for linha in arquivoTxt:
                    entrada = linha.split()
                    if (len(entrada) > 1):
                        cep = entrada[0]
                        nomeLoja = entrada[1]
                        valorFrete = float(entrada[2])

                        bloco = Frete.pack(cep.encode("utf-8"), nomeLoja.encode("utf-8"),valorFrete)
                        arquivoBin.write(bloco)
        print("Arquivo binário criado.")
    except IOError:
        print('Arquivo txt não encontrado.')

main()