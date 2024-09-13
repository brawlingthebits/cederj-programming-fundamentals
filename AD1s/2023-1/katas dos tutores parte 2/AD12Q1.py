# Programa AD12.Q1


# Subprograma(s)
def lerPessoa():
    nome, idade, peso, altura = input().split()
    idade = int(idade)
    peso = float(peso)
    altura = float(altura)
    return nome, idade, peso, altura

def escreverCrescentes(c, vPessoas):
    opcoes = ["Nome(s)", "Idade(s)", "Peso(s)", "Altura(s)"]
    print("Dados das Pessoas com %s Maiores Que o Primeiro:"%opcoes[c])
    print(vPessoas[0])
    for posicaoSeguinte in range(1, len(vPessoas)):
        if vPessoas[0][c] < vPessoas[posicaoSeguinte][c]:
            print(vPessoas[posicaoSeguinte])
    return None

# Principal
# Inicialização
qtdPessoas = int(input())
vetorDePessoas = [None]*qtdPessoas
# Processamento
for posicaoPessoa in range(qtdPessoas):
    vetorDePessoas[posicaoPessoa] = lerPessoa()
campo = int(input())
escreverCrescentes(campo, vetorDePessoas)
# Finalização
print("Obrigado por utilizar nosso sistema!!!")
