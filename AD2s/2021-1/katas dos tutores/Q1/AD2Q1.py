import struct

def imprimirArquivo(nomeArquivo):
    with open(nomeArquivo + ".txt", "r") as arquivo:
        for linha in arquivo:
            print(linha, end="")
    print("")

def tomouDuasDoses(nome,nomeArquivoDuasDoses):
    tomouDoses = False

    with open(nomeArquivoDuasDoses + ".txt", "r") as arquivoDuasDoses:
        for linha in arquivoDuasDoses:
            dados = linha.split("#")
            if (len(dados) > 1):
                if(nome == dados[0]):
                    tomouDoses = True
                    break
    return tomouDoses

def criarArquivoDuasDoses(nomeArquivoDoses,nomeArquivoDuasDoses):
    with open(nomeArquivoDuasDoses+".txt", "w") as arquivoDuasDoses:
        with open(nomeArquivoDoses + ".txt", "r") as  arquivoDoses:
            for linha in arquivoDoses:
                dados = linha.split("#")
                if(len(dados)>1):
                    nome = dados[0]
                    vacina = dados[1]
                    dose = int(dados[2])

                    if(dose == 2):
                        arquivoDuasDoses.write(nome+"#"+vacina+"\n")

def processarArquivosUmaDose(nomeArquivoDoses,nomeArquivoDuasDoses):
    for nomeVacina in ["Coronavac","Oxford", "Pfizer", "Sputnik","Covax", "Jansen"]:
        with open(nomeVacina + ".txt", "w") as arquivoUmaDose:
            with open(nomeArquivoDoses + ".txt", "r") as  arquivoDoses:
                for linha in arquivoDoses:
                    dados = linha.split("#")
                    if (len(dados) > 1):
                        nome = dados[0]
                        vacina = dados[1]

                        if(vacina == nomeVacina and tomouDuasDoses(nome,nomeArquivoDuasDoses) == False):
                            arquivoUmaDose.write(nome+"\n")

        print("Vacinados com uma dose da",nomeVacina, "em", nomeArquivoDoses+":")
        imprimirArquivo(nomeVacina)

def main():
    nomeArquivoDoses = input()
    nomeArquivoDuasDoses = "duasDoses"

    try:
        criarArquivoDuasDoses(nomeArquivoDoses,  nomeArquivoDuasDoses)

        print("Listagem das Aplicações de Vacina",nomeArquivoDoses+":")
        imprimirArquivo(nomeArquivoDoses)

        print("Vacinados com duas doses em",nomeArquivoDoses+":")
        imprimirArquivo(nomeArquivoDuasDoses)

        processarArquivosUmaDose(nomeArquivoDoses, nomeArquivoDuasDoses)
    except IOError:
        print('Um dos arquivos não foi encontrado.')

main()