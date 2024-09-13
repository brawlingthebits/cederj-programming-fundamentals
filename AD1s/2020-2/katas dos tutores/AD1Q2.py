# AD1 - Questão 2


# Subprogramas
def primo(n):
    if n < 2:
        return False
    else:
        for divisor in range(2, int(n ** 0.5) + 1):
            if n % divisor == 0:
                return False
        return True


def mostra(vals):
    for x in vals:
        print(x)


def pegaPares(vals):
    listaPares = []
    for x in vals:
        if x % 2 == 0:
            listaPares.append(x)
    return listaPares


def pegaPrimos(vals):
    listaPrimos = []
    for x in vals:
        if primo(x):
            listaPrimos.append(x)
    return listaPrimos


# Programa Principal
numeros = list(map(int, input().split()))
if len(numeros) == 0:
    print("Nenhum Número Foi Lido!!!")
else:
    pares = pegaPares(numeros)
    if len(pares) > 0:
        print("Relação de Par(es)")
        mostra(pares)
        print("Fim da Relação de Par(es).")
        print()
    primos = pegaPrimos(numeros)
    if len(primos) > 0:
        print("Relação de Primo(s)")
        mostra(primos)
        print("Fim da Relação de Primo(s).")