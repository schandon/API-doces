from flask import request, jsonify
from services.cliente_service import add_cliente, fetch_all_cliente

def create_user():
    data = request.get_json()
    user = add_cliente(data)
    return jsonify(user), 201

def get_users():
    users = fetch_all_cliente()
    return jsonify(users), 200
