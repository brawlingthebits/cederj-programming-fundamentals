# Programa AD22Q1 - 2023.2
"""
Teste:
Entrada:
ArquivoDeNumeros
Saída Correspondente:
Menor Número em ArquivoDeNumeros: 7.2100
Maior Número em ArquivoDeNumeros: 88.1234
Soma dos Números Contidos em ArquivoDeNumeros: 320.0286
"""
# Subprogramas
def processa(nmArq):
    min = max = None
    total = 0
    arquivo = open(nmArq, "r")
    for linha in arquivo:
        numero = float(linha)
        total += numero
        if min == max == None:
            min = max = numero
        elif numero < min:
            min = numero
        elif numero > max:
            max = numero
    arquivo.close()
    return min, max, total
# Principal
nomeArquivo = input()
menor, maior, soma = processa(nomeArquivo)
print("Menor Número em", nomeArquivo+":", "%.4f"%menor)
print("Maior Número em", nomeArquivo+":", "%.4f"%maior)
print("Soma dos Números Contidos em", nomeArquivo+":", "%.4f"%soma)
