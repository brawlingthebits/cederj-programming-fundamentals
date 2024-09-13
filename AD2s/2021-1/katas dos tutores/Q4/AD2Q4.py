import struct
Frete = struct.Struct("8s 5s f")

def decodificaDadosFrete(bloco):
    campos = Frete.unpack(bloco)
    cep = campos[0].decode("utf-8")
    nomeLoja = campos[1].decode("utf-8").rstrip(chr(0))
    valorFrete = round(campos[2], 2)

    return cep, nomeLoja, valorFrete

def processarArquivoFreteBin(nomeArquivoFrete,cepDestinatario):
    frete = dict()

    with open(nomeArquivoFrete, "rb") as arquivo:
        while (True):
            bloco = arquivo.read(Frete.size)
            if (not bloco):
                break
            cep, nomeLoja, valorFrete = decodificaDadosFrete(bloco)

            if(cep == cepDestinatario):
                frete[nomeLoja] = valorFrete
    return frete

def getMelhorCusto(nomeArquivoProduto, frete):
    melhorCusto = {"nomeProduto": None, "nomeLoja": None, "custoTotal": None}

    if(not frete):
        return None

    with open(nomeArquivoProduto, "r") as arquivo:
        melhorCusto["nomeProduto"] = arquivo.readline().strip("\n")
        for linha in arquivo:
            dados = linha.split()
            if(len(dados)>1):
                nomeLoja = dados[0]
                valorProduto = float(dados[1])

                custoTotal = valorProduto+frete[nomeLoja]
                if(melhorCusto["nomeLoja"] == None or  custoTotal< melhorCusto["custoTotal"]):
                    melhorCusto["nomeLoja"] = nomeLoja
                    melhorCusto["custoTotal"] = custoTotal
    return melhorCusto

def main():
    nomeArquivoFrete = input()
    nomeArquivoProduto = input()
    cepDestinatario = input().replace('.', '').replace('-', '')

    try:
        frete = processarArquivoFreteBin(nomeArquivoFrete,cepDestinatario)
        melhorCusto = getMelhorCusto(nomeArquivoProduto, frete)

        msg = ""
        if(not frete):
            msg = "O produto desejado não pode ser entregue neste frete."
        else:
            msg = "A melhor loja do " + melhorCusto["nomeProduto"] + " para o CEP " + cepDestinatario + " é a "
            msg += melhorCusto["nomeLoja"] + " com valor total de R$ " + "{:.2f}".format(melhorCusto["custoTotal"]) + "."
        print(msg)
    except IOError:
        print('Um dos arquivos não foi encontrado.')

main()