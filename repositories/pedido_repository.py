# app/repositories/user_repository.py
from models.Pedido import Pedido
from app import db

def create_pedido(data):
    new_pedido = Pedido(**data)
    db.session.add(new_pedido)
    db.session.commit()
    return new_pedido

def get_all_pedido():
    return Pedido.query.all()
