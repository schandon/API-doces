from . import db
from datetime import datetime


class Cliente(db.Model):
    __tablename__ = 'clientes'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    endereco = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.Integer)
    sexo = db.Column(db.String(1))
    estadoCivil = db.Column(db.String(50), default="Solteiro")
    dataNascimento = db.Column(db.DateTime)
    ultimaAtualizado = db.Column(db.DateTime, default=datetime.now())
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def __repr__(self):
        return f'<Cliente {self.nome}>'
