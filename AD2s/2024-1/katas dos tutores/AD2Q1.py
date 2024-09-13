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
 
def ordem(nmArq):
    arquivo = open(nmArq, "r")
    for linha in arquivo:
        numeros = linha.split()
    nmArq = numeros
    qtd = 0
    for num in nmArq:
        qtd += 1
    tamanho = int(qtd)

    for ind in range(tamanho):
        min_index = ind

        for j in range(ind+1, tamanho):
            if float(nmArq[j]) < float(nmArq[min_index]):
                min_index = j
        (nmArq[ind], nmArq[min_index]) = (nmArq[min_index], nmArq[ind])
    
    print("Ordem crescente:", end = " ")
    for i in range(tamanho):
        print(nmArq[i], end = " ")
    print(end = "\n")
    return 



# Principal
nomeArquivo = input()
mostra(nomeArquivo)
media = encontraMedia(nomeArquivo)
qtdAcima = acima(media, nomeArquivo)
print("Média dos Números em", nomeArquivo + ":", media)
print("Quantidade Acima de", media, "em " + nomeArquivo + ":", qtdAcima)
ordemInput = ordem(nomeArquivo)
