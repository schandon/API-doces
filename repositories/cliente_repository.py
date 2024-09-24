from models.Cliente import Cliente
from . import db

class ClienteRepository:
    @staticmethod
    def add_cliente(new_cliente):
        db.session.add(new_cliente)
        db.session.commit()
        return new_cliente

    @staticmethod
    def get_all():
        return Cliente.query.all()
    
    @staticmethod
    def get_cliente_by_id(user_id):
        return Cliente.query.get(user_id)
    
    @staticmethod
    def update_cliente(cliente):
        db.session.commit()

    @staticmethod
    def delete_cliente(cliente):
        db.session.delete(cliente)
        db.session.commit()