x = int(input("Digite um número inteiro: "))
y = int(input("Digite outro número inteiro: "))

if x < y:
	menor = x
	maior = y
	while y % x != 0:
		a = x
		x = y % x
		y = a
		print(y, x)
	print("O MDC entre ", menor, " e ", maior, " é ", x)
	print("O MMMC entre ", menor, " e ", maior, " é ", (menor*maior)/x) 

else:
	menor = y
	maior = x
	while x % y != 0:
		a = y
		y = x % y
		x = a
		print(x, y)
	print("O MDC entre ", menor, " e ", maior, " é ", y)
	print("O MMMC entre ", menor, " e ", maior, " é ", (menor*maior)/y) 
