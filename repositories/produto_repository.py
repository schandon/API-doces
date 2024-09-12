from models.Produto import Produto
from app import db

def create_produto(data):
    new_produto = Produto(**data)
    db.session.add(new_produto)
    db.session.commit()
    return new_produto

def get_all_produto():
    return Produto.query.all()
