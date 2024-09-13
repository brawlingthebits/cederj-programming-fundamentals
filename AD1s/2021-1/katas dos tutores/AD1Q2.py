# Entrada
tam = int(input())
mofit = str(input())
dna = str(input())

# Pre processamento
if (tam > 50):
    print("Valores não estão de acordo")
    exit()
if (len(mofit) > 50):
    print("Valores não estão de acordo")
    exit()
if (len(dna) > 500):
    print("Valores não estão de acordo")
    exit()


# dna1 e dna2 devem ter msm tamanho
def Dist_Hamming_C_Pos(dna1, dna2):
    dist = 0
    p = 0
    pos = ''
    while (p <= len(dna2) - 1):
        if (dna1[p] != dna2[p]):
            q = str(p + 1)
            pos += f'{q} '
            dist += 1
        p += 1
    return dist, pos


def Mofit(dna1, dna2, k):
    result = ''

    if (len(dna1) > len(dna2)):
        return result

    for i in range(0, len(dna2) - len(dna1) + 1):
        dna2_aux = dna2[i:(len(dna1) + i)]
        dist, pos = Dist_Hamming_C_Pos(dna1, dna2_aux)

        if (dist <= k):
            result += f'\n{i + 1} {pos}'

    return result


resultado = Mofit(mofit, dna, tam)

if resultado:
    print(f"As substrings com distância no máximo {tam} do mofit e as posições são: {resultado}")
else:
    print("Valores não estão de acordo")