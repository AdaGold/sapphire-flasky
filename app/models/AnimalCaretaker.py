from app import db

class AnimalCaretaker(db.Model):
    __tablename__ = "animal_caretaker"
    animal_id = db.Column(db.Integer, db.ForeignKey('animal.id'), primary_key=True,nullable=False)
    caretaker_id = db.Column(db.Integer, db.ForeignKey('caretaker.id'), primary_key=True,nullable=False)
