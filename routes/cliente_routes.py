from flask import Blueprint, jsonify
from controllers.cliente_controller import ClienteController

cliente_bp = Blueprint('cliente', __name__)

# Rota de teste para verificar se a API está rodando
@cliente_bp.route('/', methods=['GET'])
def home():
    return jsonify({"message": "API Doces rodando! 🚀", "status": "Success"})

# Rotas para cliente
@cliente_bp.route('/cliente', methods=['GET'])
def get_all_clientes():
    return ClienteController.get_all_cliente()

@cliente_bp.route('/cliente/<int:cliente_id>', methods=['GET'])
def get_cliente(cliente_id):
    return ClienteController.get_cliente(cliente_id)

@cliente_bp.route('/cliente', methods=['POST'])
def create_cliente():
    return ClienteController.create_cliente()

@cliente_bp.route('/cliente/<int:cliente_id>', methods=['PUT'])
def update_cliente(cliente_id):
    return ClienteController.update_cliente(cliente_id)

@cliente_bp.route('/cliente/<int:cliente_id>', methods=['DELETE'])
def delete_cliente(cliente_id):
    return ClienteController.delete_cliente(cliente_id)
