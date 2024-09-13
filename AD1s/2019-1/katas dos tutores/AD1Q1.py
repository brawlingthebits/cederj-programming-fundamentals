# AD1 - Questão 1


# Programa Principal
total = 0
itensComprados = 0
menorPreco, maiorPreco = None, None

linha = input()
while linha != "":
    quantidade, preco = map(float, linha.split())
    total += quantidade * preco
    itensComprados += 1
    if menorPreco == None:
        menorPreco = preco
        maiorPreco = preco
    elif preco < menorPreco:
        menorPreco = preco
    elif preco > maiorPreco:
        maiorPreco = preco
    linha = input()

if itensComprados == 0:
    print("Nenhum produto foi comprado!!!")
else:
    print("Item de Menor Preço:", "%.2f"%menorPreco)
    print("Item de Maior Preço:", "%.2f"%maiorPreco)
    print("Itens Comprados:", itensComprados)
    print("Total Gasto:", "%.2f"%total)