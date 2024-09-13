def pot(b, exp):
    if exp == 0:
        return 1
    else:
        return b * pot(b, exp - 1)

def teste(numero):
    try:
        int(numero)
        return True
    except ValueError:
        return False


base = input()
potencia = input()

if teste(base) and teste(potencia):
    result = pot(int(base), int(potencia))
    print(f"{base} elevado a {potencia} é igual a {result}")
elif teste(base) is False and teste(potencia) is False:
    print(f"Base {base} e expoente {potencia} não estão no formato devido")
elif teste(base) is False:
    print(f"Base {base} não está no formato devido")
else:
    print(f"Expoente {potencia} não está no formato devido")
