import sqlite3

conexao = sqlite3.connect('banco_wmc')
cursor = conexao.cursor()


'''
1. Crie uma tabela chamada "alunos" com os seguintes campos: id
(inteiro), nome (texto), idade (inteiro) e curso (texto).
'''

cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')


'''
2. Insira pelo menos 5 registros de alunos na tabela que você criou no
exercício anterior.
'''

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


'''
3. Consultas Básicas
Escreva consultas SQL para realizar as seguintes tarefas:
a) Selecionar todos os registros da tabela "alunos".
b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
d) Contar o número total de alunos na tabela.
'''  

# a) Selecionar todos os registros da tabela "alunos".
dados_a = cursor.execute('SELECT * FROM alunos;')
for dado in dados_a:
    print(dado)

# b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
dados_b = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20;')
for dado in dados_b:
    print(dado)

# c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
dados_c = cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome;')
for dado in dados_c:
    print(dado)

# d) Contar o número total de alunos na tabela.
cursor.execute('SELECT COUNT(*) FROM alunos;')
total_alunos = cursor.fetchone()[0]
print(total_alunos)


'''
4. Atualização e Remoção
a) Atualize a idade de um aluno específico na tabela.
b) Remova um aluno pelo seu ID.
'''

# a) Atualize a idade de um aluno específico na tabela.
cursor.execute('UPDATE alunos SET idade=17 WHERE nome="Ana Moreira";')

# b) Remova um aluno pelo seu ID.
cursor.execute('DELETE FROM alunos WHERE id=2;')


'''
5. Criar uma Tabela e Inserir Dados
Crie uma tabela chamada "clientes" com os campos: id (chave
primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns
registros de clientes na tabela.
'''

cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT);')

registros_v2 = [
    (1, 'Ana Moreira', 30, 100.65),
    (2, 'Maria Silva', 20, 2564.63),
    (3, 'Lucia Pereira', 18, 10000.00),
    (4, 'Carlos Silva', 45, 10.05),
    (5, 'Maria Rodrigues', 58, 524.98),
    (6, 'João Rodrigues', 65, 278.51)
]

query_v2 = '''
INSERT INTO clientes(id, nome, idade, saldo) VALUES(?, ?, ?, ?);
'''

cursor.executemany(query_v2, registros_v2)


'''
6. Consultas e Funções Agregadas
Escreva consultas SQL para realizar as seguintes tarefas:
a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
b) Calcule o saldo médio dos clientes.
c) Encontre o cliente com o saldo máximo.
d) Conte quantos clientes têm saldo acima de 1000.
'''

# a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
dados_a2 = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30;')
for dado in dados_a2:
    print(dado)

# b) Calcule o saldo médio dos clientes.
cursor.execute('SELECT AVG(saldo) FROM clientes;')
saldo_medio = cursor.fetchone()[0]
print(saldo_medio)

# c) Encontre o cliente com o saldo máximo.
dados_c2 = cursor.execute('SELECT * FROM clientes WHERE saldo = (SELECT MAX(saldo) FROM clientes);')
for dado in dados_c2:
    print(dado)

# d) Conte quantos clientes têm saldo acima de 1000.
cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000;')
total_saldo_maior_1000 = cursor.fetchone()[0]
print(total_saldo_maior_1000)


'''
7. Atualização e Remoção com Condições
a) Atualize o saldo de um cliente específico.
b) Remova um cliente pelo seu ID.
'''

# a) Atualize o saldo de um cliente específico.
cursor.execute('UPDATE clientes SET saldo=10000.99 WHERE nome="Lucia Pereira";')

# b) Remova um cliente pelo seu ID.
cursor.execute('DELETE FROM clientes WHERE id=5;')


'''
8. Junção de Tabelas
Crie uma segunda tabela chamada "compras" com os campos: id
(chave primária), cliente_id (chave estrangeira referenciando o id
da tabela "clientes"), produto (texto) e valor (real). Insira algumas
compras associadas a clientes existentes na tabela "clientes".
Escreva uma consulta para exibir o nome do cliente, o produto e o
valor de cada compra.
'''

query_v3 = '''
    CREATE TABLE compras(
    id INT PRIMARY KEY,
    cliente_id INT,
    produto VARCHAR(100),
    valor REAL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);
'''

cursor.execute(query_v3)

query_v4 = '''
INSERT INTO compras (id, cliente_id, produto, valor) VALUES
    (1, 1, 'Produto A', 25.10),
    (2, 2, 'Produto B', 150.50),
    (3, 3, 'Produto C', 100.01),
    (4, 3, 'Produto D', 1120.25);
'''

cursor.execute(query_v4)

query_v5 = '''
SELECT clientes.nome AS nome_cliente, compras.produto, compras.valor
FROM compras
JOIN clientes ON compras.cliente_id = clientes.id;
'''

dados_consulta = cursor.execute(query_v5)

for dado in dados_consulta:
    print(dado)


conexao.commit()
conexao.close