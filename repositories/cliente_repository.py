from models.Cliente import Cliente
from app import db

class ClienteRepository:
    @staticmethod
    def create(cliente_data):
        new_cliente = Cliente(**cliente_data)
        db.session.add(new_cliente)
        db.session.commit()
        return new_cliente

    @staticmethod
    def get_all():
        return Cliente.query.all()
    
    @staticmethod
    def get_by_id(user_id):
        return Cliente.query.get(user_id)
