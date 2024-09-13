def binario(seq):
    i = 0
    while i <= len(seq)-1:
        if seq[i] == '0' or seq[i] == '1':
            i += 1
        else:
            return 0
    return 1


def soma(seq):
    i = len(seq)-1
    while seq[i] != '0' and i != -1:
        seq = seq[:i] + '0' + seq[(i+1):]
        print(seq)
        i -= 1
    if seq[i] == '0' and i != -1:
        seq = seq[:i] + '1' + seq[(i+1):]
        print(seq)
        return seq
    else:
        seq = '1' + seq
        print(seq)
        return seq


def main():
    seq = input()
    saida = binario(seq)
    if saida == 1:
        print(f"a soma de {seq} por 1 é: ")
        soma(seq)
    else:
        print(f"{seq} não está codificado em binário")


main()
