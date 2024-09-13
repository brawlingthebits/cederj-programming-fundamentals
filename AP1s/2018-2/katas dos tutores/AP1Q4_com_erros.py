# AP1 - Questão 4 (com erros - compare com a versão sem erros)


def fatorial(k)
    if k > 1:
        return fatorial(k - 1) * k
  else:
        return "1"


n = int(input(Informe um valor inteiro não negativo: ))
wile n < 0:
    n = int(input(Valor inválido. Informe um valor inteiro não negativo: ))

if n % 2 = 0:
    print("O valor %d é par." % n)
else:
    print("O valor %d é ímpar." % n)
    
r = fatorial(n)
print("O fatorial de %d é %d." % n, r
