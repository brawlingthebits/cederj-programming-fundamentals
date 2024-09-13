# AP2 - Questão 4a - Obs.: Execute o programa para ver o resultado


def funcao1(x, y):
    return y / (x + 1)


def funcao2(x, y):
    z = x + 2
    y = z
    w = y
    return x, y


c, b = 0, 5
c, b = funcao2(c, b)
print(c, b)
print("%1.4f" % funcao1(c, b))