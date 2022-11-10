from Esquema import Categoria, Cliente, Produtos, Historico_precos,Vendas

# Liste todo o histórico de preços (valor, data) do produto "Caneta Bic esferográfica azul".

query1 = Historico_precos.select().join(Produtos, on = Historico_precos.id_produto == Produtos.id).where(Produtos.descricao == 'Caneta Bic esferográfica azul')

for row in query1:
    print('descricao: ',row.id_produto.descricao,' valor: ', row.valor, 'data:', row.data)


# Liste descrição e preço de todos os produtos da categoria "Papelaria", ordenados no menor para o maior preço.

query2 = Produtos.select().join(Categoria, on = Produtos.id_categoria == Categoria.id).where(Categoria.descricao == 'Papelaria').order_by(Produtos.valor)

for row in query2:
    print('descricao: ', row.descricao, 'valor: ', row.valor)

# Recupere os nomes dos clientes que fizeram ao menos uma compra com valor superior a R$ 5.000,00 no mês de setembro/2022. Exiba-os em ordem alfabética.

query3 = Vendas.select().join(Cliente, on = Vendas.id_cliente == Cliente.id).where(Vendas.valor_total >= 5000 and Vendas.data.between ('2022-09-01','2022-09-30')).order_by(Cliente.nome)

for row in query3:
    print('id_cliente: ', row.id_cliente.nome, 'valor: ', row.valor_total)

