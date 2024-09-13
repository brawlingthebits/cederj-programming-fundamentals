# Programa AD21Q1 - 2023.2
# Subprogramas
def leituraDeMatriz():
    valores = []
    linhaLida = input()
    while linhaLida != "":
        numeros = list(map(int, linhaLida.split()))
        valores.append(numeros)
        linhaLida = input()
    return valores

def somaMatrizes(valsAlfa, valsBeta):
    if valsAlfa == [] or valsBeta == [] or \
            len(valsAlfa) != len(valsBeta) or \
            len(valsAlfa[0]) != len(valsBeta[0]):
        valores = None
    else:
        valores = []
        for lin in range(len(valsAlfa)):
            numeros = [0]*len(valsAlfa[0])
            for col in range(len(valsAlfa[0])):
                numeros[col] +=  valsAlfa[lin][col]+valsBeta[lin][col]
            valores.append(numeros)
    return valores

def multiplicaMatrizes(valsAlfa, valsBeta):
    if valsAlfa == [] or valsBeta == [] or \
       len(valsAlfa[0])!=len(valsBeta):
        valores = None
    else:
        valores = []
        for lin in range(len(valsAlfa)):
            numeros = [0]*len(valsBeta[0])
            for col in range(len(valsBeta[0])):
                for varre in range(len(valsBeta)):
                    numeros[col] += valsAlfa[lin][varre]*valsBeta[varre][col]
            valores.append(numeros)
    return valores

def mostraMatriz(texto, valores):
    print(texto+":")
    if valores == None:
        print("Inexistente!!!")
    else:
        for lin in range(len(valores)):
            for col in range(len(valores[0])):
                print("%5d"%valores[lin][col], end="")
            print()
    return None

# Principal
valoresA = leituraDeMatriz()
valoresB = leituraDeMatriz()
mostraMatriz("Matriz A", valoresA)
mostraMatriz("Matriz B", valoresB)
valoresSoma = somaMatrizes(valoresA, valoresB)
valoresMult = multiplicaMatrizes(valoresA, valoresB)
mostraMatriz("Matriz Soma de A com B", valoresSoma)
mostraMatriz("Matriz Multiplicação de A por B", valoresMult)
