# AP3 - Questão 1


# Subprograma
def ordenaPorCampo(qualCampo, vetorDeProdutos): # Função Solicitada na Questão
    for i in range(len(vetorDeProdutos)):
        ondeMenor = i
        for j in range(i+1,len(vetorDeProdutos)):
            if vetorDeProdutos[j][qualCampo] < vetorDeProdutos[ondeMenor][qualCampo]:
                ondeMenor = j
        temp = vetorDeProdutos[i]
        vetorDeProdutos[i] = vetorDeProdutos[ondeMenor]
        vetorDeProdutos[ondeMenor] = temp
    return None


# Programa Principal
lista = [["xy3", "arroz", 120, 5.25], ["aa9", "feijão", 555, 2.99], ["ab8","banana", 100, 3.99]]
print("Antes das ordenações:\n",lista)
for campo in range(1,5):
    ordenaPorCampo(campo-1, lista)
    print("Ordenado pelo Campo:",campo,"\n", lista)