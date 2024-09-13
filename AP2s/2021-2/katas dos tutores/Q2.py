# Programa Completo - AP2XQ1
# Subprogramas
def construirECarregarMatriz(nm):
    vals = []
    dados = open(nm, "r")
    for linha in dados:
        numeros = list(map(int, linha.split()))
        vals.append(numeros)
    dados.close()
    return vals

def mostra(vals, texto):
    print(texto)
    for linha in vals:
        for valor in linha:
            print("%4d"%valor, end="")
        print()
    print()
    return None

def ordenaLinhaComMaiorSoma(vals):
    def localizaLinhaMaiorSoma(vs):
        vencedora = None
        totalVencedora = -1
        for i in range(len(vs)):
            soma = 0
            for valor in vs[i]:
                soma += valor
            if soma > totalVencedora:
                totalVencedora = soma
                vencedora = i
        return vencedora
    def ordenar(vs):
        for i in range(len(vs)-1):
            menor = i
            for j in range(i+1, len(vs)):
                if vs[j] < vs[menor]:
                    menor = j
            vs[i], vs[menor] = vs[menor], vs[i]
        return None
    onde = localizaLinhaMaiorSoma(vals)
    ordenaLista = ordenar(vals[onde])
    return None

def salvarMatriz(vals, nm):
    dados = open(nm, "w")
    for linha in vals:
        for valor in linha:
            dados.write("%4d"%valor)
        dados.write("\n")
    dados.close()
    return None

# Programa Principal
nomeArq = input()
valores = construirECarregarMatriz(nomeArq)
mostra(valores, "Conteúdo da Matriz Lida Antes de Ordenar:")
ordenaLinhaComMaiorSoma(valores)
mostra(valores, "Conteúdo da Matriz Após Ordenar Linha de Maior Soma:")
salvarMatriz(valores, nomeArq)