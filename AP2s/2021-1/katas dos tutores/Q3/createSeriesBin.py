import struct
Series = struct.Struct("4s 30s 60s")

def main():
    try:
        with open("Series.txt", "r") as arquivoTxt:
            with open("Series.bin", "wb") as arquivoBin:
                for linha in arquivoTxt:
                    entrada = linha.split('#')
                    if (len(entrada) > 1):
                        anoSerie = entrada[0]
                        nomeSerie = entrada[1]
                        nomePlataforma = entrada[2]

                        bloco = Series.pack(anoSerie.encode("utf-8"), nomeSerie.encode("utf-8"), nomePlataforma.encode("utf-8"))
                        arquivoBin.write(bloco)
        print("Arquivo binário criado.")
    except IOError:
        print('Arquivo txt não encontrado.')

main()