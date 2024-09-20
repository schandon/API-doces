from . import db
from datetime import datetime

class Venda(db.Model):
    __tablename__ = 'vendas'

    id = db.Column(db.Integer, primary_key=True ,unique=True )
    numero_pedido = db.Column(db.String, nullable=False)
    quantidade_itens = db.Column(db.Integer)
    id_cliente = db.Column(db.String, db.ForeignKey('Clientes.id'),nullable=False)
    id_produto = db.Column(db.Integer, db.ForeignKey('Produtos.id'),nullable=False)
    valor = db.Column(db.Float)
    data = db.Column(db.DateTime, nullable=False)
    ultima_atualizado = db.Column(db.DateTime, default=datetime.now())
    
    PedidoClienteColaborador = db.relationship('PedidoClienteColaborador', backref='author', lazy=True)
    PedidoProduto = db.relationship('PedidoProdutos', backref='author', lazy=True)
    
    
def __repr__(self):
    return f'<Vendas {self.nome}>'
