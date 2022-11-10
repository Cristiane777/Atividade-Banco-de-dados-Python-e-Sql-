from Esquema import *
from datetime import datetime

lista_categorias = [
    {'descricao': 'Papelaria'},
    {'descricao': 'Alimentos'},
    {'descricao': 'Roupas'},
    {'descricao': 'Higiene'},
    {'descricao': 'Bebidas'},
    
]

Categoria.insert_many(lista_categorias).execute()

lista_clientes = [
    {'nome': 'Juliana Paes','endereco':'França', 'data_registro': '2022-02-11'},
    {'nome': 'Graziele Almeida','endereco':'Brasil', 'data_registro': '2022-03-09'},
    {'nome': 'Jenny Lopes','endereco':'Itália','data_registro': '2022-05-12'},
    {'nome': 'João Grilo','endereco':'Brasil','data_registro': '2022-07-01'},
    {'nome': 'Bruno Mars','endereco':'EUA', 'data_registro': '2022-08-10'},
        
]

Cliente.insert_many(lista_clientes).execute()

lista_produtos = [
    {'descricao':'Caneta Bic esferográfica azul', 'id_categoria': Categoria.select().where(Categoria.descricao == 'Papelaria').get(), 'valor': 2.00},
    {'descricao':'Caderno 20 matérias', 'id_categoria': Categoria.select().where(Categoria.descricao == 'Papelaria').get(), 'valor': 25.00},
    {'descricao':'Borracha', 'id_categoria': Categoria.select().where(Categoria.descricao == 'Papelaria').get(), 'valor': 3.00},
    {'descricao':'Arroz parborizado Urbano', 'id_categoria': Categoria.select().where(Categoria.descricao == 'Alimentos').get(), 'valor': 5.00},
    {'descricao':'Calça Jeans', 'id_categoria': Categoria.select().where(Categoria.descricao == 'Roupas').get(), 'valor': 100.00},
    {'descricao':'Creme dental Colgate', 'id_categoria': Categoria.select().where(Categoria.descricao == 'Higiene').get(), 'valor': 10.00},
    {'descricao':'Água mineral indaiá 500 ml', 'id_categoria': Categoria.select().where(Categoria.descricao == 'Bebidas').get(), 'valor': 2.00},
    
]

Produtos.insert_many(lista_produtos).execute()

lista_historico_precos = [
    {'id_produto':Produtos.select().where(Produtos.descricao == 'Caneta Bic esferográfica azul').get(), 'valor': Produtos.select(Produtos.valor).where (Produtos.descricao == 'Caneta Bic esferográfica azul').get().valor,'data':'2022-01-23'},

    {'id_produto':Produtos.select().where(Produtos.descricao == 'Caderno 20 matérias').get(), 'valor': Produtos.select(Produtos.valor).where (Produtos.descricao == 'Caderno 20 matérias').get().valor,'data':'2022-01-23'},

    {'id_produto':Produtos.select().where(Produtos.descricao == 'Borracha').get(), 'valor': Produtos.select(Produtos.valor).where (Produtos.descricao == 'Borracha').get().valor,'data':'2022-01-23'},

    {'id_produto':Produtos.select().where(Produtos.descricao == 'Arroz parborizado Urbano').get(), 'valor': Produtos.select(Produtos.valor).where (Produtos.descricao == 'Arroz parborizado Urbano').get().valor,'data':'2022-01-23'},

    {'id_produto':Produtos.select().where(Produtos.descricao == 'Calça Jeans').get(), 'valor': Produtos.select(Produtos.valor).where (Produtos.descricao == 'Calça Jeans').get().valor,'data':'2022-01-23'},

    {'id_produto':Produtos.select().where(Produtos.descricao == 'Creme dental Colgate').get(), 'valor': Produtos.select(Produtos.valor).where (Produtos.descricao == 'Creme dental Colgate').get().valor,'data':'2022-01-23'},

    {'id_produto':Produtos.select().where(Produtos.descricao == 'Água mineral indaiá 500 ml').get(), 'valor': Produtos.select(Produtos.valor).where (Produtos.descricao == 'Água mineral indaiá 500 ml').get().valor,'data':'2022-01-23'},
   
]

Historico_precos.insert_many(lista_historico_precos).execute()

lista_vendas = [
    {
        'id_produto': Produtos.select().where(Produtos.descricao == 'Caneta Bic esferográfica azul').get(), 
        'id_cliente': Cliente.select().where(Cliente.nome == 'Juliana Paes'), 
        'data': '2022-03-12', 
        'quantidade': 1000, 
        'valor_unitario' : Produtos.select(Produtos.valor).where(Produtos.descricao == 'Caneta Bic esferográfica azul').get().valor, 
        'valor_total': 1000 * Produtos.select(Produtos.valor).where(Produtos.descricao == 'Caneta Bic esferográfica azul').get().valor
    },

    {
        'id_produto': Produtos.select().where(Produtos.descricao == 'Caderno 20 matérias').get(), 
        'id_cliente': Cliente.select().where(Cliente.nome == 'Juliana Paes'), 
        'data': '2022-04-15', 
        'quantidade': 500, 
        'valor_unitario' : Produtos.select(Produtos.valor).where(Produtos.descricao == 'Caderno 20 matérias').get().valor, 
        'valor_total': 500 * Produtos.select(Produtos.valor).where(Produtos.descricao == 'Caderno 20 matérias').get().valor
    },

    {
        'id_produto': Produtos.select().where(Produtos.descricao == 'Arroz parborizado Urbano').get(), 
        'id_cliente': Cliente.select().where(Cliente.nome == 'Jenny Lopes'), 
        'data': '2022-05-23', 
        'quantidade': 500, 
        'valor_unitario' : Produtos.select(Produtos.valor).where(Produtos.descricao == 'Arroz parborizado Urbano').get().valor, 
        'valor_total': 500 * Produtos.select(Produtos.valor).where(Produtos.descricao == 'Arroz parborizado Urbano').get().valor
    },

    {
        'id_produto': Produtos.select().where(Produtos.descricao =='Borracha'). get(),
        'id_cliente': Cliente.select().where(Cliente.nome == 'Jenny Lopes'), 
        'data': '2022-06-20', 'quantidade': 5, 
        'valor_unitario' : Produtos.select(Produtos.valor).where(Produtos.descricao == 'Borracha').get().valor, 'valor_total': 5 * Produtos.select(Produtos.valor).where(Produtos.descricao == 'Borracha').get().valor
    },

    {
        'id_produto': Produtos.select().where(Produtos.descricao == 'Creme dental Colgate').get(),
        'id_cliente': Cliente.select().where(Cliente.nome == 'João Grilo'), 
        'data': '2022-08-05', 
        'quantidade': 10, 
        'valor_unitario' : Produtos.select(Produtos.valor).where(Produtos.descricao == 'Creme dental Colgate').get().valor, 
        'valor_total': 10 * Produtos.select(Produtos.valor).where(Produtos.descricao == 'Creme dental Colgate').get().valor
    },

    {
        'id_produto': Produtos.select().where(Produtos.descricao == 'Calça Jeans').get(),
        'id_cliente': Cliente.select().where(Cliente.nome == 'Graziele Almeida'), 
        'data': '2022-09-17', 
        'quantidade': 100, 
        'valor_unitario' : Produtos.select(Produtos.valor).where(Produtos.descricao == 'Calça Jeans').get().valor, 'valor_total': 100 * Produtos.select(Produtos.valor).where(Produtos.descricao == 'Calça Jeans').get().valor
    },

    {
        'id_produto': Produtos.select().where(Produtos.descricao == 'Água mineral indaiá 500 ml').get(),'id_cliente': Cliente.select().where(Cliente.nome == 'Bruno Mars'), 
        'data': '2022-09-30', 
        'quantidade': 2500, 
        'valor_unitario' : Produtos.select(Produtos.valor).where(Produtos.descricao == 'Água mineral indaiá 500 ml').get().valor, 
        'valor_total': 2500 * Produtos.select(Produtos.valor).where(Produtos.descricao == 'Água mineral indaiá 500 ml').get().valor},

    {
        'id_produto': Produtos.select().where(Produtos.descricao == 'Caneta Bic esferográfica azul').get(),
        'id_cliente': Cliente.select().where(Cliente.nome == 'João Grilo'), 
        'data': '2022-10-22', 
        'quantidade': 300, 
        'valor_unitario' : Produtos.select(Produtos.valor).where(Produtos.descricao == 'Caneta Bic esferográfica azul').get().valor, 
        'valor_total': 300 *Produtos.select(Produtos.valor).where(Produtos.descricao == 'Caneta Bic esferográfica azul').get().valor
    },

    {
        'id_produto': Produtos.select().where(Produtos.descricao == 'Calça Jeans').get(),
        'id_cliente': Cliente.select().where(Cliente.nome == 'Bruno Mars'), 
        'data': '2022-11-07', 
        'quantidade': 10, 
        'valor_unitario' : Produtos.select(Produtos.valor).where(Produtos.descricao == 'Calça Jeans').get().valor, 'valor_total': 10 * Produtos.select(Produtos.valor).where(Produtos.descricao == 'Calça Jeans').get().valor
    },

    {
        'id_produto': Produtos.select().where(Produtos.descricao == 'Água mineral indaiá 500 ml').get(),
        'id_cliente': Cliente.select().where(Cliente.nome == 'Graziele Almeida'), 
        'data': '2022-12-01', 
        'quantidade': 500, 
        'valor_unitario' : Produtos.select(Produtos.valor).where(Produtos.descricao == 'Água mineral indaiá 500 ml').get().valor, 
        'valor_total': 500 * Produtos.select(Produtos.valor).where(Produtos.descricao == 'Água mineral indaiá 500 ml').get().valor
    },
]

Vendas.insert_many(lista_vendas).execute()

