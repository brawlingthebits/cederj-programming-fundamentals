import struct

cliente = struct.Struct("20s 50s 50s 100s")
printInfo = False


def decodifica_dados_cliente(bloco):
    campos = cliente.unpack(bloco)

    pais = campos[0].decode("utf-8").strip(chr(0))
    cidade = campos[1].decode("utf-8").strip(chr(0)).strip('\n')
    aeroporto = campos[2].decode("utf-8").strip(chr(0)).strip('\n')
    cias = campos[3].decode("utf-8").strip(chr(0)).strip('\n')

    return pais, cidade, aeroporto, cias


def processar_arquivo_cliente(nome_arquivo_cliente, tipo, consulta):
    with open(nome_arquivo_cliente, "rb") as arquivo:
        dic_cidade = dict()
        dic_aeroporto = dict()
        dic_cias = dict()
        dic_pais = dict()
        while True:
            bloco = arquivo.read(cliente.size)
            if not bloco:
                break
            pais, cidade, aeroporto, cias = decodifica_dados_cliente(bloco)
            cias_separadas = cias.split('&')
            if tipo == 'país':
                if consulta in pais:
                    if consulta not in dic_cidade.keys():
                        dic_cidade[consulta] = [cidade]
                        dic_aeroporto[consulta] = [aeroporto]
                    else:
                        dic_cidade[consulta].append(cidade)
                        dic_aeroporto[consulta].append(aeroporto)
            if tipo == 'aeroporto':
                if consulta in aeroporto:
                    print(f"As cias aéreas que operam para {consulta}, {cidade} - {pais}, são:")
                    for x in range(0, len(cias_separadas)):
                        print(f"{cias_separadas[x]}")
            if tipo == 'cia':
                if consulta in cias:
                    if consulta not in dic_cias.keys():
                        dic_cias[consulta] = [aeroporto]
                        dic_cidade[consulta] = [cidade]
                        dic_pais[consulta] = [pais]
                    else:
                        dic_cias[consulta].append(aeroporto)
                        dic_cidade[consulta].append(cidade)
                        dic_pais[consulta].append(pais)
        if tipo == 'país':
            if len(dic_aeroporto) > 0:
                print(f"Os aeroportos de {consulta} são:")
                for x in range(0, len(dic_aeroporto[consulta])):
                    print(f"{dic_aeroporto[consulta][x]}, {dic_cidade[consulta][x]}")
            else:
                print(f"{consulta} não é um país listado na nossa base.")
        if tipo == 'cia':
            if len(dic_cias) > 0:
                print(f"A companhia aérea {consulta} opera para os aeroportos:")
                for x in range(0, len(dic_cias[consulta])):
                    print(f"{dic_cias[consulta][x]}, {dic_cidade[consulta][x]}, {dic_pais[consulta][x]}")
            else:
                print(f"A companhia aérea {consulta} não opera para nenhum dos aeroportos da base ou digitou errado.")


def main():
    arq = input()
    tipo = input()
    consulta = input()

    try:
        processar_arquivo_cliente(arq, tipo, consulta)
    except IOError:
        print('Um dos arquivos não foi encontrado ou digitou errado.')


main()
