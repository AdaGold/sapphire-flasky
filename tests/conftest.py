import pytest
from app import create_app
from app import db
from flask.signals import request_finished


# CREATE A NEW "TEST" APP 
@pytest.fixture 
def app():
    app = create_app({"TESTING": True})

    # CLOSE THE DATABASE SESSION
    @request_finished.connect_via(app)
    def expire_session(send, response, **extra):
        db.session.remove()

    # AKA ARRANGE PORTION OF TESTING 
    # SET UP A DATABASE
    with app.app_context():
        db.create_all()  # RUN ALL THE MIGRATIONS
        yield app

    # CLEAR DATABASE
    with app.app_context():
        db.drop_all()

# CREATE A NEW CLIENT TO SEND OUR REQUESTS
# AKA: creating a pytest version of Postman
@pytest.fixture 
def client(app):
    return app.test_client()


# POPULATE DATABASE

    
        