import struct

cartoes = struct.Struct("20s 50s")
printInfo = False


def decodifica_dados_cartoes(bloco):
    campos = cartoes.unpack(bloco)

    bandeira = campos[0].decode("utf-8").strip(chr(0))
    valor = campos[1].decode("utf-8").strip(chr(0)).strip('\n')
    valor = float(valor)

    return bandeira, valor


def eh_float(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


def processar_arquivo_cartoes(nome_arquivo_cartoes, tipo, taxa, preco):
    if eh_float(taxa):
        if eh_float(preco):
            with open(nome_arquivo_cartoes, "rb") as arquivo:
                index = 0
                while True:
                    bloco = arquivo.read(cartoes.size)
                    if not bloco:
                        break
                    bandeira, valor = decodifica_dados_cartoes(bloco)
                    if tipo == bandeira:
                        total = float(preco)*float(taxa) + valor
                        total = float('%.2f' % total)
                        print(f"Como seu cartão é da bandeira {tipo}, então você pagará {total}")
                        index = 1
                if index == 0:
                    print("Cartão não consta")
        else:
            print("você colocou um valor não correspondente")
    else:
        print("você colocou uma taxa não correspondente")


def main():
    arq = input()
    tipo = input()
    taxa = input()
    preco = input()

    try:
        processar_arquivo_cartoes(arq, tipo, taxa, preco)
    except IOError:
        print('Um dos arquivos não foi encontrado ou digitou errado.')


main()
