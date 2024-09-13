def ordena(s):
    for i in range(len(s)-1):
        min = i
        for j in range(i + 1, len(s)):
            if int(s[j]) < int(s[min]):
                min = j
        aux = s[i]
        s[i] = s[min]
        s[min] = aux

    return s

def inverte(s):
    for i in range(0,len(s)//2):
        aux = s[i]
        s[i] = s[len(s) - 1 - i]
        s[len(s) - 1 - i] = aux
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

        print(f"A sequência em ordem não crescente é:", end=" ")
        s2 = inverte(s)
        for i in range(len(s2)-1):
            print(s2[i], end=" ")
        print(s2[len(s2)-1])

    elif len(nao_int) == 1:
        print(f"Há um elemento que não é inteiro, ele é:", end=" ")
        print(nao_int[0], end=" ")
    else:
        qtd = len(nao_int)
        print(f"Há {qtd} que não são inteiros, eles são:", end=" ")
        for i in range(len(nao_int)):
            print(nao_int[i], end=" ")

main()
