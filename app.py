from flask import Flask, jsonify
from flask_migrate import Migrate
from config import Config
from models import db
from models.Cliente import Cliente
from models.Colaborador import Colaborador
from models.Pedido import Pedido
from models.Produto import Produto


app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app,db)

# Garantir que as tabelas sejam criadas ao iniciar a aplicação
with app.app_context():
    db.create_all()

# Rota de exemplo
@app.route('/')
def index():
    return jsonify({"message": "API Doces rodando! 🚀", "status": "Success"});

if __name__ == "__main__":
    app.run(debug=True)
