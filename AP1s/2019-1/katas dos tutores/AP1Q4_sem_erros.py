# AP1 - Questão 4 (sem erros - compare com a versão com erros)


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


x = int(input("Informe x, um valor inteiro não negativo: "))
while x < 0:
    x = int(input("Valor inválido. Informe outro valor para x: "))

y = int(input("Informe y, um valor inteiro não negativo: "))
while y < 0:
    y = int(input("Valor inválido. Informe outro valor para y: "))

r = gcd(x, y)
print("O máximo divisor comum de %d e %d é %d." % (x, y, r))
