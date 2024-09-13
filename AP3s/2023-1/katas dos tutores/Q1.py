def fib_it(n, n1, n2):
    fib = []
    fib.append(int(n1))
    fib.append(int(n2))
    for i in range(2, n):
        fib.append(int(fib[i-1]) + int(fib[i-2]))
    print(f"Os {n} elementos da sequência são {fib}.")

    seqpar = []
    for i in range(0, n):
        if fib[i]%2 == 0:
            seqpar.append(fib[i])

    if len(seqpar) == 0:
        print(f"Não há elementos pares na sequência até a posição {n}.")
    else:
        quadrado = []
        for i in range(0,len(seqpar)):
            for j in range(2, int(seqpar[i])):
                if j**2 == seqpar[i]:
                    quadrado.append(seqpar[i])

        if len(quadrado) == 0:
            print(
                f"Os elementos pares da sequência são {seqpar}. Não há elemento par quadrado perfeito.")
        else:
            print(f"Os elementos pares da sequência são {seqpar}.")
            print(f"Dentre esses, os que são quadrado perfeito são {quadrado}.")
    return

def main():
    pos = int(input())
    f1 = float(input())
    f2 = float(input())
    fib_it(pos, f1, f2)


main()
