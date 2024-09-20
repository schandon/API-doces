from . import db
from datetime import datetime

class VendaClienteColaborador(db.Model):
    __tablename__ = 'vendaClienteColaborador'

    id = db.Column(db.Integer, primary_key=True,unique=True )   
    id_cliente = db.Column(db.Integer, db.ForeignKey('Clientes.id'), nullable=False)
    id_colaborador = db.Column(db.Integer, db.ForeignKey('Colaboradores.id'), nullable=False)
    id_venda = db.Column(db.Integer, db.ForeignKey('Vendas.id'), nullable=False)
    id_produto = db.Column(db.Integer, db.ForeignKey('Produtos.id'), nullable=False)
    ultima_atualizacao = db.Column(db.DateTime, default=datetime.now())
    
def __repr__(self):
    return f'<vendaClienteColaborador {self.nome}>'