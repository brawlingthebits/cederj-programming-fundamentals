# Entrada
mofit = str(input())
dna = str(input())



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


def Mofit(dna1, dna2):
    dist_opt = max(len(dna1),len(dna2))

    if (len(dna1) > len(dna2)):
        maior = dna1
        for i in range(0, len(dna1) - len(dna2) + 1):
            dna1_aux = dna1[i:(len(dna2) + i)]
            dist, pos = Dist_Hamming_C_Pos(dna1_aux, dna2)

            if dist < dist_opt:
                dist_opt = dist
                substring = i+1

        return dist_opt, substring, maior
    else:
        maior = dna2
        for i in range(0, len(dna2) - len(dna1) + 1):
            dna2_aux = dna2[i:(len(dna1) + i)]
            dist, pos = Dist_Hamming_C_Pos(dna1, dna2_aux)

            if dist < dist_opt:
                dist_opt = dist
                substring = i+1

        return dist_opt, substring, maior


resultado = Mofit(mofit, dna)

print(f"A subcadeia mais próxima tem {resultado[0]} cacarteres distintos e começa na posição {resultado[1]} da cadeia {resultado[2]}")