# AD2 - Questão 3

# Programa Principal
with open("entrada.txt", "r") as arq:
    times = []
    for _ in range(5):
        valores = arq.readline().split()
        n = int(valores[0])
        x = [0] * n
        for i in range(n):
            x[i] = int(valores[i + 1])
        times.append(x)
    
    k = int(arq.readline())

somas = []
for i0 in range(len(times[0])):
    for i1 in range(len(times[1])):
        for i2 in range(len(times[2])):
            for i3 in range(len(times[3])):
                for i4 in range(len(times[4])):
                    somas.append(times[0][i0] + times[1][i1] + times[2][i2] + times[3][i3] + times[4][i4])

for n in range(len(somas) - 1, 0, -1):
    for i in range(n):
        if somas[i] < somas[i + 1]:
            somas[i], somas[i + 1] = somas[i + 1], somas[i]

total = 0
for i in range(k):
    total += somas[i]

print(total)
