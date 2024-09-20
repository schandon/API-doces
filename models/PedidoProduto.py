from . import db
from datetime import datetime

class PedidoProduto(db.Model):
    __tablename__ = 'pedidoProduto'

    id = db.Column(db.Integer, primary_key=True,unique=True)   
    id_produto = db.Column(db.Integer, db.ForeignKey('Produtos.id'), nullable=False)
    id_pedido = db.Column(db.Integer, db.ForeignKey('Pedidos.id'), nullable=False)
    ultima_atualizacao = db.Column(db.DateTime, default=datetime.now())

def __repr__(self):
    return f'<PedidoProduto {self.nome}>'