# AD1 - Questão 1


# Subprogramas
def contarDigitos(linha):
    total = 0
    for x in linha:
        if x in "0123456789":
            total += 1
    return total


def apenasVogaisSemAcento(linha):
    for x in linha:
        if not x in "aeiou":
            return False
    return True


# Programa Principal
lida = input()
if lida == "":
    print("Nenhuma String Não Vazia Foi Lida!!!")
else:
    primeiraStringMaiorComprimento = lida
    tamanhoPrimeiraStringMaiorComprimento = len(lida)
    ultimaStringComMaisDigitos = None
    quantidadeDigitosStringMaisDigitos = 0
    quantidadeStringsFormadasApenasVogaisMinusculasSemAcento = 0
    while lida != "":
        if len(lida) > tamanhoPrimeiraStringMaiorComprimento:
            primeiraStringMaiorComprimento = lida
            tamanhoPrimeiraStringMaiorComprimento = len(lida)
        contagem = contarDigitos(lida)
        if contagem > 0:
            if quantidadeDigitosStringMaisDigitos <= contagem:
                ultimaStringComMaisDigitos = lida
                quantidadeDigitosStringMaisDigitos = contagem
        if apenasVogaisSemAcento(lida):
            quantidadeStringsFormadasApenasVogaisMinusculasSemAcento += 1
        lida = input()
    print("Primeira de Maior Comprimento:", primeiraStringMaiorComprimento)
    if quantidadeDigitosStringMaisDigitos == 0:
        print("Nenhuma String Contém Dígito!!!")
    else:
        print("Última com Mais Dígitos:", ultimaStringComMaisDigitos)
    print("Quantidade de Strings Apenas Com Vogais Minúsculas:",
          quantidadeStringsFormadasApenasVogaisMinusculasSemAcento)