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

@cliente_bp.route('/Clientes', methods=['GET'])
def get_Clientes():
    Clientes = ClienteService.list_Clientes()
    return jsonify([cliente_to_json(Cliente) for Cliente in Clientes])

@cliente_bp.route('/Clientes/<int:Cliente_id>', methods=['GET'])
def get_Cliente(Cliente_id):
    Cliente = ClienteService.find_Cliente_by_id(Cliente_id)
    if not Cliente:
        return jsonify({'message': 'Cliente not found'}), 404
    return jsonify(cliente_to_json(Cliente))

@cliente_bp.route('/Clientes', methods=['POST'])
def create_Cliente():
    data = request.get_json()
    try:
        new_Cliente = ClienteService.add_Cliente(data)
        return jsonify(new_Cliente), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
