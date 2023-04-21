from flask import Blueprint, jsonify

class Animal():
    def __init__(self, id, species, name, habitat):
        self.id = id
        self.species = species
        self.name = name
        self.habitat = habitat

sapphire_animals = [
    Animal(1, "Anaconda", "Nikki Minaj", "Jungle"),
    Animal(2, "Elephant", "Dumbo", "Our childhood!!!"),
    Animal(3, "Unicorn", "Not Charlie", "Youtube")
]

animals_bp = Blueprint("animals", __name__, url_prefix="/animals")

@animals_bp.route("", methods=['GET'])
def handle_animals():
    sapphire_animals_as_dict = [vars(animal) for animal in sapphire_animals]
    return jsonify(sapphire_animals_as_dict), 200

@animals_bp.route("/<animal_id>", methods=['GET'])
def handle_animal(animal_id):
    try:
        animal_id = int(animal_id)
    except:
        return {'msg': f"Invalid id '{animal_id}'"}, 400
    for animal in sapphire_animals:
        if animal.id == animal_id:
            return {
                'id': animal.id,
                'name': animal.name
            }, 200
    return {'msg': f"No animal with id {animal_id}"}, 404
