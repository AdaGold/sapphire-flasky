from app import db

# "one" side, one Sanctuary has many Animals
class Sanctuary(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80))
    animals = db.relationship("Animal", back_populates="sanctuary")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

    @classmethod
    def from_dict(cls, sanctuary_details):
        new_sanctuary = cls(
            name=sanctuary_details["name"]
        )
        return new_sanctuary
