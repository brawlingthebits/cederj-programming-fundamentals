"""
Q4: Faça um programa que processe matrizes de números de ponto flutuante com dimensões
definidas pelo usuário e com valores gerados aleatoriamente num intervalo também definido
pelo usuário. Escreva na saída padrão:
(a) A matriz gerada aleatoriamente;
(b) Qual é o maior valor contido na matriz e sua respectiva posição, linha e coluna. Casa haja
    empate, escreva um deles;
(c) Qual é o produto dos maiores valores de cada uma das linhas;
(d) Qual é a soma dos menores valores de cada uma das linhas;
(e) Qual a linha de maior intervalo entre seu menor valor e seu maior valor.
"""


# Subprogramas

def gerar(qLins, qCols, valMin, valMax):
    from random import uniform
    resp = []
    for lin in range(qLins):
        linhaValores = []
        for col in range(qCols):
            aleatorio = uniform(valMin, valMax)
            linhaValores.append(aleatorio)
        resp.append(linhaValores)
    return resp


def mostrar(vals):
    print("Matriz:")
    for linha in vals:
        for valor in linha:
            print(valor, end=" ")
        print()
    print()
    return None


def localizaCelulaComMenorValor(vals):
    resp = (0, 0)
    for lin in range(len(vals)):
        for col in range(len(vals[lin])):
            if vals[lin][col] > vals[resp[0]][resp[1]]:
                resp = (lin, col)
    return resp


def mostraMaiorProdutoEntreLinhas(vals):
    def maior(valsLinha):
        if len(valsLinha) == 0:
            return 0
        else:
            max = valsLinha[0]
            for valor in valsLinha:
                if valor > max:
                    max = valor
            return max

    produto = 1
    for lin in range(len(vals)):
        produto *= maior(vals[lin])
    print("O maior produto é:", produto)
    return None


def mostraMenorSomaEntreLinhas(vals):
    def menor(valsLinha):
        if len(valsLinha) == 0:
            return 0
        else:
            min = valsLinha[0]
            for valor in valsLinha:
                if valor < min:
                    min = valor
            return min

    soma = 0
    for lin in range(len(vals)):
        soma += menor(vals[lin])
    print("A menor soma é:", soma)
    return None


def mostraLinhaComMaiorIntervalo(vals):
    def pegaFaixa(valoresNaLinha):
        if len(valoresNaLinha) == 0:
            return 0
        else:
            minimo = maximo = valoresNaLinha[0]
            for i in range(1, len(valoresNaLinha)):
                if valoresNaLinha[i] < minimo:
                    minimo = valoresNaLinha[i]
                elif valoresNaLinha[i] > maximo:
                    maximo = valoresNaLinha[i]
            return maximo - minimo

    if len(vals) > 0:
        linha = 0
        maiorIntervalo = pegaFaixa(vals[0])
        for lin in range(1, len(vals)):
            atual = pegaFaixa(vals[lin])
            if atual > maiorIntervalo:
                linha = lin
                maiorIntervalo = atual
        print("A linha:", linha, "possui o maior intervalo entre valores:", maiorIntervalo)
    return None


# Programa Principal

print("Dimensões da Matriz:")
dimensoes = input().split()
qtdLinhas = int(dimensoes[0])
qtdColunas = int(dimensoes[1])

print("Intervalo de Valores:")
faixaDeValores = input().split()
minimo = float(faixaDeValores[0])
maximo = float(faixaDeValores[1])

valores = gerar(qtdLinhas, qtdColunas, minimo, maximo)
mostrar(valores)

ondeMenor = localizaCelulaComMenorValor(valores)
print("Linha:", ondeMenor[0], "Coluna:", ondeMenor[1], \
      "contém o maior valor:", valores[ondeMenor[0]][ondeMenor[1]])

mostraMaiorProdutoEntreLinhas(valores)
mostraMenorSomaEntreLinhas(valores)
mostraLinhaComMaiorIntervalo(valores)