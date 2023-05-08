from app import db

# "one" side, one Sanctuary has many Animals
class Sanctuary(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80))
    animals = db.relationship("Animal", back_populates="sanctuary")

