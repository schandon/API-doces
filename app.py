from flask import Flask, jsonify
from flask_migrate import Migrate
from config import Config

# Crie o Flask app primeiro
app = Flask(__name__)
app.config.from_object(Config)

migrate = Migrate()

def create_app():
    from models import db  # Agora pode importar db sem erro circular
    from controllers.cliente_controller import cliente_bp

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(cliente_bp)

    with app.app_context():
        db.create_all()

    return app

@app.route('/')
def index():
    return jsonify({"message": "API Doces rodando! 🚀", "status": "Success"})

if __name__ == "__main__":
    create_app().run(debug=True)
