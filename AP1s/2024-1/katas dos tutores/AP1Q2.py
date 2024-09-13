# Programa AP1Q2
# Suprogramas
def lerFaixa():
    primeiraLinha = input()
    min, max = primeiraLinha.split()
    return float(min), float(max)

def naoPertence(lis, n):
    for num in lis:
        if num == n:
            return False
    return True

def insere(lista, n):
    if naoPertence(lista, n):
        lista.append(n)
    return None

def processaEntradas(min, max):
    menores = []
    meio = []
    maiores = []
    linhaNova = input()
    while linhaNova != "":
        elementos = linhaNova.split()
        for el in elementos:
            num = float(el)
            if num < min:
                insere(menores, num)
            elif num < max:
                insere(meio, num)
            else:
                insere(maiores, num)
        linhaNova = input()
    return menores, meio, maiores

def listar(texto, lista):
    print(texto)
    for numero in lista:
        print("\t", numero)
    print()
    return None

# Principal
minimo, maximo = lerFaixa()
listaMenores, listaMeio, listaMaiores = processaEntradas(minimo, maximo)
listar("Menores que "+str(minimo)+":", listaMenores)
listar("Maiores ou Iguais a "+str(minimo)+" e Menores que "+str(maximo)+":", listaMeio)
listar("Maiores ou Iguais a "+str(maximo)+":", listaMaiores)
