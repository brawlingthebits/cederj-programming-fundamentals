# Programa Completo - AD1-1Q1

# Subprogramas
def processa(val):
    print("Trocando", val, "em:")
    if val >= 100:
        notas = val // 100
        if notas == 1:
            print("   1 nota de 100 reais")
        else:
            print("   %d notas de 100 reais"%notas)
        val = val % 100
    if val >= 50:
        print("   1 nota de 50 reais")
        val = val % 50
    if val >= 20:
        notas = val // 20
        if notas == 1:
            print("   1 nota de 20 reais")
        else:
            print("   %d notas de 20 reais"%notas)
        val = val % 20
    if val >= 10:
        print("   1 nota de 10 reais")
        val = val % 10
    if val >= 5:
        print("   1 nota de 5 reais")
        val = val % 5
    if val >= 2:
        notas = val // 2
        if notas == 1:
            print("   1 nota de 2 reais")
        else:
            print("   %d notas de 2 reais"%notas)
        val = val % 2
    if val == 1:
        print("   1 moeda de 1 real")
    print()
    return None


# Principal
linhaLida = input()
while linhaLida != "":
    valor = int(linhaLida)
    processa(valor)
    linhaLida = input()
