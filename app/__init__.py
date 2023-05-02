from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

"""
The responsibility of create_app is to:
- Connect Flask to our sapphire_flasky_development db
    - setting up SQLAlchemy and Migrate to do its thing
- Register our blueprints (our routes)
"""
def create_app(testing=None):
    app = Flask(__name__)

    if testing is None:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DEV_DATABASE_URI')
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('TEST_DATABASE_URI')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate.init_app(app, db)


    from app.models.animal import Animal


    #  add our new animals blueprint
    from flask import Blueprint
    from .routes.animal import animals_bp

    app.register_blueprint(animals_bp)

    return app 
