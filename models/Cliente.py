from . import db
from datetime import datetime


class Cliente(db.Model):
    __tablename__ = 'Clientes'

    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    endereco = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.Integer)
    sexo = db.Column(db.String(1))
    estado_civil = db.Column(db.String(50), default="Solteiro")
    data_nascimento = db.Column(db.DateTime)
    ultima_atualizado = db.Column(db.DateTime, default=datetime.now)
    PedidoClienteColaborador = db.relationship('PedidoClienteColaborador', backref='author', lazy=True)
    
    def __repr__(self):
        return f'<Cliente {self.nome}>'
