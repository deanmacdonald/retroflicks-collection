# app/__init__.py

import os
from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv

# 🌿 Load .env variables
load_dotenv()

# 📦 Internal imports
from app.extensions import db
from app.routes import routes_bp

def create_app():
    app = Flask(__name__)

    # 🔧 Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///movies.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')

    # ⚙️ Extensions
    db.init_app(app)
    migrate = Migrate(app, db)

    # 🛣️ Routes
    app.register_blueprint(routes_bp)

    return app

