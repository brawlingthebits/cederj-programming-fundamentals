# Programa - AD1.1Q1
# Subprogramas
# Principal
PI = 3.1415
linha = input()
while linha != "":
    numero = int(linha)
    if numero%2 != 0:
        raio = numero
        area = PI*raio**2
        perimetro = 2*PI*raio
        print("Área e Perímetro do Círculo de Raio %d são: %.2f e %.2f"%(raio, area, perimetro))
    else:
        print("Divisores de %d são:"%numero, end="")
        for divisor in range(1, numero+1):
            if numero%divisor == 0:
                print("", divisor, end="")
        print()
    linha = input()

