from flask import Blueprint, jsonify, abort, make_response, request
from app import db

from app.models.sanctuary import Sanctuary
from app.routes.routes_helper import get_valid_item_by_id

sanctuaries_bp = Blueprint("sanctuaries", __name__, url_prefix="/sanctuaries")

@sanctuaries_bp.route("", methods=['GET'])
def handle_sanctuaries():
    name_query = request.args.get("name")
    if name_query:
        sanctuaries = Sanctuary.query.filter_by(name=name_query)
    else:
        sanctuaries = Sanctuary.query.all()

    sanctuaries_response = []
    for sanctuary in sanctuaries :
        sanctuaries_response.append(sanctuary.to_dict())
    return jsonify(sanctuaries_response), 200


@sanctuaries_bp.route("", methods=['POST'])
def create_sanctuary():
    request_body = request.get_json()
    new_sanctuary = Sanctuary.from_dict(request_body)

    db.session.add(new_sanctuary)
    db.session.commit()

    # Give back our response
    return {
        "id": new_sanctuary.id,
        "name": new_sanctuary.name,
        "msg": "Successfully created"
    }, 201


@sanctuaries_bp.route("/<sanctuary_id>", methods=["PUT"])
def update_one_sanctuary(sanctuary_id):
    request_body = request.get_json()
    sanctuary_to_update = get_valid_item_by_id(Sanctuary, sanctuary_id)

    sanctuary_to_update.name = request_body["name"]

    db.session.commit()

    return sanctuary_to_update.to_dict(), 200


@sanctuaries_bp.route("/<sanctuary_id>", methods=["DELETE"])
def delete_one_sanctuary(sanctuary_id):
    sanctuary_to_delete = get_valid_item_by_id(Sanctuary, sanctuary_id)

    db.session.delete(sanctuary_to_delete)
    db.session.commit()

    return f"Sanctuary {sanctuary_to_delete.name} is deleted!", 200

@sanctuaries_bp.route("/<sanctuary_id>", methods=['GET'])
def handle_one_sanctuary(sanctuary_id):
    sanctuary = get_valid_item_by_id(Sanctuary, sanctuary_id)
    return sanctuary.to_dict(), 200


@sanctuaries_bp.route("/<sanctuary_id>/animals", methods=['GET'])
def handle_all_animals_of_one_sanctuary(sanctuary_id):
    sanctuary = get_valid_item_by_id(Sanctuary, sanctuary_id)

    animals_response = []
    for animal in sanctuary.animals:
        animals_response.append(animal.to_dict())

    return jsonify(animals_response), 200
