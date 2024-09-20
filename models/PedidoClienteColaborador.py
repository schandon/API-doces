from . import db
from datetime import datetime

class PedidoClienteColaborador(db.Model):
    __tablename__ = 'pedidoClienteColaborador'

    id = db.Column(db.Integer, primary_key=True,unique=True)   
    id_cliente = db.Column(db.Integer, db.ForeignKey('Clientes.id'), nullable=False)
    id_colaborador = db.Column(db.Integer, db.ForeignKey('Colaboradores.id'), nullable=False)
    id_pedido = db.Column(db.Integer, db.ForeignKey('Pedidos.id'), nullable=False)
    id_produto = db.Column(db.Integer, db.ForeignKey('Produtos.id'), nullable=False)
    ultima_atualizacao = db.Column(db.DateTime, default=datetime.now())

def __repr__(self):
    return f'<PedidoClienteColaborador {self.nome}>'