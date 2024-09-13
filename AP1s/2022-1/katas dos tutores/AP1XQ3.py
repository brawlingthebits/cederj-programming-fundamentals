def verifica_entrada(entrada):
    valores = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    for i in range(0, len(entrada)):
        if entrada[i] not in valores:
            return i
    pontos = entrada.count('.')
    if pontos == 0 or pontos == 1:
        return -1
    else:
        return -2

def converte_numero(entrada):
    eh_numero = verifica_entrada(entrada)
    if eh_numero >= 0:
        print(f'você digitou errado, {entrada} não é do tipo float.')
        print(f'Na posição {eh_numero+1} há o caracter {entrada[eh_numero]}.')
        return 0
    elif eh_numero == -2:
        print('Há mais do que um ".".')
        return 0
    else:
        numero = float(entrada)
        return numero


def conversor(real, taxa):
    valor = real*taxa
    valor = float('%.3f' % valor)
    return valor


def desconto(valor):
    a_vista = valor - valor*.15
    a_vista = float('%.3f' % a_vista)
    return a_vista


def juros(valor, tempo):
    if tempo == 1:
        preco = desconto(valor)
        print(f'Você ganhou 15% de desconto, portanto, de {valor} BRL, você vai pagar {preco} BRL.')
    else:
        preco = valor
        for i in range(2, tempo):
            preco = 1.05*preco
        preco = float('%.2f' % preco)
        preco_final = preco/tempo
        preco_final = float('%.2f' % preco_final)
        print(f'Pagando em {tempo} parcelas, e com 5% de juros ao mês, você pagará {preco_final} BRL por mês, sendo o total de {preco} BRL.')
    return preco



def main():
    real = input()
    taxa = float(input())

    verifica_entrada(real)
    numero = converte_numero(real)

    if numero != 0:
        convertido = conversor(numero, taxa)

        print(f'O valor {numero} USD com a taxa {taxa} vai para {convertido} BRL')
        print(f'Em quantas vezes você quer comprar o produto?')
        tempo = int(input())
        juros(convertido, tempo)

main()

