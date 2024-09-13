# letra A
def eh_int(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

# letra B
def compara_elementos(seq):
    aux = 0
    for i in range(len(seq)):
        if i+1 == int(seq[i]):
            aux += 1
    return aux


# letra C
def verifica_ordem(seq):
    i = 0
    while i < len(seq)-1 and seq[i] <= seq[i+1]:
        i += 1
    if i < len(seq)-1:
        return 0
    else:
        return 1

# letra D
def retorne_pares(seq):
    pares = []
    for i in range(len(seq)):
        if int(seq[i])%2 == 0:
            pares.append(seq[i])
    if len(pares) == 0:
        print(f"Não há elementos pares em {seq}")
    else:
        print(f"A lista dos elementos pares de {seq} em ordem de aparição é {pares}")


def main():
    entrada = input()
    if eh_int(entrada):
        entrada = str(entrada)
        qtd = compara_elementos(entrada)
        if qtd == 0:
            print(f"Na entrada {entrada} não há elementos com valores iguais as suas posições")
        elif qtd == 1:
            print(f"Na entrada {entrada} há 1 elemento com valor igual a sua posição")
        else:
            print(f"Na entrada {entrada} há {qtd} elementos com valores iguais as suas posições")

        ordenado = verifica_ordem(entrada)
        if ordenado == 0:
            print(f"A entrada {entrada} não está ordenada")
        else:
            print(f"A entrada {entrada} está ordenada")
            retorne_pares(entrada)
    else:
        print(f"A entrada {entrada} não está do formato solicitado")


main()
