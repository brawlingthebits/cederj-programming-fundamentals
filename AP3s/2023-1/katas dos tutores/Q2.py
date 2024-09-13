def remocao(frase):
    saidaespaco = frase.replace(' ', '')
    return saidaespaco

def qtdvogais(frase):
    qtd_v = 0
    i = 0
    while i < len(frase):
        if frase[i] in ["a","ã","á","â","à","e","ê","é","i","í","o","ô","ó","õ","u","ú"]:
            qtd_v += 1
        i += 1
    return qtd_v

def palindrome(frase):
    if len(frase) < 2:
        return True
    else:
        return frase[0] == frase[len(frase) - 1] and palindrome(frase[2:len(frase) - 2])

frase = input()
semespaco = remocao(frase)
print(f"A frase sem espaços é {semespaco}")

vogais = qtdvogais(semespaco)
print(f"A quantidade de vogais de '{frase}' é {vogais} e a quantidade de consoantes é {len(semespaco) - vogais}")

saida = palindrome(semespaco)
if saida is True:
    print(f"{semespaco} é palíndroma")
else:
    print(f"{semespaco} não é palíndroma")
