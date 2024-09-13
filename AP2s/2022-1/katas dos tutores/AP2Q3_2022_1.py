# Programa Completo - Prova 2 - Questão 3 - 2022.1
# Subprogramas
def mostra(msg, nm):
    print(msg)
    dados = open(nm, "r")
    for linhaLida in dados:
        print(linhaLida, end="")
    dados.close()
    print()
    return None


def ehPrimo(n):
    for divisor in range(2, 1 + n // 2):
        if n % divisor == 0:
            return False
    return n > 1


def naoOcorrePrimos(nums):
    for num in nums:
        if ehPrimo(num):
            return False
    return True


def removeLinhasComPrimos(nm):
    dados = open(nm, "r")
    temporario = open("temp.txt", "w")
    for linhaDeNumeros in dados:
        numeros = linhaDeNumeros.split()
        for i in range(len(numeros)):
            numeros[i] = int(numeros[i])
        if naoOcorrePrimos(numeros):
            temporario.write(linhaDeNumeros)
    temporario.close()
    dados.close()
    dados = open(nm, "w")
    temporario = open("temp.txt", "r")
    for linhaLida in temporario:
        dados.write(linhaLida)
    dados.close()
    temporario.close()
    import os  # Não cobrado na correção
    os.remove("temp.txt")  # Não cobrado na correção
    return None


# Principal
nomeArquivo = input()
mostra("Conteúdo do Arquivo %s:" % nomeArquivo, nomeArquivo)
removeLinhasComPrimos(nomeArquivo)
mostra("Conteúdo do Arquivo %s após eventuais remoções:" % nomeArquivo, nomeArquivo)
