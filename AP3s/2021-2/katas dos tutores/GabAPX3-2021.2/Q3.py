def primo(n):
    for i in range(2, int(n/2 +1)):
        if n%i == 0:
            return 0
    return 1


def funcao_primos(a,b):
    k = 0
    i = 0
    qtd = 0
    while k == 0:
        resp = i**2 + a*i + b
        is_prime = primo(resp)
        if is_prime == 1 and resp != 1:
            qtd += 1
            i = i+1
        else:
            k = 1
    return qtd


def compara(tot1, tot2):
    max = 0
    for a in range(0, tot1):
        for b in range(0, tot2):
            saida = funcao_primos(a,b)
            if saida >= max:
                max = saida
                coef1 = a
                coef2 = b

    print(f"A função com maior número de termos primos é: n^2 + {coef1}n + {coef2}")
    print(f"O maior número de termos primos consecutivos é {max}")


def main():
    val1 = int(input())
    val2 = int(input())
    compara(val1, val2)


main()
