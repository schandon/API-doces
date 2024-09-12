from models.Venda import Venda
from app import db

def create_venda(data):
    new_venda = Venda(**data)
    db.session.add(new_venda)
    db.session.commit()
    return new_venda

def get_all_venda():
    return Venda.query.all()
