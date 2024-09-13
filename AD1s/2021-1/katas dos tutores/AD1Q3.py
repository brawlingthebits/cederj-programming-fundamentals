import random

# Entrada: dimensao da matriz
qtd_lojas = int(input())
qtd_produtos = int(input())

loja = []
for i in range(qtd_lojas):
    loja.append(input())

produto_valMin_valMax = ""
produto = []
valMin = []
valMax = []
for i in range(qtd_produtos):
    produto_valMin_valMax = input()
    caracter = len(produto_valMin_valMax)-1
    while (produto_valMin_valMax[caracter] != ' '):
        caracter -= 1
    valMax.append(produto_valMin_valMax[caracter+1:len(produto_valMin_valMax)])
    final_min = caracter -1
    caracter2 = final_min
    while (produto_valMin_valMax[caracter2] != ' '):
        caracter2 -= 1
    valMin.append(produto_valMin_valMax[caracter2+1:final_min+1])
    final_prod = caracter2 -1
    produto.append(produto_valMin_valMax[0:final_prod+1])

def gera_matriz(dim_linhas, dim_colunas, min, max, loja, produto):
    matriz = []
    for l in range(dim_linhas):
        linha = []
        linha.append(loja[l])
        for c in range(dim_colunas):
            linha.append('%.2f'% random.uniform(int(min[c]), int(max[c])))
        matriz.append(linha)
    produto.insert(0, ' ')
    matriz.insert(0, produto)
    return matriz


def escreve_matriz(matriz, qtd_lojas, qtd_produtos):
    for x in range(qtd_lojas+1):
        for y in range(qtd_produtos+1):
            print(matriz[x][y], end="")
        print()


def menores_precos(matriz,qtd_produtos,qtd_lojas):
    total = 0
    for j in range(1, qtd_produtos+1):
        melhor_preco = matriz[1][j]
        melhor_loja = matriz[1][0]
        for i in range(1, qtd_lojas+1):
            if (float(matriz[i][j]) < float(melhor_preco)):
                melhor_preco= matriz[i][j]
                melhor_loja = matriz[i][0]
        print(matriz[0][j], melhor_loja)
        total = total + float(melhor_preco)
    print()
    print("Valor total: R$ " + str(total))

print()
matriz = gera_matriz(qtd_lojas, qtd_produtos, valMin, valMax, loja, produto)

print("Resultado da pesquisa:")
escreve_matriz(matriz, qtd_lojas, qtd_produtos)

print()
print("Menores preços:")
menores_precos(matriz, qtd_produtos, qtd_lojas)
