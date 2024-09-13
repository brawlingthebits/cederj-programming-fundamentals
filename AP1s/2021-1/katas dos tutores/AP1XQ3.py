# AP1X - Questão 3 - Valor 3.5
letras = input()

letras_distintas = letras.split()


def generate_all(letras_distintas, tam_atual, palavras_anteriores, acumulado):
    current_words = []
    if tam_atual == len(letras_distintas):
        return acumulado
    for word in palavras_anteriores:
        for letter in letras_distintas:
            current_words.append(word + letter)

    acumulado.extend(current_words)
    return generate_all(letras_distintas, tam_atual + 1, current_words, acumulado)


saida = generate_all(letras_distintas, 0, [''], [])

print(f"\n\nAs palavras do alfabeto {letras} são {saida}")
