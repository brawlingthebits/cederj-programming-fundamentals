# AP2 - Questão 3

import struct

# Subprogramas
def ler_alunos(nome_arquivo):
    registros = dict()
    with open(nome_arquivo, 'rb') as arq:
        arq.seek(0, 2)
        num_registros = arq.tell() // (9 + 14 + 50)
        arq.seek(0)
        for _ in range(num_registros):
            matricula = arq.read(9).decode('utf-8')
            cpf = arq.read(14).decode('utf-8')
            nome = arq.read(50).decode('utf-8').rstrip(chr(0))
            registros[matricula] = (matricula, cpf, nome)
    return registros


def ler_disciplinas(nome_arquivo):
    registros = dict()
    with open(nome_arquivo, 'rb') as arq:
        arq.seek(0, 2)
        num_registros = arq.tell() // (10 + 50 + 4)
        arq.seek(0)
        for _ in range(num_registros):
            codigo = arq.read(10).decode('utf-8')
            nome = arq.read(50).decode('utf-8').rstrip(chr(0))
            creditos = struct.unpack('=i', arq.read(4))[0]
            registros[codigo] = (codigo, nome, creditos)
    return registros


def substituit_media(nome_arquivo, matricula_procurada, codigo_procurado, nova_media):
    with open(nome_arquivo, 'a+b') as arq:
        arq.seek(0, 2)
        num_registros = arq.tell() // (10 + 50 + 4)
        arq.seek(0)
        for _ in range(num_registros):
            matricula = arq.read(9).decode('utf-8')
            codigo = arq.read(10).decode('utf-8')
            media = struct.unpack('=f', arq.read(4))[0]
            if matricula == matricula_procurada and codigo == codigo_procurado:
                arq.seek(-(10 + 50 + 4), 1)
                break
        arq.write(matricula_procurada.encode('utf-8'))
        arq.write(codigo_procurado.encode('utf-8'))
        arq.write(struct.pack('=f', nova_media))


def ler_matricula(registros):
    r = input('Informe a matricula do aluno ("fim" para sair): ')
    while r not in registros and r != 'fim':
        r = input('Matrícula inválida. Informe a matricula do aluno ("fim" para sair): ')
    return r


def ler_codigo(registros):
    r = input('Informe o código da disciplina: ')
    while r not in registros:
        r = input('Código inválido. Informe o código da disciplina: ')
    return r


# Programa Principal
alunos = ler_alunos(input('Favor informar o nome do arquivo de alunos: '))
disciplinas = ler_disciplinas(input('Favor informar o nome do arquivo de disciplinas: '))

print(alunos)
print(disciplinas)

matricula_atualizacao = ler_matricula(alunos)
while matricula_atualizacao != 'fim':
    codigo_atualizacao = ler_codigo(disciplinas)
    media_atualizacao = float(input('Informe a nova média final: '))
    substituit_media('medias.dat', matricula_atualizacao, codigo_atualizacao, media_atualizacao)
    matricula_atualizacao = ler_matricula(alunos)
