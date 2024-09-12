from app import db
from datetime import datetime

class VendaClienteColaborador(db.Model):
    __tablename__ = 'vendaClienteColaborador'

    id = db.Column(db.Integer, primary_key=True,unique=True, increment=True)   
    id_cliente = db.Column(db.integer, db.ForeignKey('Clientes.id'), nullable=False)
    id_colaborador = db.Column(db.integer, db.ForeignKey('Colaboradores.id'), nullable=False)
    id_venda = db.Column(db.integer, db.ForeignKey('Vendas.id'), nullable=False)
    id_produto = db.Column(db.integer, db.ForeignKey('Produtos.id'), nullable=False)
    ultima_atualizacao = db.Column(db.datetime, default=datetime.now())