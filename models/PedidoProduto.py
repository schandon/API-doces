from . import db
from datetime import datetime

class PedidoClienteColaborador(db.Model):
    __tablename__ = 'PedidoProduto'

    id = db.Column(db.Integer, primary_key=True,unique=True, increment=True)   
    id_produto = db.Column(db.integer, db.ForeignKey('Produtos.id'), nullable=False)
    id_pedido = db.Column(db.integer, db.ForeignKey('Pedidos.id'), nullable=False)
    ultima_atualizacao = db.Column(db.datetime, default=datetime.now())