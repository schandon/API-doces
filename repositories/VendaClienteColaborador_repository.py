from models.VendaClienteColadorador import VendaClienteColadorador
from app import db

def create_vendaClienteColadorador(data):
    new_vendaClienteColadorador = VendaClienteColadorador(**data)
    db.session.add(new_vendaClienteColadorador)
    db.session.commit()
    return new_vendaClienteColadorador

def get_all_vendaClienteColadorador():
    return VendaClienteColadorador.query.all()
