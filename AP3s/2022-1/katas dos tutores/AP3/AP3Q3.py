def jogos_it(n):
    jogos = []
    jogos.append(0)
    jogos.append(1)
    jogos.append(2)
    for i in range(3, n+1):
        jogos.append(int(jogos[i-1]) + (i-1)*int(jogos[i-2]))
    print(f"Iterativamente, temos {jogos[n]} possibilidades de jogos.")
    return


def jogos_rec(n):
    if n == 1:
        jogos = 1
    elif n == 2:
        jogos = 2
    else:
        jogos = jogos_rec(n-1) + (n-1)*jogos_rec(n-2)
    return jogos


def main():
    pos = int(input())
    jogos = jogos_rec(pos)
    print(f"Recursivamente, temos {jogos} possibilidades de jogos")

    jogos_it(pos)


main()
