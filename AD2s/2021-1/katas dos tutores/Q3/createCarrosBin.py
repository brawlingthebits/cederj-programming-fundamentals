import struct
Carro = struct.Struct("4s 16s f f f f f")

def main():
    try:
        with open("carros.txt", "r") as  arquivoTxt:
            with open("carros.bin", "wb") as  arquivoBin:
                for linha in arquivoTxt:
                    entrada = linha.split()
                    if (len(entrada) > 1):
                        anoCarro = entrada[0]
                        modeloCarro = entrada[1]
                        cidadeAlcool = float(entrada[2])
                        cidadeGasolina = float(entrada[3])
                        estradaAlcool = float(entrada[4])
                        estradaGasolina = float(entrada[5])
                        capacidadeTanque = float(entrada[6])

                        bloco = Carro.pack(anoCarro.encode("utf-8"), modeloCarro.encode("utf-8"), cidadeAlcool, cidadeGasolina,
                                           estradaAlcool, estradaGasolina, capacidadeTanque)
                        arquivoBin.write(bloco)
        print("Arquivo binário criado.")
    except IOError:
        print('Arquivo txt não encontrado.')

main()