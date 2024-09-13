# AP2X - Questão 2 - Infectados
# Subprogramas
def produz(nmArq, qualCepa):
    dados = open(nmArq, "r", encoding="utf-8")
    dEstados = dict()
    for linha in dados:
        cpf, cepa, data, cidade, estado = linha.strip().split("#")
        if  cepa == qualCepa:
            dia, mes, ano = data.split("/")
            if dEstados.get(estado)==None:
                dEstados[estado] = {cidade:{(ano,mes):1}}
            else:
                if dEstados[estado].get(cidade)==None:
                    dEstados[estado][cidade] = {(ano,mes):1}
                else:
                    if dEstados[estado][cidade].get((ano,mes))== None:
                        dEstados[estado][cidade][(ano, mes)] = 1
                    else:
                        dEstados[estado][cidade][(ano,mes)] += 1
    dados.close()
    return dEstados

def mostra(dEstados, qualCepa):
    print("Tipo da Cepa:", qualCepa)
    total = 0
    for estado in dEstados:
        print(estado)
        for cidade in dEstados[estado]:
            print("\t", cidade)
            for (ano, mes) in sorted(dEstados[estado][cidade]):
                total += dEstados[estado][cidade][(ano, mes)]
                print("\t\tAno:", ano, "Mês:", "%2s"%str(mes), "Infectados:", dEstados[estado][cidade][(ano,mes)])
    print("\nTotal Geral:", total)
    return None

# Programa Principal
nome = input()
cepa = input()
dicionarioDosEstados = produz(nome, cepa)
mostra(dicionarioDosEstados, cepa)