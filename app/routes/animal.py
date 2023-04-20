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
    Animal(3, "Unicorn", "Charlie", "Youtube")
]

animals_bp = Blueprint("animals", __name__, url_prefix="/animals")

@animals_bp.route("", methods=['GET'])
def handle_animals():
    sapphire_animals_as_dict = [vars(animal) for animal in sapphire_animals]
    return jsonify(sapphire_animals_as_dict), 200
