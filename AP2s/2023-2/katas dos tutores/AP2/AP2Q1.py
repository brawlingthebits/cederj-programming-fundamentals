# Programa AP2 - Q1
# Subprogramas
def mostra(nmArq):
    print("Conteúdo em", nmArq + ":")
    arquivo = open(nmArq, "r")
    for linha in arquivo:
        print(linha, end="")
    arquivo.close()
    return None

def encontraMedia(nmArq):
    qtd = soma = 0
    arquivo = open(nmArq, "r")
    for linha in arquivo:
        numeros = linha.split()
        for num in numeros:
            soma += float(num)
            qtd += 1
    arquivo.close()
    return soma / qtd

def acima(limite, nmArq):
    total = 0
    arquivo = open(nmArq, "r")
    for linha in arquivo:
        numeros = linha.split()
        for num in numeros:
            if float(num) > limite:
                total += 1
    arquivo.close()
    return total

# Principal
nomeArquivo = input()
mostra(nomeArquivo)
media = encontraMedia(nomeArquivo)
qtdAcima = acima(media, nomeArquivo)
print("Média dos Números em", nomeArquivo + ":", media)
print("Quantidade Acima de", media, "em " + nomeArquivo + ":", qtdAcima)
