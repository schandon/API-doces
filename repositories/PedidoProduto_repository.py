from models.PedidoProduto import PedidoProduto
from app import db

def create_pedidoProduto(data):
    new_pedidoProduto = PedidoProduto(**data)
    db.session.add(new_pedidoProduto)
    db.session.commit()
    return new_pedidoProduto

def get_all_pedidoProduto():
    return PedidoProduto.query.all()
