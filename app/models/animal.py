from app import db

# Inherits from the Model class! The model class is accessed through db...
class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80))
    species = db.Column(db.String(80))
    age = db.Column(db.Integer)

    # Given an instance of Animal, get list of caretakers with animal.caretakers
    caretakers = db.relationship("Caretaker", secondary="animal_caretaker", backref="animals")

    sanctuary_id = db.Column(db.Integer, db.ForeignKey('sanctuary.id'))
    sanctuary = db.relationship("Sanctuary", back_populates="animals")


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "species": self.species,
            "age": self.age,
            "sanctuary_id": self.sanctuary_id
        }

    @classmethod
    def from_dict(cls, animal_details):
        new_animal = cls(
            name=animal_details["name"],
            species=animal_details["species"],
            age=animal_details["age"],
            sanctuary_id=animal_details["sanctuary_id"]
        )
        return new_animal

