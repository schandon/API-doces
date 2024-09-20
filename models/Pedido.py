from . import db
from datetime import datetime

class Pedido(db.Model):
    __tablename__ = 'pedidos'

    id = db.Column(db.Integer, primary_key=True,unique=True)
    numero_pedido = db.Column(db.String, nullable=False)
    quantidade_itens = db.Column(db.Integer)
    valor = db.Column(db.Float)
    data = db.Column(db.DateTime, nullable=False)
    ultima_atualizado = db.Column(db.DateTime, default=datetime.now())

    
def __repr__(self):
    return f'<Pedidos {self.nome}>'