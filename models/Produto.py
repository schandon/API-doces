from . import db
from datetime import datetime

class Produto(db.Model):
    __tablename__ = 'Produtos'

    id = db.Column(db.Integer, primary_key=True,unique=True, increment=True)
    name = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(150), nullable=False)
    valor = db.Column(db.float, nullable=False)
    disponivel = db.Column(db.boolean, nullable=False)
    ultima_atualizado = db.Column(db.datetime, default=datetime.now())
    
    PedidoClienteColaborador = db.relationship('PedidoClienteColaborador', backref='author', lazy=True)
    
