from flask import Blueprint, request, jsonify
from controllers.cliente_controller import ClientController

cliente_bp = Blueprint('cliente', __name__)

@cliente_bp.route('/cliente', methods=['POST'])
def create_client():
    data = request.json
    response = ClientController.create_client(data)
    return jsonify(response), response.get('status_code', 200)
