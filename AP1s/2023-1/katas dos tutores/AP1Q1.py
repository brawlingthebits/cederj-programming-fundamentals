"""
Teste:
Entradas:
1
0
997
2
4

Saídas Correspondentes:
Listagem de Pares:
    0
    2
    4
Fim da Listagem de Pares
Listagem de Ímpares:
    1
    997
Fim da Listagem de Ímpares
Listagem de Primos:
    997
    2
Fim da Listagem de Primos
Obrigado por utilizar nosso sistema!!!

"""
# Programa AD11.Q1


# Subprograma(s)
def pegaNumeros():
    listaNumeros = []
    linhaLida = input()
    while linhaLida != "":
        listaNumeros.append(int(linhaLida))
        linhaLida = input()
    return listaNumeros


def mostraPares(listaNumeros):
    print("Listagem de Pares:")
    for num in listaNumeros:
        if num % 2 == 0:
            print("   ", num)
    print("Fim da Listagem de Pares")
    return None


def mostraImpares(listaNumeros):
    print("Listagem de Ímpares:")
    for num in listaNumeros:
        if num % 2 == 1:
            print("   ", num)
    print("Fim da Listagem de Ímpares")
    return None


def mostraPrimos(listaNumeros):
    def ehPrimo(n):
        for divisor in range(2, 1 + n // 2):
            if n % divisor == 0:
                return False
        return n > 1

    print("Listagem de Primos:")
    for num in listaNumeros:
        if ehPrimo(num):
            print("   ", num)
    print("Fim da Listagem de Primos")
    return None


# Principal
# Inicialização
numeros = pegaNumeros()
# Processamento
mostraPares(numeros)
mostraImpares(numeros)
mostraPrimos(numeros)
# Finalização
print("Obrigado por utilizar nosso sistema!!!")
