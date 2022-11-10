from email.policy import default
from tokenize import Floatnumber
from peewee import PostgresqlDatabase, Model, TextField, ForeignKeyField, DateTimeField, FloatField, IntegerField
from datetime import datetime

db = PostgresqlDatabase('esquema', host='localhost', port=5432, 
    user='postgres', password='123456')

class BaseModel(Model):
    class Meta:
        database = db

class Categoria(BaseModel):
    descricao = TextField(unique=True)

class Cliente(BaseModel):
    nome = TextField(null=False)
    endereco = TextField()
    data_registro = DateTimeField(default=datetime.now)

class Produtos(BaseModel):
    descricao = TextField(unique=True)
    id_categoria = ForeignKeyField(Categoria,backref='categoria')
    valor = FloatField()

class Historico_precos(BaseModel):
    id_produto = ForeignKeyField(Produtos,backref='produto')
    valor = FloatField(default = 8)
    data = DateTimeField(default=datetime.now)

class Vendas(BaseModel):
    id_produto = ForeignKeyField(Produtos,backref='produto')
    id_cliente = ForeignKeyField(Cliente,backref='cliente')
    data = DateTimeField(default=datetime.now)
    quantidade = IntegerField()
    valor_unitario = FloatField()
    valor_total = FloatField()

lista_tabelas = [
    Categoria,Cliente,Produtos,Historico_precos,Vendas
]

db.connect()
db.create_tables(lista_tabelas)
db.close()
