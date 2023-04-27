from app import db

# Inherits from the Model class! The model class is accessed through db...
class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }