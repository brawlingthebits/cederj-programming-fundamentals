# AP3 - Questão 2


# Subprograma
def eh_primo(num, i=2):
    if num <= 2:
        return n == 2
    elif num % i  == 0:
        return False
    elif i * i > num:  # Condicão opcional. Apenas um truque para reduzir o processamento.
        return True
    else:
        return eh_primo(num, i + 1)


# Programa Principal
n = int(input())
if eh_primo(n):
    print("O número informado é primo")
else:
    print("O número informado não é primo")