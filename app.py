from flask import Flask
from flask_migrate import Migrate
from config import Config, db
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

from routes.cliente_routes import cliente_bp

app.register_blueprint(cliente_bp)

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
