# AP1X - Q1
# Subprograma
def dentro(xP, yP, xC, yC, r):
    return ((xC-xP)**2+(yC-yP)**2)**0.5 <= r

# Programa Principal
xCentro, yCentro, raio = input().split()
xCentro, yCentro, raio = int(xCentro), int(yCentro), int(raio)
qtdPontos = qtdPontosDentro = 0
linha = input()
while linha != "":
    qtdPontos += 1
    xPonto, yPonto = linha.split()
    xPonto, yPonto = int(xPonto), int(yPonto)
    if dentro(xPonto,yPonto,xCentro,yCentro,raio):
        qtdPontosDentro += 1
        print((xPonto, yPonto), "está dentro do círculo", (xCentro, yCentro, raio))
    linha = input()
print("Quantidade de Pontos Processados:", qtdPontos)
print("Quantidade de Pontos Dentro de Círculo:", qtdPontosDentro)
if qtdPontos == 0:
    percentual = 0
else:
    percentual = (100*qtdPontosDentro/qtdPontos)
print("Percentual de Pontos Dentro do Círculo: %.1f"%percentual,"%")