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

#dados = cursor.execute(query1)


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

dados = cursor.executemany(query2, registros)
  

conexao.commit()
conexao.close