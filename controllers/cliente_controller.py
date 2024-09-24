from flask import Blueprint, jsonify, request
from services.cliente_service import ClienteService
from models import db

cliente_bp = Blueprint('Clientes', __name__)

def cliente_to_json(Cliente):
    return {
        'id': Cliente.id,
        'name': Cliente.name,
        'email': Cliente.email,
        'cpf': Cliente.cpf,
        'cep': Cliente.cep,
        'endereco': Cliente.endereco,
        'numero': Cliente.numero,
        'sexo': Cliente.sexo,
        'dataNascimento': Cliente.dataNascimento
    }

class ClienteController:
    @staticmethod
    def get_all_cliente():
        clientes = ClienteService.get_all_cliente()
        return jsonify([cliente.as_dict() for cliente in clientes]), 200
    
    @staticmethod
    def get_cliente(cliente_id):
        cliente = ClienteService.find_Cliente_by_id(cliente_id)
        if cliente:
            return jsonify(cliente.as_dict()), 200
        return jsonify({'Message':"Cliente não encontrado"}), 404 

    @staticmethod
    def create_cliente():
        data = request.get_json()
        cliente = ClienteService.create_cliente(data)
        return jsonify(cliente.as_dict()), 201
    @staticmethod
    def update_cliente(cliente_id):
        data = request.get_json()
        cliente = ClienteService.update_cliente(cliente_id, data)
        if cliente:
            return jsonify(cliente.as_dict()), 200
        return jsonify({'message': 'Product not found'}), 404

    @staticmethod
    def delete_cliente(cliente_id):
        cliente = ClienteService.delete_cliente(cliente_id)
        if cliente:
            return jsonify({'message': 'Product deleted'}), 200
        return jsonify({'message': 'Product not found'}), 404
