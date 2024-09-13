"""
Q3: Faça um programa que processe eleições com até dez candidatos. Seu programa deve permitir
inicialmente que sejam definidos: a quantidade de candidatos com seus respectivos nomes. Em
seguida, as eleições ficarão abertas até que alguém vote em um candidato inexistente. Seu
programa deve ao final escrever o nome de cada candidato seguido pela sua quantidade de
votos recebidos.
"""


# Subprogramas
def apurar(nomes, votos):
    print("\nResultados:")
    for i in range(len(nomes)):
        print(nomes[i],"com",votos[i],"voto(s)")
    return None


# Programa Principal
print("Definição do Pleito:")
qtdCandidatos = int(input())
if qtdCandidatos < 1 or qtdCandidatos > 10:
    print("Quantidade de Candidatos Inválida!!!")
else:
    candidatos = []
    votosCandidatos = [0] * qtdCandidatos
    for i in range(qtdCandidatos):
        nome = input()
        candidatos.append(nome)

    print("\nVotação:")
    voto = input()
    while voto in candidatos:
        votosCandidatos[candidatos.index(voto)] += 1
        voto = input()

    apurar(candidatos, votosCandidatos)