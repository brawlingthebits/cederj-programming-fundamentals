# AD1.1.2022.2 - Questão 1

# Programa Principal
lida = input()
if lida == "":
    print("Nenhuma linha lida com conteúdo, portanto não há soma nem média!!")
else:
    soma = 0
    qtd = 0
    while lida != "":
        soma += float(lida)
        qtd += 1
        lida = input()
    print("Soma dos Números: %.2f"%soma)
    print("Média dos Números: %.2f"%(soma/qtd))
