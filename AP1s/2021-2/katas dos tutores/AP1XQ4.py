def ordena(sequencia):
    if len(sequencia) > 1:
        meio = len(sequencia)//2
        primeirametade = sequencia[:meio]
        segundametade = sequencia[meio:]

        ordena(primeirametade)
        ordena(segundametade)

        i = 0
        j = 0
        k = 0

        while i < len(primeirametade) and j < len(segundametade):
            if primeirametade[i] <= segundametade[j]:
                sequencia[k] = primeirametade[i]
                i += 1
            else:
                sequencia[k] = segundametade[j]
                j += 1

            k += 1

        while i < len(primeirametade):
            sequencia[k] = primeirametade[i]
            i += 1
            k += 1

        while j < len(segundametade):
            sequencia[k] = segundametade[j]
            j += 1
            k += 1

    return sequencia


def buscabin(seq, menor, maior, x):
    if maior >= menor:
        meio = (menor + maior) // 2

        if seq[meio] == x:
            print(f"O elemento {x} está na posição {meio+1}")
            return 1, meio
        elif seq[meio] > int(x):
            return buscabin(seq, menor, meio - 1, x)
        else:
            return buscabin(seq, meio + 1, maior, x)
    else:
        print(f" O elemento {x} não consta na lista e, caso deseje, ele será inserido na posição {maior+2}")
        return -1, maior+2


def insercao(seq, x, pos):
    print(f"Você deseja inserir o elemento {x}? Insira S (s) ou N (n)")
    resposta = input()
    if resposta == 'S' or resposta == 's':
        seq.append(0)
        for i in range(len(seq)-1, int(pos)-1, -1):
            seq[i] = seq[i-1]
        seq[pos-1] = x
        print(seq)
        return seq
    elif resposta == 'N' or resposta == 'n':
        print(seq)
        return 0
    else:
        print("Opção não encontrada")
        insercao(seq, x, pos)


def remocao(seq, x, pos):
    print(f"Você deseja remover o elemento {x}? Insira S (s) ou N (n)")
    resposta = input()
    if resposta == 'S' or resposta == 's':
        for i in range(pos, len(seq)-1):
            seq[i] = seq[i+1]
        print(seq[:(len(seq)-1)])
        return seq
    elif resposta == 'N' or resposta == 'n':
        print(seq)
        return 0
    else:
        print("Opção não encontrada")
        remocao(seq, x, pos)


def main():
    entrada = input()
    seqentrada = entrada.split()

    lst = []
    for i in range(len(seqentrada)):
        lst.append(int(seqentrada[i]))
    ordenada = ordena(lst)
    print(f"A lista ordenada é: {ordenada}")

    busca = int(input())
    saida, pos = buscabin(ordenada, 0, len(ordenada)-1, busca)
    if saida == -1:
        insercao(ordenada, busca, pos)
    else:
        remocao(ordenada, busca, pos)


main()
