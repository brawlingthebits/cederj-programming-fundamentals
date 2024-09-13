permut = input()


def repeticoes(permutacao):
    permutacao = permutacao.split()
    rep = []
    for i in range(len(permutacao)-1):
        for j in range(i+1, len(permutacao)):
            if permutacao[i] == permutacao[j]:
                rep.append(permutacao[j])
    return rep


def inverter(permutacao):
    permutacao = permutacao.split()
    perm = []
    for i in range(len(permutacao)-1, -1, -1):
        perm.append(permutacao[i])
    inv = " "
    return inv.join(perm)


def inversao(permutacao):
    permutacao = permutacao.split()
    inv = []
    qtd_inv = 0
    for i in range(len(permutacao)-1):
        for j in range(i+1, len(permutacao)):
            if int(permutacao[i]) > int(permutacao[j]):
                a = (i+1, j+1)
                inv.append(a)
                qtd_inv += 1
    return inv, qtd_inv




saida = repeticoes(permut)
saida2 = inverter(permut)
saida3, qtd = inversao(permut)

print(f"Os elementos que se repetem são: {saida}")
print(f"Sequência inversa: {saida2}")
print(f"Há {qtd} inversões, e as posições são: {saida3}")

