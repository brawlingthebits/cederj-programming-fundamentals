import struct

def processarArquivo(nomeArquivo,resultadoSorteio):
    print("Conteúdo do Arquivo de Apostas",nomeArquivo+":")

    totalApostas = 0
    acertos = dict()
    for qtdAcertos in range(3, 9):
        acertos[qtdAcertos] = set()

    with open(nomeArquivo, "r") as arquivo:
        for linha in arquivo:
            print(linha, end="")
    
            if(len(linha.split("#"))>1):
                totalApostas = totalApostas + 1
                nomeApostador = linha.split("#")[0]
                numerosJogados = set(map(int, linha.split("#")[1:]))
    
                qtdAcertos = len(resultadoSorteio & numerosJogados)
                if(qtdAcertos >= 3):
                    acertos[qtdAcertos].add(nomeApostador)

    print("---- Fim do Arquivo de Apostas ----\n")
    return totalApostas,acertos

def imprimeResultados(totalAposta, acertos):
    if (totalAposta == 0):
        print("“Nenhuma Aposta!!!")
    else:
        print("Total de Apostas:", totalAposta)

        existeVencedor = False
        for qtdAcertos in range(8, 2, -1):
            if (len(acertos[qtdAcertos]) == 0):
                print("Ninguém Acertou", qtdAcertos, "Números!!!")
            else:
                existeVencedor = True
                print("Foi(ram)", len(acertos[qtdAcertos]), "Ganhador(es) com", qtdAcertos, "Acertos:")
                for nomesGanhador in sorted(acertos[qtdAcertos]):
                    print('\t', nomesGanhador)
        if (existeVencedor == False):
            print("ACUMULOU TUDO")

def main():
    nomeArquivo = input()+".txt"
    resultadoSorteio = set(map(int, input().split()))

    try:
        totalAposta,acertos = processarArquivo(nomeArquivo,resultadoSorteio)
        imprimeResultados(totalAposta,acertos)
    except IOError:
        print('O arquivo não foi encontrado')

main()