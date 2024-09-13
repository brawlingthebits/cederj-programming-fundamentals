# Programa Completo - AP3.Q1
# Subprogramas
def mostra(nm):
    print("Conteúdo do Arquivo de Apostas %s:"%nm)
    dados = open(nm, "r")
    for aposta in dados:
        print(aposta.strip("\n"))
    dados.close()
    print()
    return None


def apura(nm, res):
    dicionarioDeQuantidadeDeAcertos = {6:0, 5:0, 4:0, 3:0}
    dados = open(nm, "r")
    for aposta in dados:
        numsAposta = list(map(int, aposta.split()))
        qtdAcertosDaAposta = 0
        for num in numsAposta:
            if num in res:
                qtdAcertosDaAposta += 1
        if 3 <= qtdAcertosDaAposta <= 6:
            dicionarioDeQuantidadeDeAcertos[qtdAcertosDaAposta] += 1
    print("Quantidades de Apostas Premiadas:")
    for acertos in range(6,2,-1):
        print("\tCom %d acertos tivemos: %d aposta(s)"%(acertos, dicionarioDeQuantidadeDeAcertos[acertos]))
    print()
    dados.close()
    return None


# Programa Principal
nome = input()
mostra(nome)
resultados = list(map(int, input().split()))
apura(nome, resultados)