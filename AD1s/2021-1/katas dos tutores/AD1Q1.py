import math

# pi com 3 casas decimais
PI = float('%.3f' % math.pi)


def computar_comprimeto_roda(dimatro):
    return PI * dimatro


def computar_numero_de_voltas(distancia, comprimento):
    distancia_cm = distancia * 100000

    return distancia_cm / comprimento


def computar_ordem_de_grandeza(nvoltas):
    ordem = 0
    base = nvoltas

    while base < 0.316:
        ordem -= 1
        base *= 10.0
    while base > 3.16:
        ordem += 1
        base /= 10.0

    return ordem


def obter_entrada():
    distancia = converte_string_para_float(input())
    diametro = converte_string_para_float(input())

    return distancia, diametro


def converte_string_para_float(valor):
    # Remove o separador de milhares '.' e subsitui o separador de decimal ',' por '.'
    valor_formatado = valor.replace('.', '').replace(',', '.')

    return float(valor_formatado)


def formatar_saida(valor):
    valor_int = int(valor)

    # Verifica se o valor é um inteiro, se sim, converte
    if valor == valor_int:
        valor = valor_int

    # #Usa '.' como separador de milhares
    valor_formatado = f"{valor:_}".replace('.', ',').replace('_', '.')

    return valor_formatado


def imprimir_saida(distancia, diametro, ordem):
    distancia_formatada = formatar_saida(distancia)
    diametro_formatado = formatar_saida(diametro)

    print(f"\nDistância percorrida: {distancia_formatada} km")
    print(f"Diâmetro da roda: {diametro_formatado} cm")
    print(f"Ordem de grandeza da quantidade de voltas efetuadas: 10 elevado a {ordem}")


def main():
    distancia, diametro = obter_entrada()
    comprimento = computar_comprimeto_roda(diametro)
    nvoltas = computar_numero_de_voltas(distancia, comprimento)
    ordem = computar_ordem_de_grandeza(nvoltas)
    imprimir_saida(distancia, diametro, ordem)


main()