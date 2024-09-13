def menor(seq):
    min = seq[0]
    pos = 0
    for i in range(len(seq)):
        if int(seq[i]) < int(min):
            min = seq[i]
            pos = i
    return pos, min

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

def busca_bin(seq,menor,maior,x):
    if maior >= menor:
        meio = (menor + maior) // 2
        if int(seq[meio]) == int(x):
            return meio
        elif int(seq[meio]) > int(x):
            return busca_bin(seq, menor, meio - 1, x)
        else:
            return busca_bin(seq, meio + 1, maior, x)
    else:
        return -1

def main():
    seq = input()
    seq = seq.split( )

    print(f"A entrada é:", end=" ")
    for i in range(len(seq)-1):
        print(seq[i], end=" ")
    print(seq[len(seq)-1])

    pos, min = menor(seq)
    ordem = ordena(seq)

    print(f"O menor elemento da sequência da entrada é {min}, ele está na posição {pos+1}")

    print(f"Ordenando a sequência, temos:", end=" ")
    for i in range(len(ordem)-1):
        print(ordem[i], end=" ")
    print(ordem[len(ordem)-1])

    print("qual elemento você quer buscar?")

    x = input()
    pos_busca = busca_bin(ordem, 0, len(ordem) - 1, x)

    if pos_busca != -1:
        print(f"Elemento {x} está na posição {pos_busca +1}")
        tam = 0
        posicoes = []
        for i in range(len(ordem)):
            if int(ordem[i]) == int(x):
                tam += 1
                posicoes.append(i+1)
        if len(posicoes) > 1:
            print(f"Além da posição {pos_busca +1}, todas as posições que contém o elemento {x} são:")
            for i in range(len(posicoes) - 1):
                print(posicoes[i], end=" ")
            print(posicoes[len(posicoes) - 1])
    else:
        print(f"Elemento {x} não se encontra na sequência")


main()
