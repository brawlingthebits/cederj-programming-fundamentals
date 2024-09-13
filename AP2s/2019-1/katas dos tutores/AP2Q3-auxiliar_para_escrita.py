# AP2 - Questão 3 - Programa auxiliar para gerar arquivos de entrada (não precisava ser escrito na avaliação)

import struct

# Escrever registros de alunos
alunos = [
    ('123456789', '156.348.456-12', 'Don Pedro I'),
    ('987654321', '789.654.123-48', 'Maria Joaquina'),
    ('456123789', '123.456.789-99', 'Princesa Isabel')
]

with open('alunos.dat', 'wb') as arq:
    for matricula, cpf, nome in alunos:
        arq.write(matricula[:9].ljust(9, chr(0)).encode('utf-8'))
        arq.write(cpf[:14].ljust(14, chr(0)).encode('utf-8'))
        arq.write(nome[:50].ljust(50, chr(0)).encode('utf-8'))

# Escrever registros de disciplinas
disciplinas = [
    ('EAD-05.009', 'Fundamentos de Programacao', 4),
    ('EAD-05.005', 'Projeto e Desenvolvimento de Algoritmos', 4)
]

with open('disciplinas.dat', 'wb') as arq:
    for codigo, nome, creditos in disciplinas:
        arq.write(codigo[:10].ljust(10, chr(0)).encode('utf-8'))
        arq.write(nome[:50].ljust(50, chr(0)).encode('utf-8'))
        arq.write(struct.pack('=i', creditos))
