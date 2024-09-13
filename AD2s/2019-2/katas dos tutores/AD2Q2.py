# AD2 - Questão 2


# Subprogramas
def mostrar(nm):  # não solicitado
    dados = open(nm, "r")
    for linha in dados:
        print(linha, end = "")
    print()
    dados.close()
    return None

def primo(n):
    for divisor in range(2, n//2):
        if n%divisor == 0:
            return False
    return n > 1

def copiaPrimos(nm, nmPrimos):
    dados = open(nm, "r")
    dadosDest = open(nmPrimos, "w")
    for linha in dados:
        numeros = list(map(int, linha.split()))
        for num in numeros:
            if primo(num):
                dadosDest.write(str(num)+" ")
        dadosDest.write("\n")
    dados.close()
    dadosDest.close()
    return None

# Programa Principal
nomeOrigem, nomeDestino = input().split()
mostrar(nomeOrigem) # não solicitado
copiaPrimos(nomeOrigem, nomeDestino)
mostrar(nomeDestino) # não solicitado