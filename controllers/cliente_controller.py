from flask import Blueprint, jsonify, request
from services.cliente_service import ClienteService

Cliente_bp = Blueprint('Clientes', __name__)

@Cliente_bp.route('/Clientes', methods=['GET'])
def get_Clientes():
    Clientes = ClienteService.list_Clientes()
    return jsonify([{'id': Cliente.id, 'name': Cliente.name, 'email': Cliente.email, 'cpf': Cliente.cpf,'cep' : Cliente.cep,
                     'endereco' :Cliente.endereco   , 'numero' : Cliente.numero, 'sexo' :  Cliente.sexo,'dataNascimento' : Cliente.dataNascimento} for Cliente in Clientes])

@Cliente_bp.route('/Clientes/<int:Cliente_id>', methods=['GET'])
def get_Cliente(Cliente_id):
    Cliente = ClienteService.find_Cliente_by_id(Cliente_id)
    if not Cliente:
        return jsonify({'message': 'Cliente not found'}), 404
    return jsonify({'id': Cliente.id, 'name': Cliente.name, 'email': Cliente.email, 'cpf': Cliente.cpf,'cep' : Cliente.cep,
                    'endereco' :Cliente.endereco   , 'numero' : Cliente.numero, 'sexo' :  Cliente.sexo,'dataNascimento' : Cliente.dataNascimento})

@Cliente_bp.route('/Clientes', methods=['POST'])
def create_Cliente():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    cpf = data.get('cpf')
    cep = data.get('cep')
    endereco = data.get('endereco')
    numero = data.get('numero')
    sexo = data.get('sexo')
    dataNascimento = data.get('dataNascimento')
    new_Cliente = ClienteService.add_Cliente(name, email, cpf, cep, endereco, numero, sexo, dataNascimento)
    return jsonify({'id': new_Cliente.id, 'name': new_Cliente.name, 'email': new_Cliente.email, 'cpf': new_Cliente.cpf,'cep' : new_Cliente.cep,
                    'endereco' :new_Cliente.endereco   , 'numero' : new_Cliente.numero, 'sexo' :  new_Cliente.sexo,'dataNascimento' : new_Cliente.dataNascimento}), 201
