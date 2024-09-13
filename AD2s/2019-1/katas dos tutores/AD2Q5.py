# AD2 - Questão 5


# Programa Principal
naipes = {"P": 1, "O": 2, "C": 3, "E": 4}
simbolos = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13}

cartas = []
with open("cartas.txt", "r") as arq:
    for _ in range(52):
        cartas.append(arq.readline().split())  # O primeiro string é o símbolo e o segundo é o naipe

for n in range(len(cartas) - 1, 0, -1):
    for i in range(n):
        if naipes[cartas[i][1]] > naipes[cartas[i + 1][1]] or (naipes[cartas[i][1]] == naipes[cartas[i + 1][1]] and simbolos[cartas[i][0]] > simbolos[cartas[i + 1][0]]):
            cartas[i], cartas[i + 1] = cartas[i + 1], cartas[i]


with open("cartas_ordenadas.txt", "w") as arq:
    for carta in cartas:
        arq.write(carta[0] + " " + carta[1] + "\n")
