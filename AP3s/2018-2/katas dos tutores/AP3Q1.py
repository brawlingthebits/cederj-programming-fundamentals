# AP3 - Questão 1

m1 = None
m2 = None

n = int(input())
while n >= 0:
    if m1 is None or m1 <= n:
        m2 = m1
        m1 = n
    elif m2 is None or m2 < n:
        m2 = n
    n = int(input())

if m1 is None:
    print("Nenhum valor válido!!!")
elif m2 is None:
    print("Apenas um valor foi lido:", m1)
else:
    print("Os dois maiores números lidos foram:", m1, "e", m2)