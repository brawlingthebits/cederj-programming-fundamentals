def monta_ciclo(pi):
	pi = pi.split(" ")

	flag = []
	for posicao in range(len(pi)):
		flag.append(0)
	
	ciclos = []
	for k in range(len(flag)):
		if int(flag[k]) == 0:
			ciclo = []
			i = k+1
			while int(flag[i-1]) == 0:
				ciclo.append(i)
				flag[i-1] = 1
				
				j = int(pi[i-1])
				i = int(j)
			ciclos.append(ciclo)

	return ciclos

	
pi = input()
print(monta_ciclo(pi))
