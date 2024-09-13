# AP2X - Questão 1 - Olimpíadas de Tóquio
# Subprogramas
def produz(nm):
    medsOuro = set()
    medsPrata = set()
    medsBronze = set()
    dados = open(nm, "r", encoding="utf-8")
    for linha in dados:
        pais, tipo, modalidade = linha.split("#")
        if tipo == "ouro":
            medsOuro.add(pais)
        elif tipo == "prata":
            medsPrata.add(pais)
        else:
            medsBronze.add(pais)
    dados.close()
    return medsOuro, medsPrata, medsBronze

def mostrar(msg, conjMeds):
    print(msg)
    for pais in sorted(conjMeds):
        print("\t", pais)
    print()
    return None

# Principal
nomeArq = input()
ouro, prata, bronze = produz(nomeArq)
mostrar("Países com Ouro(s):", ouro)
mostrar("Países com Prata(s):", prata)
mostrar("Países com Bronze(s):", bronze)
paisesComPeloMenosUmaMedalha = ouro.union(prata.union(bronze))
mostrar("Países com pelo menos uma medalha:", paisesComPeloMenosUmaMedalha)
paisesComPeloMenosUmaMedalhaDeCadaTipo = ouro.intersection(prata.intersection(bronze))
mostrar("País(es) com pelo menos uma Medalha de cada Tipo:", paisesComPeloMenosUmaMedalhaDeCadaTipo)