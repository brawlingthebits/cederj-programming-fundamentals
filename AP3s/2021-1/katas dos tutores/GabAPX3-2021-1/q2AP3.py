import struct

Dicionario = struct.Struct("30s 100s")
printInfo = False


def decodificaDadosDicionario(bloco):
    campos = Dicionario.unpack(bloco)

    nome = campos[0].decode("utf-8").strip(chr(0))
    definicao = campos[1].decode("utf-8").strip(chr(0)).strip('\n')

    return nome, definicao



def dist_palavra1_palavra2(w1, w2):
    if len(w1) == len(w2):
        maximo = len(w2)
    elif len(w1) < len(w2):
        maximo = len(w1)
    else:
        maximo = len(w2)
    dist = 0
    p = 0
    while p <= maximo - 1:
        if w1[p] != w2[p]:
            dist += 1
        p += 1
    return dist


def percorre_palavra1_palavra2(w1, w2):
    result = ''

    if len(w2) > len(w1):
        maior = w2
        menor = w1
    else:
        maior = w1
        menor = w2

    for i in range(0, len(maior) - len(menor) + 1):
        aux = maior[i:(len(menor) + i)]
        dist = dist_palavra1_palavra2(menor, aux)

        if dist <= 1:
            result += f'{dist} '

    ordenada_result = sorted(result)
    nova_result = ' '.join(ordenada_result).split()

    if len(nova_result) > 0:
        menor_distancia = nova_result[0]
        return menor_distancia
    else:
        return 3

def processaArquivoDicionario(nomeArquivoDicionario,tipo,consulta):
    with open(nomeArquivoDicionario, "rb") as arquivo:
        dic_nome = dict()
        marcador = 0
        while True:
            bloco = arquivo.read(Dicionario.size)
            if not bloco:
                break
            nome, definicao = decodificaDadosDicionario(bloco)
            if tipo == 'todas_palavras':
                if consulta in nome[0]:
                    if nome not in dic_nome.keys():
                        dic_nome[nome] = [definicao]
                    else:
                        dic_nome[nome].append(definicao)

            elif tipo == 'unica_palavra':
                dist = percorre_palavra1_palavra2(consulta, nome)
                if int(dist) == 0:
                    if len(consulta) == len(nome):
                        print(f"A palavra {consulta} possui a seguinte definição: {definicao}")
                        marcador = 1
                        break
                    else:
                        print(f"Você quis dizer: {nome}? Neste caso, sua definição é: {definicao}")
                        marcador = 1
                elif int(dist) == 1:
                    print(f"Você quis dizer: {nome}? Neste caso, sua definição é: {definicao}")
                    marcador = 1

        if marcador == 0 and tipo == 'unica_palavra':
            print(f"A palavra {consulta} não foi encontrada, nem ao menos palavras similares.")

        if tipo == 'todas_palavras':
            if len(dic_nome) == 0:
                print(f"Não há palavras iniciando com a letra {consulta}")
            else:
                for item in sorted(dic_nome):
                    print(item)
                    for item2 in dic_nome[item]:
                        print(item2)

    return



def main():
    arq = input()
    tipo = input()
    query = input()
    processaArquivoDicionario(arq, tipo, query)

main()