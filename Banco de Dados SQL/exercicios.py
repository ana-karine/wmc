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

cursor.executemany(query1, registros)

conexao.commit()
conexao.close