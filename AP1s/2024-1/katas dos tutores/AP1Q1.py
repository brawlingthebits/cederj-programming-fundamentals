# Programa AP1Q1
# Suprogramas
def maisDigitos(linha):
    qtdDigitos = 0
    for caracter in linha:
        if "0" <= caracter <= "9":
            qtdDigitos += 1
    return 2*qtdDigitos > len(linha)

# Principal
qtdLinhasProcessadas = int(input())
for i in range(qtdLinhasProcessadas):
    linhaProcessada = input()
    if maisDigitos(linhaProcessada):
        print(linhaProcessada)
