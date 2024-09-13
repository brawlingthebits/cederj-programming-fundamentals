# Dizemos que um número inteiro positivo é triangular se ele é o produto de três numeros inteiros consecutivos. Por exemplo, 120 é triangular, pois

# >>> 4 * 5 * 6
#120
#Dado um número inteiro positivo n, verificar se n é triangular.

n = int(input("Digite um número inteiro: "))
d = 1
resultado = d*(d+1)*(d+2)

while resultado < n:
	d = d + 1
	resultado = d * (d + 1) * (d+2)

if resultado == n:
	print(f"{n} é um número triangular, pois pode ser escrito por {d}*{d+1}*{d+2}")

else:
	print(f"{n} não é um número triangular")