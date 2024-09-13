# AD1.1.2022.2 - Questão 3

# Subprogramas
def contarVogais(linha):
    total = 0
    for char in linha:
        if char in "AEIOUaeiou":
            total += 1
    return total


def pegaMaisComprida(linha):
    mais = ""
    palavrasNaLinha = linha.split()
    for pal in palavrasNaLinha:
        if len(pal) > len(mais):
            mais = pal
    return mais


def palindrome(palavra):
    for i in range(len(palavra) // 2):
        if palavra[i] != palavra[len(palavra) - 1 - i]:
            return False
    return True


def contarPalindromes(linha):
    total = 0
    palavrasNaLinha = linha.split()
    for pal in palavrasNaLinha:
        if palindrome(pal):
            total += 1
    return total


# Programa Principal
lida = input()
if lida == "":
    print("Nenhuma linha não vazia foi lida!!")
else:
    palMaisComprida = ""
    maisVogais = lida
    qtdMaisVogais = contarVogais(lida)
    comMaisPalindromes = ""
    qtdMaisPalindromes = -1
    while lida != "":
        qtdAtual = contarVogais(lida)
        if qtdAtual > qtdMaisVogais:
            maisVogais = lida
            qtdMaisVogais = qtdAtual
        palMaisCompridaAtual = pegaMaisComprida(lida)
        if len(palMaisCompridaAtual) > len(palMaisComprida):
            palMaisComprida = palMaisCompridaAtual
        qtdMaisPalindromesAtual = contarPalindromes(lida)
        if qtdMaisPalindromesAtual > qtdMaisPalindromes:
            comMaisPalindromes = lida
            qtdMaisPalindromes = qtdMaisPalindromesAtual
        lida = input()
    print("Linha com mais vogais sem acento:", maisVogais)
    print("Quantidade de vogais sem acento:", qtdMaisVogais)
    print()
    print("Palavra de maior comprimento lida:", palMaisComprida)
    print()
    print("Linha com mais Palíndromes:", comMaisPalindromes)
    print("Quantidade de palavras Palíndromes:", qtdMaisPalindromes)
