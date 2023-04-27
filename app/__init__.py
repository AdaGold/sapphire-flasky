from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

"""
The responsibility of create_app is to:
- Connect Flask to our sapphire_flasky_development db
    - setting up SQLAlchemy and Migrate to do its thing
- Register our blueprints (our routes)
"""
def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:postgres@localhost:5432/sapphire_flasky_development"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate.init_app(app, db)

    #  add our new animals blueprint
    from flask import Blueprint
    from .routes.animal import animals_bp

    app.register_blueprint(animals_bp)

    return app 
