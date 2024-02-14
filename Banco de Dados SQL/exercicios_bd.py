import sqlite3

conexao = sqlite3.connect('banco_wmc')
cursor = conexao.cursor()


'''
1. Crie uma tabela chamada "alunos" com os seguintes campos: id
(inteiro), nome (texto), idade (inteiro) e curso (texto).
'''
query1 = '''
CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));
'''

#cursor.execute(query1)


'''
2. Insira pelo menos 5 registros de alunos na tabela que você criou no
exercício anterior.
'''
# Lista de registros a serem inseridos
registros = [
    (1, 'Ana Moreira', 30, 'Python'),
    (2, 'Maria Silva', 20, 'JavaScript'),
    (3, 'Lucia Pereira', 18, 'C#'),
    (4, 'Carlos Silva', 45, 'Java'),
    (5, 'Maria Rodrigues', 58, 'R')
]

query2 = '''
INSERT INTO alunos(id, nome, idade, curso) VALUES(?, ?, ?, ?);
'''

#cursor.executemany(query2, registros)
  
'''
3. Consultas Básicas
Escreva consultas SQL para realizar as seguintes tarefas:
a) Selecionar todos os registros da tabela "alunos".
b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
c) Selecionar os alunos do curso de "Engenharia" em ordem
alfabética.
d) Contar o número total de alunos na tabela
'''  

dados_a = cursor.execute('SELECT * FROM alunos;')
print("Selecionar todos os registros da tabela 'alunos'\n")
for dado in dados_a:
    print(dado)

dados_b = cursor.execute('\nSELECT nome, idade FROM alunos WHERE idade > 20;')
print("Selecionar o nome e a idade dos alunos com mais de 20 anos\n")
for dado in dados_b:
    print(dado)

dados_b = cursor.execute('\nSELECT nome, idade FROM alunos WHERE idade > 20;')
print("Selecionar o nome e a idade dos alunos com mais de 20 anos\n")
for dado in dados_b:
    print(dado)

conexao.commit()
conexao.close