# Programa Completo da AD21 - Questão 2 - 2022.1
# Subprogramas
def mostrar(nm, msg):
    print(msg)
    dados = open(nm, "r")
    for linha in dados:
        print("\t", linha.strip())
    dados.close()
    print()
    return None

def distancia(xA,yA,xB,yB):
    return ((xB-xA)**2+(yB-yA)**2)**0.5

def naoPertence(x, y, nmC):
    dados = open(nmC, "r")
    for linha in dados:
        xC,yC,rC = map(int, linha.split())
        if distancia(x,y,xC,yC) < rC:
            dados.close()
            return False
    dados.close()
    return True

def remover(nmPts, nmCircs):
    from os import rename, remove
    dadosPontos = open(nmPts, "r")
    temporario = open(nmPts+"temp", "w")
    for linha in dadosPontos:
        xAtual, yAtual = map(int, linha.split())
        if naoPertence(xAtual,yAtual, nmCircs):
            temporario.write(linha)
    dadosPontos.close()
    temporario.close()
    remove(nmPts)
    rename(nmPts+"temp", nmPts)
    return None

# Principal
nomeArqPontos = input()
nomeArqCirculos = input()
mostrar(nomeArqPontos, "Conteúdo do Arquivo %s:"%nomeArqPontos)
mostrar(nomeArqCirculos, "Conteúdo do Arquivo %s:"%nomeArqCirculos)
remover(nomeArqPontos, nomeArqCirculos)
mostrar(nomeArqPontos, "Conteúdo do Arquivo %s após eventuais remoções:"%nomeArqPontos)
