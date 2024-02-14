import sqlite3

conexao = sqlite3.connect('banco_wmc')
cursor = conexao.cursor()


'''
1. Crie uma tabela chamada "alunos" com os seguintes campos: id
(inteiro), nome (texto), idade (inteiro) e curso (texto).
'''

#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

'''
2. Insira pelo menos 5 registros de alunos na tabela que você criou no
exercício anterior.
'''

# Lista de registros a serem inseridos
registros = [
    (1, 'Ana Moreira', 30, 'Engenharia'),
    (2, 'Maria Silva', 20, 'Medicina'),
    (3, 'Lucia Pereira', 18, 'Engenharia'),
    (4, 'Carlos Silva', 45, 'Direiro'),
    (5, 'Maria Rodrigues', 58, 'Psicologia')
]

query1 = '''
INSERT INTO alunos(id, nome, idade, curso) VALUES(?, ?, ?, ?);
'''

#cursor.executemany(query1, registros)

'''
3. Consultas Básicas
Escreva consultas SQL para realizar as seguintes tarefas:
a) Selecionar todos os registros da tabela "alunos".
b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
c) Selecionar os alunos do curso de "Engenharia" em ordem
alfabética.
d) Contar o número total de alunos na tabela
'''  

'''
dados_a = cursor.execute('SELECT * FROM alunos;')
print("\nSelecionar todos os registros da tabela 'alunos:'\n")
for dado in dados_a:
    print(dado)

dados_b = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20;')
print("\nSelecionar o nome e a idade dos alunos com mais de 20 anos:\n")
for dado in dados_b:
    print(dado)

dados_c = cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome;')
print("\nSelecionar os alunos do curso de 'Engenharia' em ordem alfabética:\n")
for dado in dados_c:
    print(dado)

cursor.execute('SELECT COUNT(*) FROM alunos;')
total_alunos = cursor.fetchone()[0]
print("\nContar o número total de alunos na tabela:\n")
print(total_alunos)
'''

'''
4. Atualização e Remoção
a) Atualize a idade de um aluno específico na tabela.
b) Remova um aluno pelo seu ID.
'''

cursor.execute('UPDATE alunos SET idade=17 WHERE nome="Ana Moreira";')

cursor.execute('DELETE FROM alunos WHERE id=2;')



conexao.commit()
conexao.close