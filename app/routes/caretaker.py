from flask import Blueprint, jsonify, request
from app.models.caretaker import Caretaker
from app import db

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
