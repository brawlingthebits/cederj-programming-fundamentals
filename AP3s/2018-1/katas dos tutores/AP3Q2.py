# AP3 - Questão 2


# Subprogramas
def insereOrdenado(nomeDoArquivo, novoValor):  # Função Solicitada na Questão
    dados = open(nomeDoArquivo, "r")
    dadosAuxiliar = open(nomeDoArquivo + "$$$", "w")
    inseriu = False
    for linha in dados:
        valor = float(linha)
        if not inseriu and novoValor <= valor:
            dadosAuxiliar.write(str(novoValor) + "\n")
            inseriu = True
        dadosAuxiliar.write(linha)
    if not inseriu:
        dadosAuxiliar.write(str(novoValor) + "\n")
    dados.close()
    dadosAuxiliar.close()
    dadosAuxiliar = open(nomeDoArquivo + "$$$", "r")
    dados = open(nomeDoArquivo, "w")
    for linha in dadosAuxiliar:
        dados.write(linha)
    dados.close()
    dadosAuxiliar.close()
    return None


def mostrar(nm):
    dados = open(nm, "r")
    print("------- " + nm + " -------")
    for linha in dados:
        print(linha, end="")
    dados.close()
    return None


# Programa Principal
mostrar("teste.txt")
insereOrdenado("teste.txt", 6.0)
mostrar("teste.txt")