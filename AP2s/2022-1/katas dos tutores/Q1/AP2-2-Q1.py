import struct

conversoes = struct.Struct("20s 20s f")
printInfo = False


def decodifica_dados_conversao(bloco):
    campos = conversoes.unpack(bloco)

    moeda1 = campos[0].decode("utf-8").strip(chr(0))
    moeda2 = campos[1].decode("utf-8").strip(chr(0)).strip('\n')
    taxa = campos[2]

    return moeda1, moeda2, taxa


def eh_float(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


def processar_arquivo_conversoes(nome_arquivo_conversao, tipo1, tipo2, valor):
    dic = {"real": "BRL", "dolar": "USD", "euro": "EUR"}
    if eh_float(valor):
         with open(nome_arquivo_conversao, "rb") as arquivo:
            index = 0
            while True:
                bloco = arquivo.read(conversoes.size)
                if not bloco:
                    break
                moeda1, moeda2, taxa = decodifica_dados_conversao(bloco)
                if tipo1 == moeda1:
                    if tipo2 == moeda2:
                        total = float(taxa)*float(valor)
                        total = float('%.2f' % total)
                        print(f"Você pagará {total} {dic[moeda2]} por {valor} {dic[moeda1]}")
                        index = 1
                elif tipo1 == moeda2:
                    if tipo2 == moeda1:
                        total = float(valor)/float(taxa)
                        total = float('%.2f' % total)
                        print(f"Você pagará {total} {dic[moeda1]} por {valor} {dic[moeda2]}")
                        index = 1
            if index == 0:
                print("Alguma moeda não consta")
    else:
        print("você não colocou um valor correto")


def main():
    arq = input()
    tipo1 = input()
    tipo2 = input()
    valor = input()

    try:
        processar_arquivo_conversoes(arq, tipo1, tipo2, valor)
    except IOError:
        print('Um dos arquivos não foi encontrado ou digitou errado.')


main()
