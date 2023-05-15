from flask import Blueprint, jsonify, request
from app.models.caretaker import Caretaker
from app.models.animal import Animal
from app import db
from app.routes.routes_helper import get_valid_item_by_id

caretaker_bp = Blueprint("caretaker", __name__, url_prefix="/caretakers")

@caretaker_bp.route("", methods=['GET'])
def get_caretakers():
    caretakers = Caretaker.query.all()
    caretaker_response = []
    for caretaker in caretakers:
        caretaker_response.append({
            "id": caretaker.id,
            "name": caretaker.name
        })
    return jsonify(caretaker_response), 200


@caretaker_bp.route("", methods=['POST'])
def create_caretaker():
    request_body = request.get_json()
    new_caretaker = Caretaker(
        name=request_body["name"]
    )
    db.session.add(new_caretaker)
    db.session.commit()
    return {
        "id": new_caretaker.id,
        "name": new_caretaker.name,
        "msg": "Successfully created"
    }, 201

@caretaker_bp.route("/<caretaker_id>/animals", methods=['POST'])
def create_animal_for_caretaker(caretaker_id):
    request_body = request.get_json()
    new_animal = Animal.from_dict(request_body)
    caretaker = get_valid_item_by_id(Caretaker, caretaker_id)

    new_animal.caretakers.append(caretaker)

    db.session.add(new_animal)
    db.session.commit()

    caretakers = []
    for caretaker in new_animal.caretakers:
        caretakers.append({
            "caretaker": {
                "id": caretaker.id,
                "name": caretaker.name
            }
        })

    # # Give back our response
    return {
        "id": new_animal.id,
        "name": new_animal.name,
        "caretakers": caretakers,
        "msg": "Successfully created"
    }, 201

@caretaker_bp.route("/<caretaker_id>/animals", methods=['GET'])
def get_animals_for_caretaker(caretaker_id):
    caretaker = get_valid_item_by_id(Caretaker, caretaker_id)
    animals = []

    for animal in caretaker.animals:
        animals.append(animal.to_dict())

    return {
        "id": caretaker.id,
        "name": caretaker.name,
        "animals": animals
    }, 200
