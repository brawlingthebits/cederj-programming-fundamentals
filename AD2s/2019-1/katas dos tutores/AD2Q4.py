# AD2 - Questão 4

import struct


# Subprogramas
def ordenar_memoria(lista):
    for n in range(len(lista) - 1, 0, -1):
        for i in range(n):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return lista


def mostrar_memoria(lista):
    print("Ordenação na memória principal:")
    for valor in lista:
        print(valor, end=" ")
    print()


def criar_arquivo(nome_arquivo, lista):
    with open(nome_arquivo, "wb") as arq:
        arq.write(struct.pack("=i", len(lista)))  # Optei por escrever o tamanho na lista nos
        for valor in lista:                       # primeiros 4 bytes do arquivo, mas a quantidade
            arq.write(struct.pack("=i", valor))   # também pode ser deduzida do tamanho do arquivo,


def ler_valor(arq, indice):
    arq.seek(4 + indice * 4)  # [espaço ocupado pelo tamanho da lista] + [índice] * [espaço ocupado por cada valor]
    return struct.unpack("=i", arq.read(4))[0]


def escrever_valor(arq, indice, valor):
    arq.seek(4 + indice * 4)  # [espaço ocupado pelo tamanho da lista] + [índice] * [espaço ocupado por cada valor]
    arq.write(struct.pack("=i", valor))


def ordenar_arquivo(nome_arquivo):
    with open(nome_arquivo, "r+b") as arq:
        arq.seek(0)
        m = struct.unpack("=i", arq.read(4))[0]
        for n in range(m - 1, 0, -1):
            for i in range(n):
                atual = ler_valor(arq, i)
                proximo = ler_valor(arq, i + 1)
                if atual > proximo:
                    escrever_valor(arq, i, proximo)
                    escrever_valor(arq, i + 1, atual)


def mostrar_arquivo(nome_arquivo):
    print("Ordenação no arquivo:")
    with open(nome_arquivo, "rb") as arq:
        n = struct.unpack("=i", arq.read(4))[0]
        for _ in range(n):
            valor = struct.unpack("=i", arq.read(4))[0]
            print(valor, end=" ")
        print()


# Programa Principal
colecao = list(map(int, input().split()))  # Utilizei map para simplificar o código de leitura, porém o processo iterativo explícito é válido, também

colecao_ordenada = ordenar_memoria(list(colecao))
mostrar_memoria(colecao_ordenada)

criar_arquivo("colecao.bin", colecao)
ordenar_arquivo("colecao.bin")
mostrar_arquivo("colecao.bin")
