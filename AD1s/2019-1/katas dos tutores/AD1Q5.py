# AD1 - Questão 5


# Inicialização
qtdParesLidos = 0  # inicializa variável
somaX = 0  # inicializa variável
somaY = 0  # inicializa variável
linhaLida = input()  # faz a leitura da primeira linha
x = float(linhaLida.split()[0])
y = float(linhaLida.split()[1])

# Processamento
while x != 0 or y != 0:  # repete até que o ponto 0 0 seja lido
    somaX = somaX + x
    somaY = somaY + y
    qtdParesLidos = qtdParesLidos + 1
    linhaLida = input()  # faz a leitura da próxima linha
    x = float(linhaLida.split()[0])
    y = float(linhaLida.split()[1])

# Finalização
if qtdParesLidos == 0:
    print("Não existem pontos!")
else:
    xCentroide = somaX / qtdParesLidos
    yCentroide = somaY / qtdParesLidos
    print("%3.2f %3.2f" % (xCentroide, yCentroide))