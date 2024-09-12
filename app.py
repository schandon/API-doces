from flask import Flask, jsonify;
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

engine = create_engine(os.getenv('DATABASE_URL'))
metadata = MetaData(schema='public')


@app.route('/')
def home():
    return jsonify({"message": "API Doces rodando! 🚀", "status": "Success"});

if __name__ == '__main__':
    app.run(debug=True)
