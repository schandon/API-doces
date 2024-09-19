from flask import request, jsonify
from services.cliente_service import ClienteService


class ClientController:
    
    @staticmethod
    def create_client(data):
        try:
            client = ClienteService.create_client(data)
            return {'message': 'Client created successfully', 'client': client}, 201
        except Exception as e:
            return {'error': str(e)}, 400
