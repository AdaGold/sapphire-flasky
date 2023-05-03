import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.animal import Animal


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
@pytest.fixture
def three_animals(app):
    animal_one = Animal(id=1, name="Furby", species="Cat", age=17)
    animal_two = Animal(id=2, name="Gouda", species="Cheese Monster", age=14)
    animal_three = Animal(id=3, name="Foxy", species="Flamingo", age=100)

    db.session.add(animal_one)
    db.session.add(animal_two)
    db.session.add(animal_three)

    db.session.commit()