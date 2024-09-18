from . import db
from datetime import datetime

class Produto(db.Model):
    __tablename__ = 'produtos'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(150), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    disponivel = db.Column(db.Boolean, nullable=False)
    ultima_atualizado = db.Column(db.DateTime, default=datetime.now)
    
def __repr__(self):
    return f'<Produtos {self.nome}>'
    
