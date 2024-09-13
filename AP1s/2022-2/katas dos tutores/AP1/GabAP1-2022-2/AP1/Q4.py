def bac_rec(n, n1, n2, n3):
    if n == 1:
        qtd = n1
    elif n == 2:
        qtd = n2
    elif n == 3:
        qtd = n3
    else:
        qtd = bac_rec(n-1, n1, n2, n3)*3 + bac_rec(n-2, n1, n2, n3)*2 - 5*bac_rec(n-3, n1, n2, n3)/3
    return qtd


def bac_it(n, n1, n2, n3):
    bac = []
    bac.append(n1)
    bac.append(n2)
    bac.append(n3)
    for i in range(3, n):
        bac.append(bac[i-1]*3 + bac[i-2]*2 - 5*bac[i-3]/3)
    return bac[n-1]


def main():
    ano = int(input())
    ano1 = 10
    ano2 = 30
    ano3 = 50
    nbacrec = bac_rec(ano, ano1, ano2, ano3)
    nbacit = bac_it(ano, ano1, ano2, ano3)
    print(f"Recursivamente: No ano 1 há {ano1} bactérias, no ano 2, {ano2}, e no ano 3, {ano3}. Assim, no ano {ano} há {'%.2f'% nbacrec} bactérias.\n")
    print(f"Iterativamente: No ano 1 há {ano1} bactérias, no ano 2, {ano2}, e no ano 3, {ano3}. Assim, no ano {ano} há {'%.2f'% nbacit} bactérias.\n")


main()
