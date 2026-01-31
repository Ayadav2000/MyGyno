
from flask import Blueprint, jsonify
from ..models import Patient, Cycle

api_bp = Blueprint("api", __name__)

@api_bp.route("/patient/<mrn>")
def get_patient(mrn):
    p = Patient.query.filter_by(MRN=mrn).first_or_404()
    return jsonify({"resourceType":"Patient","id":p.MRN})
