"""
Q2: Leia strings do teclado até que uma string vazia seja lida. Escreva no vídeo:
(a) a quantidade de vogais lidas;
(b) a quantidade de dígitos lidos;
(c) qual foi a string de maior comprimento lida. Caso haja empate, escreva uma delas;
(d) a quantidade de strings palíndromes lidas.
"""


# Subprogramas
def contarOcorrencias(caracteres, palavra):
    total = 0
    for c in palavra:
        if c.upper() in caracteres:
            total += 1
    return total


def palindrome(palavra):
    for i in range(len(palavra) // 2):
        if palavra[i] != palavra[len(palavra) - i - 1]:
            return False
    return True


# Programa Principal
digitos = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
vogais = {'A', 'E', 'I', 'O', "U"}

qtdVogais = 0
qtdDigitos = 0
qtdPalindromes = 0
stringMaisComprida = ""

lida = input()

while lida != "":
    qtdVogais += contarOcorrencias(vogais, lida)
    qtdDigitos += contarOcorrencias(digitos, lida)
    if len(lida) > len(stringMaisComprida):
        stringMaisComprida = lida
    if palindrome(lida):
        qtdPalindromes += 1
    lida = input()

print("Quantidade de Vogais:", qtdVogais)
print("Quantidade de Dígitos:", qtdDigitos)
print("Maior String lida:", stringMaisComprida)
print("Quantidade de Palíndromes:", qtdPalindromes)