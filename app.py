from flask import Flask, jsonify
from config import Config
from models import db
from models.Cliente import Cliente

app = Flask(__name__)

# Carregar as configurações
app.config.from_object(Config)

# Inicializar a extensão SQLAlchemy
db.init_app(app)

# Garantir que as tabelas sejam criadas ao iniciar a aplicação
with app.app_context():
    db.create_all()

# Rota de exemplo
@app.route('/')
def index():
    return jsonify({"message": "API Doces rodando! 🚀", "status": "Success"});

if __name__ == "__main__":
    app.run(debug=True)
