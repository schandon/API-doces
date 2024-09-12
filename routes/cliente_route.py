from flask import Blueprint
from controllers.cliente_controller import create_cliente, get_clientes

cliente_bp = Blueprint('clientes_bp', __name__)

cliente_bp.route('/clientes', methods=['POST'])(create_cliente)
cliente_bp.route('/clientes', methods=['GET'])(get_clientes)
