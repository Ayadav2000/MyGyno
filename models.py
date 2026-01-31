
from . import db
from datetime import date

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password_hash = db.Column(db.String(200))
    role = db.Column(db.String(20))

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    MRN = db.Column(db.String(50), unique=True)
    age = db.Column(db.Integer)
    diagnosis = db.Column(db.String(120))
    doctor_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class Cycle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey("patient.id"))
    start_date = db.Column(db.Date)
    cycle_length = db.Column(db.Integer)
    is_irregular = db.Column(db.Boolean, default=False)

    def compute_irregular(self):
        self.is_irregular = self.cycle_length > 35
