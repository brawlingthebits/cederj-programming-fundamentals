"""
Q6: Faça um programa que leia pares de números inteiros, chamados decimal e base, do teclado
até que um decimal negativo seja digitado ou uma base fora do intervalo 2 a 9 seja digitada.
Com exceção do último par lido, que representa um par delimitador de fim, chame a função
recursiva, chamada converte, que produza a string de conversão do decimal na nova base,
ambos recebidos como parâmetro. Seu programa deve completar o subprograma cujo
cabeçalho é dado a seguir:
                     def converte(decimal, base):
                             ...
"""


# Subprogramas
def converte(decimal, base):
    if decimal < base:
        return str(decimal)
    else:
        return converte(decimal // base, base) + str(decimal % base)


# Programa Principal
leitura = input().split()
decimal = int(leitura[0])
base = int(leitura[1])

while decimal >= 0 and 2 <= base <= 9:
    print(decimal, "na base", base, "=", converte(decimal, base))
    leitura = input().split()
    decimal = int(leitura[0])
    base = int(leitura[1])