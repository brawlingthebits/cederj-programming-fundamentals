import struct

natal = struct.Struct("20s 20s 100s")
printInfo = False


def decodifica_dados_natal(bloco):
    campos = natal.unpack(bloco)

    nome = campos[0].decode("utf-8").strip(chr(0))
    parentesco = campos[1].decode("utf-8").strip(chr(0)).strip('\n')
    presente_valor = campos[2].decode("utf-8").strip(chr(0)).strip('\n')

    return nome, parentesco, presente_valor


def processar_arquivo_natal(nome_arquivo_natal, consulta):
    with open(nome_arquivo_natal, "rb") as arquivo:
        marc = 0
        while True:
            bloco = arquivo.read(natal.size)
            if not bloco:
                break
            nome, parentesco, presente_valor = decodifica_dados_natal(bloco)
            presente_valor_separadas = presente_valor.split(';')
            if consulta == nome:
                marc = 1
                valor_total = []
                produtos = []
                for x in presente_valor_separadas:
                    valores = x.split('&')
                    valores[1] = valores[1].replace(',', '.')
                    valor_total.append(float(valores[1]))
                    produtos.append(valores[0])
                total = 0
                for i in range(0,len(valor_total)):
                    total += valor_total[i]
                print(f"Para comprar os presentes para {nome}, que é meu/minha {parentesco}, gastarei R$ {total}.")
                print(f"Os itens da lista para {nome} são:")
                for x in produtos:
                    print(x)
        if marc == 0:
            print(f"{consulta} não está na lista")


def main():
    arq = input()
    consulta = input()

    try:
        processar_arquivo_natal(arq, consulta)
    except IOError:
        print('Um dos arquivos não foi encontrado ou digitou errado.')


main()
