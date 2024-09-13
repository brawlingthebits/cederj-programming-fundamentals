import struct
Dicionario = struct.Struct("30s 100s")

def main():
    try:
        with open("Dicionario.txt", "r") as arquivoTxt:
            with open("Dicionario.bin", "wb") as arquivoBin:
                for linha in arquivoTxt:
                    entrada = linha.split('#')
                    if (len(entrada) > 1):
                        nome = entrada[0]
                        definicao = entrada[1]

                        bloco = Dicionario.pack(nome.encode("utf-8"), definicao.encode("utf-8"))
                        arquivoBin.write(bloco)
        print("Arquivo binário criado.")
    except IOError:
        print('Arquivo txt não encontrado.')

main()