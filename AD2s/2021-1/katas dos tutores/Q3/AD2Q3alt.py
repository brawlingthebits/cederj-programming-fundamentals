import struct
Carro = struct.Struct("4s 16s f f f f f")
printInfo = False

def processaArquivoPrecos(nomeArquivo):
    dados = open(nomeArquivo, "r")

    precoAlcool, precoGasolina = map(float, dados.readline().split())

    dados.close()
    return precoAlcool, precoGasolina

def decodificaDadosCarro(bloco):
    campos = Carro.unpack(bloco)

    anoCarro = campos[0].decode("utf-8")
    modeloCarro = campos[1].decode("utf-8").strip(chr(0))
    cidadeAlcool = campos[2]
    cidadeGasolina = campos[3]
    estradaAlcool = campos[4]
    estradaGasolina = campos[5]
    capacidadeTanque =campos[6]

    return anoCarro, modeloCarro,cidadeAlcool, cidadeGasolina, estradaAlcool, estradaGasolina, capacidadeTanque


def processarArquivoCarros(nomeArquivo,ano, estradaKm, cidadeKm):
    melhorCarroGasolina =  {"modelo": None,  "combustivelConsumido": None, "capacidadeTanque": None }
    melhorCarroAlcool = {"modelo": None, "combustivelConsumido": None, "capacidadeTanque": None}

    with open(nomeArquivo, "rb") as arquivo:
        while(True):
            bloco = arquivo.read(Carro.size)
            if(not bloco):
                break
            anoCarro, modeloCarro,cidadeAlcool, cidadeGasolina, estradaAlcool, estradaGasolina, capacidadeTanque = decodificaDadosCarro(bloco)

            if(anoCarro == ano):
                gasolinaConsumida = (estradaKm/estradaGasolina + cidadeKm/cidadeGasolina)
                if (melhorCarroGasolina["modelo"] == None or gasolinaConsumida < melhorCarroGasolina["combustivelConsumido"]):
                    if(printInfo == True):
                        print(anoCarro, modeloCarro,"- gasolina  -",cidadeKm,"/", cidadeGasolina,"+", estradaKm, "/", estradaGasolina, "=", cidadeKm/cidadeGasolina,
                              " + ",estradaKm/estradaGasolina,"=", gasolinaConsumida )
                    melhorCarroGasolina["modelo"] = modeloCarro
                    melhorCarroGasolina["combustivelConsumido"] = gasolinaConsumida
                    melhorCarroGasolina["capacidadeTanque"] = capacidadeTanque

                alcoolConsumido = (estradaKm / estradaAlcool + cidadeKm / cidadeAlcool)
                if (melhorCarroAlcool["modelo"] == None or alcoolConsumido < melhorCarroAlcool["combustivelConsumido"]):
                    if (printInfo == True):
                        print(anoCarro, modeloCarro,"- alcool", cidadeKm, "/", cidadeAlcool, "+", estradaKm, "/", estradaAlcool, "=", cidadeKm/cidadeAlcool,
                          " + ",estradaKm/estradaAlcool," = ", alcoolConsumido )
                    melhorCarroAlcool["modelo"] = modeloCarro
                    melhorCarroAlcool["combustivelConsumido"] = alcoolConsumido
                    melhorCarroAlcool["capacidadeTanque"] = capacidadeTanque

    return melhorCarroGasolina, melhorCarroAlcool

def main():
    nomeArquivoCarros = input()
    nomeArquivoPrecos = input()
    ano = input()
    cidadeKm = int(input())
    estradaKm = int(input())

    try:
        precoAlcool, precoGasolina = processaArquivoPrecos(nomeArquivoPrecos)
        melhorCarroGasolina, melhorCarroAlcool = processarArquivoCarros(nomeArquivoCarros,ano, estradaKm, cidadeKm)

        msg = ""
        msg+= 'No ano de {:s}, os carros mais econômicos para andar {:d} km à gasolina e a álcool são {:s} e {:s}, ' \
              'respetivamente.\n'.format(ano,(estradaKm+cidadeKm),melhorCarroGasolina["modelo"],melhorCarroAlcool["modelo"])
        msg+= "À gasolina, para andar {:d} km utilizaremos {:.2f} tanques e " \
              "gastaremos R$ {:.2f}.\n".format((estradaKm+cidadeKm),melhorCarroGasolina["combustivelConsumido"]/melhorCarroGasolina["capacidadeTanque"],melhorCarroGasolina["combustivelConsumido"]*precoGasolina)
        msg+= "À álcool, para andar {:d} km utilizaremos {:.2f} tanques e " \
              "gastaremos R$ {:.2f}.\n".format((estradaKm+cidadeKm),melhorCarroAlcool["combustivelConsumido"]/melhorCarroAlcool["capacidadeTanque"],melhorCarroAlcool["combustivelConsumido"]*precoAlcool)

        with open("carro_mais_economico.txt", "w") as arquivo:
            arquivo.write(msg)
    except IOError:
        print('Um dos arquivos não foi encontrado.')

main()