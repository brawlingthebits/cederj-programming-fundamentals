def flores_rec(n, n1, n2):
    if n == 1:
        qtd = n1
    elif n == 2:
        qtd = n2
    else:
        qtd = flores_rec(n-1, n1, n2)*2 - flores_rec(n-2, n1, n2)/2
    return qtd


def flores_it(n, n1, n2):
    flores = []
    flores.append(n1)
    flores.append(n2)
    for i in range(2, n):
        flores.append(flores[i-1]*2 - flores[i-2]/2)
    return flores[n-1]


def main():
    ano = int(input())
    ano1 = float(input())
    ano2 = float(input())
    nfloresrec = flores_rec(ano, ano1, ano2)
    nfloresit = flores_it(ano, ano1, ano2)
    print(f"No ano 1 há {ano1} flores e no ano 2, {ano2}. Assim, no ano {ano} há {'%.2f'% nfloresrec} flores.\n")
    print('%.2f' % nfloresit)


main()
