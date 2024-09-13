# AP1 - Questão 1

somaX = somaY = qtdPontos = 0

x, y = map(float, input().split())
while (x, y) != (0, 0):
    somaX += x
    somaY += y
    qtdPontos += 1
    x, y = map(float, input().split())

if qtdPontos == 0:
    print("Não existem pontos!")
else:
    print("%.2f %.2f" % (somaX / qtdPontos, somaY / qtdPontos))