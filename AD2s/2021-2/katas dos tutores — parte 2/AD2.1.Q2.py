# AD2.1 - Questão 2
# Subprogramas
def mostra(nm, msg):
    print("Conteúdo do arquivo", msg, nm + ":")
    dados = open(nm, "r", encoding="utf-8")
    for linha in dados:
        print(linha.strip("\n"))
    dados.close()
    print()
    return None


def remover(ps, lin):
    for p in ps:
        lin = lin.replace(p, "")
    lin = lin.replace("  ", " ").strip()
    return lin + "\n"


def eliminaPalavras(pals, nm):
    dados = open(nm, "r", encoding="utf-8")
    temporario = open(nm + "temp", "w", encoding="utf-8")
    for linha in dados:
        linhaMudada = remover(pals, linha)
        temporario.write(linhaMudada)
    temporario.close()
    dados.close()
    dados = open(nm, "w", encoding="utf-8")
    temporario = open(nm + "temp", "r", encoding="utf-8")
    for linha in temporario:
        dados.write(linha)
    temporario.close()
    dados.close()
    return None


# Programa Principal
palavrasASeremEliminadas = input().split()
palavrasASeremEliminadas.sort(reverse=True)
nomeArquivo = input()
mostra(nomeArquivo, "antes da eleminação das palavras de")
eliminaPalavras(palavrasASeremEliminadas, nomeArquivo)
mostra(nomeArquivo, "após a eliminação das palavras de")