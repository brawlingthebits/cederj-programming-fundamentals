def eh_inteiro(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


def collatz(valor):
	valor = int(valor)
	if valor%2 == 0:
		valor1 = int(valor/2)
	else:
		valor1 = 3*valor +1
	print(f"Aplicando a função de Collatz ao {valor}, temos:", valor1)
	return valor


def seq_collatz(valor):
	print(valor, end= " ")
	while valor > 1:
		if valor%2 == 0:
			valor = int(valor/2)
			if valor == 1:
				print(valor)
			else:
				print(valor, end= " ")
		elif valor%2 == 1:
			valor = 3*valor +1
			if valor == 1:
				print(valor)
			else:
				print(valor, end= " ")
	return valor


def todos_collatz(valor):
	for i in range(3, valor+1):
		seq_collatz(i)
	return


def main():
	print("Entre com o elemento para aplicar a função de Collatz")
	valor = input()
	
	if eh_inteiro(valor) is False:
		print(f"Valor {valor} não é inteiro")
	else:
		valor = int(valor)
		collatz(valor)
		print(f"Além disso, a sequência de Collatz de {valor} é:")
		seq_collatz(valor)
		print(f"A Conjectura de Collatz de 3 até {valor} é verdadeira, pois:")
		todos_collatz(valor)


main()