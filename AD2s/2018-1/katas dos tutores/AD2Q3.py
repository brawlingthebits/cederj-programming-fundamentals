# AD2 - Questão 3

# Subprogramas


def lerPalavras():
    conjunto = set()
    with open("palavras.txt", "r") as arqPalavras:
        for palavra in arqPalavras:
            conjunto.add(palavra.rstrip())  # O .rstrip é necessário, pois a linha lida inclui um "\n" no final.
    return conjunto


def lerDiscurso():
    texto = str()
    quebraPendente = False
    with open("discurso.txt", "r") as arqDiscurso:
        for linha in arqDiscurso:
            if not quebraPendente:
                texto += " "
            texto += linha.rstrip()

            if texto[len(texto) - 1] == "-":
                texto = texto.rstrip("-")
                quebraPendente = True
            else:
                quebraPendente = False
    return texto


def contarOcorrencias(conjunto, texto):
    contagem = dict()
    for palavra in conjunto:
        contagem[palavra] = 0
    for palavra in texto.split():
        if palavra in palavras:
            contagem[palavra] += 1
    return contagem


# Programa principal

palavras = lerPalavras()
discurso = lerDiscurso()
ocorrencias = contarOcorrencias(palavras, discurso)

with open("contagem.txt", "w") as arqContagem:
    for p, n in ocorrencias.items():
        arqContagem.write("%s %d\n" % (p, n))
