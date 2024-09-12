# app/repositories/user_repository.py
from models.Cliente import Cliente
from app import db

def create_cliente(data):
    new_cliente = Cliente(**data)
    db.session.add(new_cliente)
    db.session.commit()
    return new_cliente

def get_all_cliente():
    return Cliente.query.all()
