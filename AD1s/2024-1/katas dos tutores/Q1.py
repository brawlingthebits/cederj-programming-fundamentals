# Programa AD1Q1
# Subprogramas
# Principal
caracterProcurado= input().upper()
qtdPalavras = 0
linhaLida = input()
while linhaLida != "":
    palavrasNaLinha = linhaLida.upper().split()
    for palavra in palavrasNaLinha:
        if palavra[0] == caracterProcurado or palavra[len(palavra)-1] == caracterProcurado:
            qtdPalavras += 1
            print(palavra)
    linhaLida = input()
print("Quantidade de Palavras Iniciadas ou Finalizada pelo Caracter", caracterProcurado, "=", qtdPalavras, "Vez(es)")