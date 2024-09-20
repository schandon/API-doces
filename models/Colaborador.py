from . import db
from datetime import datetime

class Colaborador(db.Model):
    __tablename__ = 'colaboradores'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(100), nullable=False)
    user_name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    ultima_atualizacao = db.Column(db.DateTime, default=datetime.now())

    
    def __repr__(self):
        return f'<Colaborador {self.name}>'
