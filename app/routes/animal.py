from flask import Blueprint, jsonify, abort, make_response, request
from app.models.animal import Animal
from app import db


def validate_animal(animal_id):
    try:
        animal_id = int(animal_id)
    except:
        abort(make_response({'msg': f"Invalid id '{animal_id}'"}, 400))

    # How do I get all of the animals from the DB?
    all_animals = Animal.query.all()

    for animal in all_animals:
        if animal.id == animal_id:
            return animal
    return abort(make_response({'msg': f"No animal with id {animal_id}"}, 404))

# All routes defined with animals_bp start with url_prefix (/animals)
animals_bp = Blueprint("animals", __name__, url_prefix="/animals")

@animals_bp.route("", methods=['GET'])
def handle_animals():
    # all_animals is a list of Animal instances! We should use them as Animal instances, and access their values via .
    all_animals = Animal.query.all()
    animals_response = []
    for animal in all_animals:
        animals_response.append({
            "id": animal.id,
            "name": animal.name
        })
    return jsonify(animals_response), 200

@animals_bp.route("/<animal_id>", methods=["GET"])
def handle_animal(animal_id):
    animal = validate_animal(animal_id)
    return {
        "id": animal.id,
        "name": animal.name
    }, 200

# POST to /animals
@animals_bp.route("", methods=['POST'])
def create_animal():
    # Get the name from the request body
    request_body = request.get_json()
    print(request_body)
    print("HELLOOOO????", request_body["name"])

    # Use it to make an Animal

    new_animal = Animal(name=request_body["name"])

    # Persist (save, commit) it in the database
    db.session.add(new_animal)
    db.session.commit()

    # Give back our response
    return {
        "id": new_animal.id,
        "name": new_animal.name,
        "for fun another thing": "Successfully created"
    }, 201
