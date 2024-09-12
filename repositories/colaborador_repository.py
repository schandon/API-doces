from models.Colaborador import Colaborador
from app import db

def create_colaborador(data):
    new_colaborador = Colaborador(**data)
    db.session.add(new_colaborador)
    db.session.commit()
    return new_colaborador

def get_all_colaborador():
    return Colaborador.query.all()
