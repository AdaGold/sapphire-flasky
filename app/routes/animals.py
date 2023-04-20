from flask import Blueprint, jsonify

animals_bp = Blueprint("animals", __name__, url_prefix="/animals")

@animals_bp.route("", methods=['GET'])
def handle_animals():
    return "Hello Sapphire!"
