import struct
Series = struct.Struct("4s 30s 60s")
printInfo = False

def decodificaDadosSeries(bloco):
    campos = Series.unpack(bloco)

    ano_serie = campos[0].decode("utf-8")
    nome_serie = campos[1].decode("utf-8").strip(chr(0))
    nome_plataforma = campos[2].decode("utf-8").strip(chr(0)).strip('\n')

    return ano_serie, nome_serie, nome_plataforma

def processarArquivoSeries(nomeArquivoSeries,tipo,consulta):
    with open(nomeArquivoSeries, "rb") as arquivo:
        plataforma = dict()
        serie = dict()
        while(True):
            bloco = arquivo.read(Series.size)
            if(not bloco):
                break
            ano_serie, nome_serie, nome_plataforma = decodificaDadosSeries(bloco)
            if(tipo == 'Ano'):
                if(consulta == ano_serie):
                    if(nome_plataforma not in plataforma.keys()):
                        plataforma[nome_plataforma] = [nome_serie]
                    else:
                        plataforma[nome_plataforma].append(nome_serie)

            elif(tipo == 'Serie'):
                if (consulta in nome_serie):
                    ano = ano_serie
                    if (nome_serie not in serie.keys()):
                        serie[nome_serie] = [nome_plataforma]
                    else:
                        serie[nome_serie].append(nome_plataforma)

            elif(tipo == 'Plataforma'):
                if (consulta in nome_plataforma):
                    if (ano_serie not in plataforma.keys()):
                        plataforma[ano_serie] = [nome_serie]
                    else:
                        plataforma[ano_serie].append(nome_serie)

            else:
                print(f"{tipo} não é um tipo possível a ser consultado.")
                break


        if(tipo == 'Ano'):
            if(len(plataforma)==0):
                print(f"No catálogo apresentado não há séries produzidas no ano de {consulta}")
            else:
                for item in sorted(plataforma):
                    print(item)
                    for item2 in sorted(plataforma[item]):
                        print(item2)

        if (tipo == 'Serie'):
            if (len(serie) == 0):
                print(f"{consulta} não está listado no catálogo")
            else:
                servicos = sorted(serie[consulta])
                ultimoServico = servicos[len(servicos) - 1]
                primeiroServico = servicos[0]
                catalogoString = ""

                for item in servicos:
                    if (item == ultimoServico):
                        catalogoString += " e "
                    elif (item != primeiroServico):
                        catalogoString += ", "
                    catalogoString += item

                print(f"{consulta} possui produção de {ano} e está em cartaz em: {catalogoString}.")

        if(tipo == 'Plataforma'):
            if (len(plataforma) == 0):
                print(f"{consulta} não está listado no catálogo")
            else:
                for item in sorted(plataforma):
                    print(item)
                    for item2 in sorted(plataforma[item]):
                        print(item2)


def main():
    nomeArquivoSeries = input()
    tipo = input()
    consulta = input()

    try:
        processarArquivoSeries(nomeArquivoSeries,tipo,consulta)
    except IOError:
        print('Um dos arquivos não foi encontrado.')

main()