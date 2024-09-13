def ordena(s):
    for i in range(len(s)):
        min = i
        for j in range(i + 1, len(s)):
            if int(s[j]) < int(s[i]):
                min = j

        aux = s[i]
        s[i] = s[min]
        s[min] = aux

    return s

def eh_inteiro(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def main():
    seq = input()
    seq = seq.split( )

    nao_int = []
    for i in range(len(seq)):
        if eh_inteiro(seq[i]) is False:
            nao_int.append(seq[i])

    if len(nao_int) == 0:
        print(f"Os elementos em ordem não decrescente são:", end=" ")
        s = ordena(seq)
        for i in range(len(s)-1):
            print(s[i], end=" ")
        print(s[len(s)-1])

        meio = len(s)//2
        print(f"A mediana é o elemento {s[meio]}")
    elif len(nao_int) == 1:
        print(f"Há um elemento que não é inteiro, ele é:", end=" ")
        print(nao_int[0], end=" ")
    else:
        qtd = len(nao_int)
        print(f"Há {qtd} que não são inteiros, eles são:", end=" ")
        for i in range(len(nao_int)):
            print(nao_int[i], end=" ")

main()
