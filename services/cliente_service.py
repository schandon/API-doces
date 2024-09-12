from repositories.cliente_repository import create_cliente, get_all_cliente

class ClienteRepository:
    def valida_cliente(dados):
        if not dados.get("nome"):
            raise ValueError("O Campo 'nome' é Obrigatório")
        if not dados.get("cpf"):
            raise ValueError("O Campo 'cpf' é Obrigatório")
        if not dados.get("endereco"):
            raise ValueError("O Campo 'endereco' é Obrigatório")
        if not dados.get("telefone"):
            raise ValueError("O Campo 'telefone' é Obrigatório")
        
    def add_cliente(self,cliente_data):
        try:
            self.valida_cliente(cliente_data)
            print("Cliente criados com Sucesso!")
            return create_cliente(cliente_data)
        except ValueError as e:
            print(f"Erro ao Criar Cliente: {e}")
        except Exception as e:
            print(f"Erro Inesperado: {e}")

    def fetch_all_cliente():
        return get_all_cliente()
