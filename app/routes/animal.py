from flask import Blueprint, jsonify, abort, make_response, request
from app.models.animal import Animal
from app import db

def validate_animal(animal_id):
    try:
        animal_id = int(animal_id)
    except:
        abort(make_response({'msg': f"Invalid id '{animal_id}'"}, 400))

    animal = Animal.query.get(animal_id)

    return animal if animal else abort(make_response({'msg': f"No animal with id {animal_id}"}, 404))


# All routes defined with animals_bp start with url_prefix (/animals)
animals_bp = Blueprint("animals", __name__, url_prefix="/animals")

@animals_bp.route("", methods=['GET'])
def handle_animals():
    name_query = request.args.get("name")
    if name_query:
        animals = Animal.query.filter_by(name=name_query)
    else:
        animals = Animal.query.all()
    animals_response = []
    for animal in animals:
        animals_response.append(animal.to_dict())
    return jsonify(animals_response), 200


@animals_bp.route("", methods=['POST'])
def create_animal():
    # Get the data from the request body
    request_body = request.get_json()

    # Use it to make an Animal
    new_animal = Animal(
        name=request_body["name"],
        species=request_body["species"],
        age=request_body["age"]
    )

    # Persist (save, commit) it in the database
    db.session.add(new_animal)
    db.session.commit()

    # Give back our response
    return {
        "id": new_animal.id,
        "name": new_animal.name,
        "msg": "Successfully created"
    }, 201


@animals_bp.route("/<animal_id>", methods=["GET"])
def handle_animal(animal_id):
    animal = validate_animal(animal_id)
    return animal.to_dict(), 200

@animals_bp.route("/<animal_id>", methods=["PUT"])
def update_one_animal(animal_id):
    request_body = request.get_json()
    animal_to_update = validate_animal(animal_id)
    
    animal_to_update.name = request_body["name"]
    animal_to_update.species = request_body["species"]
    animal_to_update.age = request_body["age"]

    db.session.commit()
    
    return animal_to_update.to_dict(), 200


@animals_bp.route("/<animal_id>", methods=["DELETE"])
def delete_one_animal(animal_id):
    animal_to_delete = validate_animal(animal_id)

    db.session.delete(animal_to_delete)
    db.session.commit()

    return f"Animal {animal_to_delete.name} is deleted!", 200


