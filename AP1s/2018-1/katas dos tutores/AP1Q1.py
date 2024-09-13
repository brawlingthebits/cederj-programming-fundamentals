# AP1 - Questão 1 - Obs.: Este é um programa de referência. Existem outras formas de se resolver o problema.

a = int(input())

while a != 0:
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
        print("O ano %d é bissexto" % a)
    else:
        print("O ano %d não é bissexto" % a)

    a = int(input())
