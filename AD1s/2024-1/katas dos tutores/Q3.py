# Programa AD1Q3
# Subprogramas
def lerNumeros():
    listaLidos = []
    linhaLida = input()
    while linhaLida != "":
        valor = float(linhaLida)
        listaLidos.append(valor)
        linhaLida = input()
    return listaLidos

# Principal
listaNumeros = lerNumeros()
if len(listaNumeros)==0:
    print("Nenhum número foi lido!!!")
else:
    ultimo = listaNumeros[len(listaNumeros)-1]
    print("Relação de Números Maiores que", str(ultimo)+":")
    for numero in listaNumeros:
        if numero > ultimo:
            print(numero)
