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


def diferenca(permutacao):
    inv = inverter(permutacao)
    inv = inv.split()
    permutacao = permutacao.split()
    dif = []
    for i in range(len(permutacao)):
        subtracao = int(permutacao[i]) - int(inv[i])
        dif.append(subtracao)
    return dif


saida = repeticoes(permut)
saida2, qtd = inversao(permut)
saida3 = inverter(permut)
saida4 = diferenca(permut)

print(f"Os elementos que se repetem são: {saida}")
print(f"Há {qtd} inversões, e as posições são: {saida2}")
print(f"Sequência inversa: {saida3}")
print(f"A sequência obtida da diferença é: {saida4}")

