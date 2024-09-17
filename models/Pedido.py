from . import db
from datetime import datetime

class Pedido(db.Model):
    __tablename__ = 'Pedidos'

    id = db.Column(db.Integer, primary_key=True,unique=True, increment=True)
    numero_pedido = db.Column(db.String, nullable=False, increment=True)
    quantidade_itens = db.Column(db.integer)
    id_cliente = db.Column(db.String, db.ForeignKey('Clientes.id'),nullable=False)
    id_produto = db.Column(db.integer, db.ForeignKey('Produtos.id'),nullable=False)
    valor = db.Column(db.float)
    data = db.Column(db.datetime, nullable=False)
    ultima_atualizado = db.Column(db.datetime, default=datetime.now())
    
    PedidoClienteColaborador = db.relationship('PedidoClienteColaborador', backref='author', lazy=True)
    PedidoProduto = db.relationship('PedidoProdutos', backref='author', lazy=True)