from pydantic import BaseModel
from typing import Optional, List
from models.Cliente import cliente
from datetime import datetime


class ClienteSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    id: str = "01"
    name: str = "Alexandre Pereira"
    email: str = "alexandre.pereira@teste.com"
    cpf: str = "999999999-99"
    cep: str = "22795050"
    endereco: str = ""
    numero: int  = 23
    sexo: str = "M"
    estado_civil: str = "Solteiro"
    data_nascimento: datetime = 26/10/1997
    


class ClienteViewSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    id: str = "01"
    name: str = "Alexandre Pereira"
    email: str = "alexandre.pereira@teste.com"
    cpf: str = "999999999-99"
    cep: str = "22795050"
    endereco: str = ""
    numero: int  = 23
    sexo: str = "M"
    estado_civil: str = "Solteiro"
    data_nascimento: datetime = 26/10/1997


class ClienteBuscaPorNomeSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do produto.
    """
    name: str = "Alexandre"


class ClienteBuscaPorIDSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no ID do produto.
    """
    id: int = "1"


class ListagemClientesSchema(BaseModel):
    """ Define como uma listagem de Clientes será retornada.
    """
    Clientes:List[ClienteViewSchema]


def apresenta_clientes(cliente: List[cliente]):
    """ Retorna uma representação do Cliente seguindo o schema definido em
        ListagemClientesSchema.
    """
    result = []
    for cliente in cliente:
        result.append({
            "id": cliente.id,
            "nome": cliente.nome,
            "preco": cliente.preco,
            "descricao": cliente.descricao,
            "marca": cliente.marca,
            "categoria": cliente.categoria,
            "comentarios": [c.texto for c in cliente.comentarios]
        })

    return {"produtos": result}


class ClienteViewSchema(BaseModel):
    """ Define como um Cliente será retornado: produto + comentários.
    """
    id: int = 1
    nome: str = "Camiseta"
    preco: float = 29.99
    descricao: str = "Uma camiseta confortável e estilosa"
    marca: str = "MarcaX"
    categoria: str = "Roupas"
    total_cometarios: int = 1
    comentarios:List[str] = ["Só comprar se o preço realmente estiver bom!"]


class ClienteDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    id: int


def apresenta_cliente(cliente: cliente):
    """ Retorna uma representação do cliente seguindo o schema definido em
        clienteViewSchema.
    """
    return {
        "id": cliente.id,
        "nome": cliente.nome,
        "preco": cliente.preco,
        "descricao": cliente.descricao,
        "marca": cliente.marca,
        "categoria": cliente.categoria,
        "total_cometarios": len(cliente.comentarios),
        "comentarios": [c.texto for c in cliente.comentarios]
    }
