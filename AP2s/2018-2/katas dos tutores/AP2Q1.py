# AP2 - Questão 1


# Programa Principal
with open("entrada.txt", "r") as entrada:
    with open("traducao.txt", "w") as saida:
        t = int(entrada.readline().rstrip())

        for i in range(t):
            m, n = map(int, entrada.readline().rstrip().split())

            dicionario = dict()
            for _ in range(m):
                palavra = entrada.readline().rstrip()
                traducao = entrada.readline().rstrip()
                dicionario[palavra] = traducao

            for _ in range(n):
                primeira = True
                palavras = entrada.readline().rstrip().split()
                for palavra in palavras:
                    if primeira:
                        primeira = not primeira
                    else:
                        saida.write(" ")

                    if palavra in dicionario:
                        saida.write(dicionario[palavra])
                    else:
                        saida.write(palavra)
                saida.write("\n")
            saida.write("\n")