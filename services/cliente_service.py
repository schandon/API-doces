from repositories.cliente_repository import ClienteRepository
from models.Cliente import Cliente
from pydantic import ValidationError

class ClienteService:
    @staticmethod
    def create_cliente(data):
        try:
            new_cliente = Cliente(
                name=data['name'],
                email=data['email'],
                cpf=data['cpf'],
                cep=data['cep'],
                endereco=data['endereco'],
                numero=data['numero'],
                sexo=data['sexo'],
                estadoCivil=data['estadoCivil'],
                dataNascimento=data['dataNascimento'])
            ClienteRepository.add_cliente(new_cliente)
            return new_cliente
        except ValidationError as e:
            raise ValueError(f"Invalid client data: {e}")
   
    def update_cliente(cliente_id, data):
        cliente = ClienteRepository.get_cliente_by_id(cliente_id)
        if cliente:
            cliente.name=data['name'],
            cliente.email=data['email'],
            cliente.cpf=data['cpf'],
            cliente.cep=data['cep'],
            cliente.endereco=data['endereco'],
            cliente.numero=data['numero'],
            cliente.sexo=data['sexo'],
            cliente.estadoCivil=data['estadoCivil'],
            cliente.dataNascimento=data['dataNascimento']
            ClienteRepository.update_cliente(cliente)
        return cliente
   
    @staticmethod
    def list_clientes():
        return ClienteRepository.get_all()
    
    @staticmethod
    def find_cliente_by_id(Cliente_id):
        return ClienteRepository.get_by_id(Cliente_id)

    @staticmethod
    def delete_cliente(Cliente_id):
        cliente = ClienteRepository.get_by_id(Cliente_id)
        if cliente:
            ClienteRepository.delete_cliente(cliente)
        return cliente