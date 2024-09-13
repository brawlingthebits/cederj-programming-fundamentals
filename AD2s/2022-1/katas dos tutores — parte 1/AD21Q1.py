# Programa Completo da AD21 - Questão 1 - 2022.1
# Subprogramas
def mostrar(nm):
    print("Conteúdo do Arquivo", nm+":")
    dados = open(nm, "r")
    for linha in dados:
        print("\t", linha.strip())
    dados.close()
    print()
    return None

def calculaDesvio(nm, med, qtd):
    somatorio = 0
    dados = open(nm, "r")
    for linha in dados:
        numeros = list(map(int, linha.split()))
        for num in numeros:
            somatorio += (num-med)**2
    dados.close()
    return (somatorio/qtd)**0.5

# Principal
nomeArq = input()
dados = open(nomeArq, "r")
linha = dados.readline()
if linha == "":
    print("Não existem menor, maior, média e desvio, pois o arquivo está vazio!!!")
    dados.close()
else:
    qtdNumeros = somaNumeros = 0
    menor = maior = list(map(int, linha.split()))[0]
    while linha != "":
        numerosNaLinha = list(map(int, linha.split()))
        qtdNumeros += len(numerosNaLinha)
        for numero in numerosNaLinha:
            somaNumeros += numero
            if numero < menor:
                menor = numero
            elif numero > maior:
                maior = numero
        linha = dados.readline()
    media = somaNumeros / qtdNumeros
    dados.close()
    mostrar(nomeArq)
    print("Menor Valor em", nomeArq + ":", menor)
    print("Maior Valor em", nomeArq + ":", maior)
    print("Média dos Valores em", nomeArq + ":", "%.2f"%media)
    desvio = calculaDesvio(nomeArq, media, qtdNumeros)
    print("Desvio Padrão em", nomeArq + ":", "%.2f"%desvio)

