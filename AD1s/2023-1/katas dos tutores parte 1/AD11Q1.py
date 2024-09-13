# Programa AD11.Q1


# Subprograma(s)
def media(soma, qtd):
    return soma / qtd


# Principal
# Inicialização
maiorNumero = menorNumero = None
qtdLidos = somaLidos = 0
linhaLidaDoTeclado = input()
# Processamento
while linhaLidaDoTeclado != "":
    numeroConvertido = int(linhaLidaDoTeclado)
    qtdLidos = qtdLidos + 1
    somaLidos = somaLidos + numeroConvertido
    if qtdLidos == 1:
        maiorNumero = menorNumero = numeroConvertido
    elif numeroConvertido < menorNumero:
        menorNumero = numeroConvertido
    elif numeroConvertido > maiorNumero:
        maiorNumero = numeroConvertido
    linhaLidaDoTeclado = input()
# Finalização
if qtdLidos == 0:
    print("Nenhum número foi lido - A primeira linha lida foi vazia!!!")
else:
    print("Menor: %d, Maior: %d e Média: %.2f" % (menorNumero, maiorNumero, media(somaLidos, qtdLidos)))
