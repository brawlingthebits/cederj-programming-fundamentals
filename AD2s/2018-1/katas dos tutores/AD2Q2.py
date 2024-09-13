# AD2 - Questão 2

# Subprogramas


def repetido(pal, m):  # O uso de fatiamento (slicing) transforma essa função em uma linha de código.
    for i in range(m):
        if pal[len(pal) - 1 - m - i] != pal[len(pal) - 1 - i]:
            return False
    return True


def corrigirPalavra(pal):
    for m in range(len(pal) // 2, 0, -1):  # m indica o tamanho da repetição a ser testada. Testar maiores primeiro.
        if repetido(pal, m):
            nova_pal = ""  # O uso de fatiamento (slicing) substitui o for a seguir por uma linha de código.
            for i in range(len(pal) - m):
                nova_pal += pal[i]
            return nova_pal  # Se chegou até aqui é porque encontrou repetição.
    return pal  # Se chegou até aqui é porque não encontrou repetição. Logo, a palavra não muda.


def corrigir_mensagem(msg):
    qtd = 0
    nova_msg = ""
    for palavra in msg.split():
        nova_palavra = corrigirPalavra(palavra)
        if nova_palavra != palavra:
            qtd += 1
        nova_msg += nova_palavra + " "
    return qtd, nova_msg.strip()  # Não houve desconto por presentation error na correção. Logo, o .strip() é opcional.


# Programa principal

with open("mensagens_originais.txt", "r") as entrada:
    with open("mensagens_corrigidas.txt", "w") as saida:
        n = int(entrada.readline())
        for lin in range(n):
            linha = entrada.readline()
            correcoes, nova_linha = corrigir_mensagem(linha)
            saida.write("%d %s\n" % (correcoes, nova_linha))
