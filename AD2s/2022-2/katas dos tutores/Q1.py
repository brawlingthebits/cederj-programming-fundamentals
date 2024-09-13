# AD2.2022.2 - Questão 1
# Programa Completo
# Subprogramas
def mostra(nm):
    print("Conteúdo do Arquivo:", nm)
    dados = open(nm, "r")
    for linha in dados:
        print(linha, end="")
    dados.close()
    return None


def calculaMedia(nm):
    somaNums = qtdNums = 0
    dados = open(nm, "r")
    for linha in dados:
        numero = float(linha)
        somaNums += numero
        qtdNums += 1
    return somaNums / qtdNums


def removeAbaixo(nm, minimo):
    dados = open(nm, "r")
    temporario = open(nm + "temp", "w")
    for linha in dados:
        if float(linha) >= minimo:
            temporario.write(linha)
    dados.close()
    temporario.close()
    dados = open(nm, "w")
    temporario = open(nm + "temp", "r")
    for linha in temporario:
        dados.write(linha)
    dados.close()
    temporario.close()
    return None


# Principal
nomeArquivo = input()
mostra(nomeArquivo)
media = calculaMedia(nomeArquivo)
print("Média dos números contidos no arquivo:", media)
removeAbaixo(nomeArquivo, media)
mostra(nomeArquivo)
