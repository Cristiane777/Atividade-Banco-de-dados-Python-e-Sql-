# Atividade Banco de dados (Python e Sql)

Dado o esquema a seguir:

CATEGORIA(id, descricao)
CLIENTE(id, nome, endereco, data_registro)
PRODUTOS(id, descricao, id_categoria, valor)
HISTORICO_PRECOS(id, id_produto, valor, data)
VENDAS(id, id_produto, id_cliente, data, quantidade, valor_unitario, valor_total)

Crie um arquivo chamado esquema.py conectando-se ao PostgreSQL, contendo a criação das tabelas usando peewee.
Crie um arquivo chamado dados.py que insira ao menos 5 linhas em cada tabela, e 10 linhas na tabela de vendas. Na tabela de histórico de preços, coloque o preço atual e a data atual de cada produto criado. Procure inserir informações de forma que as consultas a seguir retornem algum resultado.
Crie um arquivo chamado consultas.py que responda às consultas a seguir:
1 - Liste todo o histórico de preços (valor, data) do produto "Caneta Bic esferográfica azul".

2 - Liste descrição e preço de todos os produtos da categoria "Papelaria", ordenados no menor para o maior preço.

3 - Recupere os nomes dos clientes que fizeram ao menos uma compra com valor superior a R$ 5.000,00 no mês de setembro/2022. Exiba-os em ordem alfabética.
