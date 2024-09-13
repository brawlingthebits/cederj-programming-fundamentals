# AP1 - Questão 4 (sem erros - compare com a versão com erros)


def fatorial(k):
    if k > 1:
        return fatorial(k - 1) * k
    else:
        return 1


n = int(input("Informe um valor inteiro não negativo: "))
while n < 0:
    n = int(input("Valor inválido. Informe um valor inteiro não negativo: "))

if n % 2 == 0:
    print("O valor %d é par." % n)
else:
    print("O valor %d é ímpar." % n)
    
r = fatorial(n)
print("O fatorial de %d é %d." % (n, r))
