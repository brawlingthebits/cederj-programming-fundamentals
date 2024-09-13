# AD2 - Questão 5


# Subprogramas
def insereOrdenado(nomeDoArquivo, novoValor):  # Função solicitada na questão
    dados = open(nomeDoArquivo, 'r')
    dadosAuxiliar = open(nomeDoArquivo + '$$$', 'w')
    inseriu = False
    for linha in dados:
        valor = float(linha)
        if not inseriu and novoValor <= valor:
            dadosAuxiliar.write(str(novoValor) + '\n')
            inseriu = True
        dadosAuxiliar.write(linha)
    if not inseriu:
        dadosAuxiliar.write(str(novoValor) + '\n')
    dados.close()
    dadosAuxiliar.close()
    dadosAuxiliar = open(nomeDoArquivo + '$$$', 'r')
    dados = open(nomeDoArquivo, 'w')
    for linha in dadosAuxiliar:
        dados.write(linha)
    dados.close()
    dadosAuxiliar.close()


def mostrar(nm):
    with open(nm, 'r') as dados:
        print('------- ' + nm + ' -------')
        for linha in dados:
            print(linha, end='')


# Programa Principal
mostrar('teste.txt')
insereOrdenado('teste.txt', 6.0)
mostrar('teste.txt')
