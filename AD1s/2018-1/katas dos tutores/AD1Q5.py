"""
Q5: Faça um programa, contendo subprogramas, que leia pares de valores inteiros, x e y, até que o
par de números zeros seja lido. Suponha que cada um destes pares representem um ponto no
espaço bidimensional. Mantenha estes pontos como um vetor de tuplas (x,y). Após a entrada
de todos pontos válidos, excetuando o par de zeros, escreva na saída padrão:
(a) A quantidade de pontos válidos;
(b) O vetor de pontos, escrevendo um ponto por linha;
(c) Caso existam, quais os dois pontos mais próximos entre si. Caso haja empate, escreva um
deles;
(d) Caso existam, quais os dois pontos mais distantes entre si. Caso haja empate, escreva um
deles;
(e) Caso existam, quais são as médias das coordenadas x e y.

Definição: A distância entre dois pontos (xA,yA) e (xB,yB) é dada pela raiz quadrada da soma do quadrado
das diferenças, (xA-xB) e (yA-yB).
"""


# Subprogramas
def mostrar(pares):
    if len(pares) == 0:
        print("Nenhum Ponto Válido!!!")
    else:
        print("Pontos Válidos:")
        for p in pares:
            print(p)
        return None


def distancia(pA, pB):
    return pow(pow(pA[0] - pB[0], 2) + pow(pA[1] - pB[1], 2), 0.5)


def paresMaisDistantes(pares):
    if len(pares) < 2:
        print("Mais Distantes: Não existem pelo menos dois pontos!!")
    else:
        p1 = pares[0]
        p2 = pares[1]
        maiorDistancia = distancia(p1, p2)

        for i in range(len(pares)):
            for j in range(i + 1, len(pares)):
                distAtual = distancia(pares[i], pares[j])
                if distAtual > maiorDistancia:
                    p1 = pares[i]
                    p2 = pares[j]
                    maiorDistancia = distAtual

        print("Pontos mais distantes entre si:", p1, "e", p2, "com distância:", maiorDistancia)
    return None


def paresMaisProximos(pares):
    if len(pares) < 2:
        print("Mais Próximos: Não existem pelo menos dois pontos!!")
    else:
        p1 = pares[0]
        p2 = pares[1]
        menorDistancia = distancia(p1, p2)

        for i in range(len(pares)):
            for j in range(i + 1, len(pares)):
                distAtual = distancia(pares[i], pares[j])
                if distAtual < menorDistancia:
                    p1 = pares[i]
                    p2 = pares[j]
                    menorDistancia = distAtual

        print("Pontos mais próximos entre si:", p1, "e", p2, "com distância:", menorDistancia)
    return None


def mostraMedia(pares):
    if len(pares) == 0:
        print("Não existe média!!!")
    else:
        somaX = 0
        somaY = 0
        qtd = 0
        for (x, y) in pares:
            somaX += x
            somaY += y
            qtd += 1
        print("Média dos X's:", somaX / qtd, "Média dos Y's:", somaY / qtd)
        return None


# Programa Principal
paresLidos = []
par = input().split()
x = int(par[0])
y = int(par[1])

while x != 0 or y != 0:
    paresLidos.append((x, y))
    par = input().split()
    x = int(par[0])
    y = int(par[1])

print("A Quantidade de Ponto(s) Válido(s):", len(paresLidos))
mostrar(paresLidos)
paresMaisProximos(paresLidos)
paresMaisDistantes(paresLidos)
mostraMedia(paresLidos)