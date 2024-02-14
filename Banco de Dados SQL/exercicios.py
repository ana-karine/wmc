import sqlite3

conexao = sqlite3.connect('banco_wmc')
cursor = conexao.cursor()


'''
1. Crie uma tabela chamada "alunos" com os seguintes campos: id
(inteiro), nome (texto), idade (inteiro) e curso (texto).
'''

cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')


conexao.commit()
conexao.close