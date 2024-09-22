from repositories.cliente_repository import ClienteRepository
from models.Cliente import Cliente
from pydantic import ValidationError

class ClienteService:
    @staticmethod
    def valida_cliente(dados):
        if not dados.get("nome"):
            raise ValueError("O Campo 'nome' é Obrigatório")
        if not dados.get("cpf"):
            raise ValueError("O Campo 'cpf' é Obrigatório")
        if not dados.get("endereco"):
            raise ValueError("O Campo 'endereco' é Obrigatório")
        if not dados.get("telefone"):
            raise ValueError("O Campo 'telefone' é Obrigatório")
        
    @staticmethod
    def add_Cliente(data):
        try:
            cliente = Cliente(**data)
            return ClienteRepository.create_cliente(cliente)
        except ValidationError as e:
            raise ValueError(f"Invalid client data: {e}")
   
   
    @staticmethod
    def list_Clientes():
        return ClienteRepository.get_all()
    
    @staticmethod
    def find_Cliente_by_id(Cliente_id):
        return ClienteRepository.get_by_id(Cliente_id)
