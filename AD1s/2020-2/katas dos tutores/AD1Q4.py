# AD1 - Questão 4


# Subprogramas
def repetir(texto, n):
    for _ in range(n):          # Uma forma mais "pythonica" de imprimir N repetições do mesmo texto é print(texto * n, end="")
        print(texto, end="")


def espacos(n):
    repetir(" ", n)


def hashtags(n):
    repetir("#", n)


def padrao1(n):
    for m in range(1, n + 1):  # Para cada uma das N linhas, indexadas por M igual a 1, 2, ..., N
        hashtags(m)            #     Imprimir M símbolos #
        print()                #     Quebrar linha
    print()                    # Deixar uma linha em branco no final


def padrao2(n):
    espacos(n - 1)                 # Imprimir símbolo # no topo do losango
    hashtags(1)                    # ..
    print()                        # Quebrar linha
    for m in range(2, n + 1):      # Para cada linha da parte superior do losango
        espacos(n - m)             #     Imprimir o símbolo # à esquerda
        hashtags(1)                #     ..
        espacos(2 * (m - 1) - 1)   #     Imprimir o símbolo # à direita
        hashtags(1)                #     ..
        print()                    #     Quebrar linha
    for m in range(n - 1, 1, -1):  # Para cada linha da parte inferior do losango
        espacos(n - m)             #     Imprimir o símbolo # à esquerda
        hashtags(1)                #     ..
        espacos(2 * (m - 1) - 1)   #     Imprimir o símbolo # à direita
        hashtags(1)                #     ..
        print()                    #     Quebrar linha
    if n != 1:                     # Se o losango possui mais que uma linha então
        espacos(n - 1)             #     Imprimir símbolo # em baixo do losango
        hashtags(1)                #     ..
        print()                    #     Quebrar linha
    print()                        # Deixar uma linha em branco no final


def padrao3(n):
    repetir("     _ ", n)              # Imprimir topo da primeira linha de peças do quebra-cabeça
    print()                            # ..
    espacos(2)                         # ..
    repetir(" _( )__", n)              # ..
    print()                            # ..
    for m in range(1, n + 1):          # Para cada linha de peças do quebra-cabeça, indexadas de 1 até N
        if m % 2 == 1:                 #     Se o índice da linha de peças for ímpar então
            repetir(" _|    ", n + 1)  #         Imprimir padrão de peças da linha ímpar do quebra-cabeça
            print()                    #         ..
            repetir("(_   _ ", n)      #         ..
            print("(_")                #         ..
            espacos(1)                 #         ..
            repetir("|__( )_", n)      #         ..
            print("|")                 #         ..
        else:                          #     Se o índice da linha de peças for par então
            repetir(" |_    ", n + 1)  #         Imprimir padrão de peças da linha par do quebra-cabeça
            print()                    #         ..
            repetir("  _) _ ", n)      #         ..
            print("  _)")              #         ..
            espacos(1)                 #         ..
            repetir("|__( )_", n)      #         ..
            print("|")                 #         ..
    print()                            # Deixar uma linha em branco no final


# Programa Principal
numero = int(input())
padrao1(numero)
padrao2(numero)
padrao3(numero)