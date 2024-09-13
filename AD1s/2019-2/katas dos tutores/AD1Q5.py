# AD 1 - Questão 5


# Subprograma
def desenhar(p, r, h, mask):  # A solução DEVE ser recursiva, conforme definido no enunciado
    m = (p + r) / 2
    if h > 0:
        desenhar(p, m, h - 1, mask)
        print(mask % m, '-' * h)
        desenhar(m, r, h - 1, mask)


# Programa Principal
n = int(input())
desenhar(0, 2 ** n, n, '%0' + str(len(str(2 ** n - 1))) + 'd')  # A formatação não é trivial. Portanto, o formato incorreto dos números não foi descontado.
