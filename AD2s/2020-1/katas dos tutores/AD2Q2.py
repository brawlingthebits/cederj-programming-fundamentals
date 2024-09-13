# AD2 - Questão 2


# Subprogramas
def acimaPercentual(rn,dn):
    conta = 0
    for i in range(len(rn)):
        if rn[i] == dn[i]:
            conta += 1
    return conta/len(rn) > 50/100


def analisa(rnaVirus, cpfsDnas):
    dadosCpfDna = open(cpfsDnas, "r")
    for linha in dadosCpfDna:
        cpf, dna = linha.strip().split("#")
        if acimaPercentual(rnaVirus, dna):
            print(cpf)
    dadosCpfDna.close()


def cruza(nmVirusRna, nmCpfDna):
    dadosVirus = open(nmVirusRna,"r")
    for linha in dadosVirus:
        virus, rna = linha.strip().split("#")
        print(virus)
        print("Listagem dos possíveis infectados:")
        analisa(rna, nmCpfDna)
        print()
    dadosVirus.close()


# Programa Principal
nomeArqVirusRna, nomeArqCpfDna = input().split()
cruza(nomeArqVirusRna, nomeArqCpfDna)
