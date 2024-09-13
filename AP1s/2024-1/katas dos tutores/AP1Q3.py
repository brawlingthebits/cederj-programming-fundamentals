count = 0


def sequencias(seq, x, n):
    global count
    if x > n:
        print(seq)
        count += 1
        return
    for i in range(2*n):
        if seq[i] == -1 and (i + x + 1) < 2*n and seq[i + x + 1] == -1:
            seq[i] = x
            seq[i + x + 1] = x
            sequencias(seq, x + 1, n)
            seq[i] = -1
            seq[i + x + 1] = -1


def main():
    n = int(input())

    seq = []
    for j in range(2*n):
        seq.append(-1)

    x = 1
    sequencias(seq, x, n)

    if count == 0:
        print(f"Não há sequências possíveis com o valor {n} de entrada")
    else:
        print(f"Há {count} sequências")


main()
