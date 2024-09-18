from models.PedidoClienteColaborador import PedidoClienteColadorador
from app import db

def create_pedidoClienteColadorador(data):
    new_pedidoClienteColadorador = PedidoClienteColadorador(**data)
    db.session.add(new_pedidoClienteColadorador)
    db.session.commit()
    return new_pedidoClienteColadorador

def get_all_pedidoClienteColadorador():
    return PedidoClienteColadorador.query.all()
