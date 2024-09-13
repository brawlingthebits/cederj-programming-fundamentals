
def dist_palavra1_palavra2(w1, w2):
    if len(w1) == len(w2):
        maximo = len(w2)
    elif len(w1) < len(w2):
        maximo = len(w1)
    else:
        maximo = len(w2)
    dist = 0
    p = 0
    while p <= maximo - 1:
        if w1[p] != w2[p]:
            dist += 1
        p += 1
    return dist


def count_vogais(w):
    count = ''
    count_a = 0
    count_e = 0
    count_i = 0
    count_o = 0
    count_u = 0
    count_aa = 0
    count_ee = 0
    count_ii = 0
    count_oo = 0
    count_uu = 0
    for letra in range(0, len(w)):
        if w[letra] in {'a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'u', 'ú'}:
            count += f'{w[letra]}'
            if w[letra] == 'a':
                count_a += 1
            if w[letra] == 'á':
                count_aa += 1
            elif w[letra] == 'e':
                count_e += 1
            elif w[letra] == 'i':
                count_i += 1
            elif w[letra] == 'í':
                count_ii += 1
            elif w[letra] == 'o':
                count_o += 1
            elif w[letra] == 'ó':
                count_oo += 1
            elif w[letra] == 'u':
                count_u += 1
            elif w[letra] == 'ú':
                count_uu += 1
    return count, count_a+count_aa, count_e+count_ee, count_i+count_ii, count_o+count_oo, count_u+count_uu

def compara_tamanhos(w1, w2):
    vogais_p1, p1count_a, p1count_e, p1count_i, p1count_o, p1count_u = count_vogais(w1)
    vogais_p2, p2count_a, p2count_e, p2count_i, p2count_o, p2count_u = count_vogais(w2)
    if len(vogais_p1) > len(vogais_p2):
        print(f"Dentre {w1} e {w2}, a palavra que mais possui vogais é {w1}, com {len(vogais_p1)} vogais.")
        print(f"A palavra {w1} possui {p1count_a} a's, {p1count_e} e's, {p1count_i} i's, {p1count_o} o's e {p1count_u} u's.")
    elif len(vogais_p2) > len(vogais_p1):
        print(f"Dentre {w1} e {w2}, a palavra que mais possui vogais é {w2}, com {len(vogais_p2)} vogais.")
        print(f"A palavra {w2} possui {p2count_a} a's, {p2count_e} e's, {p2count_i} i's, {p2count_o} o's e {p2count_u} u's.")
    elif len(vogais_p2) == len(vogais_p1):
        print(f"As palavras {w1} e {w2} possuem o mesmo número de vogais, que é {len(vogais_p1)}.")


def main():
    palavra1 = input()
    palavra2 = input()
    dist = dist_palavra1_palavra2(palavra1,palavra2)
    print(f"As palavras {palavra1} e {palavra2} estão a uma distância {dist}")
    compara_tamanhos(palavra1,palavra2)

main()