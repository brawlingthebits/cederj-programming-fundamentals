def verifica(frase):
    dic = {"BRL": "real", "USD": "dolar", "EUR": "euro"}
    frase = frase.split( )

    aux = 0
    for i in range(len(frase)):
        if frase[i] in dic:
            frase[i] = dic[frase[i]]
            aux = 1

    if aux == 1:
        for i in range(len(frase)):
            print(f"{frase[i]}", end=" ")

    else:
        print(f"Não há mudanças a serem feitas na frase.")

seq = input()
verifica(seq)