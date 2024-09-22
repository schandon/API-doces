from flask import Flask, jsonify
from flask_migrate import Migrate
from config import Config
from models import db

app = Flask(__name__)

def create_app():    
    app.config.from_object(Config)

    migrate = Migrate()
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
