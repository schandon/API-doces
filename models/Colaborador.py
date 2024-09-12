from app import db
from datetime import datetime

class Colaborador(db.Model):
    __tablename__ = 'Colaboradores'

    id = db.Column(db.Integer, primary_key=True,unique=True, increment=True)
    name = db.Column(db.String(100), nullable=False)
    user_name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    ultima_atualizado = db.Column(db.datetime, default=datetime.now())
    
    PedidoClienteColaborador = db.relationship('PedidoClienteColaborador', backref='author', lazy=True)