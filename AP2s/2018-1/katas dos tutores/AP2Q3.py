# AP2 - Questão 3

# Subprogramas


def obterValor(arq, ind):
    import struct
    arq.seek(ind * 8, 0)
    return struct.unpack("=d", arq.read(8))[0]


def buscar(arq, num):
    arq.seek(0, 2)
    tam = arq.tell()  # Aula 12 - tamanho em bytes

    inicio = 0  # Índice do primeiro registro/valor
    fim = tam // 8 - 1  # Índice do último registro/valor
    meio = (inicio + fim) // 2
    while (inicio < fim) and (num != obterValor(arq, meio)):
        if num > obterValor(arq, meio):
            inicio = meio + 1
        else:
            fim = meio - 1
        meio = (inicio + fim) // 2
    if meio < 0 or tam // 8 <= meio or num != obterValor(arq, meio):
        return -1
    else:
        return meio


# Programa Principal
nomeArquivo = input("Informe o nome do arquivo binário de números: ")
with open(nomeArquivo, "rb") as arquivo:
    numero = float(input("Favor informar o valor a ser encontrado: "))
    posicao = buscar(arquivo, numero)
    if posicao != -1:
        print("O número está na posição %d" % posicao)  # Quebra de linha (\n) incluída por print implicitamente
    else:
        print("O número não foi encontrado.")  # Quebra de linha (\n) incluída por print implicitamente
