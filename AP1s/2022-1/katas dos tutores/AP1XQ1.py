# AP1X - Q1
# Subprograma
def processaEMostraExtremos(linNums):
    nums = linNums.split()
    for i in range(len(nums)):
        nums[i] = float(nums[i])
    somaNumsLin = 0
    menor = maior = nums[0]
    for valor in nums:
        somaNumsLin += valor
        if valor < menor:
            menor = valor
        elif valor > maior:
            maior = valor
    print("Menor:", menor, "Maior:", maior)
    return len(nums), somaNumsLin

# Programa Principal
qtdNumeros = 0
somaNumeros = 0
linha = input()
while linha != "":
    qtdNumerosNaLinha, somaNumerosNaLinha = processaEMostraExtremos(linha)
    qtdNumeros += qtdNumerosNaLinha
    somaNumeros += somaNumerosNaLinha
    linha = input()
print("Quantidade de Números Lidos:", qtdNumeros)
if qtdNumeros == 0:
    print("Nenhum Número Foi Lido. Portanto, não existe média!!!")
else:
    print("Média dos Números Lidos: %.2f"%(somaNumeros/qtdNumeros))
