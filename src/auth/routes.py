from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash

from .. import db
from ..models import Doctor, Patient
from .config import authenticate_user

# blueprint for auth routing
auth = Blueprint("auth", __name__)


# registration for patients
@auth.route("/api/register/patient", methods=["POST"])
def register_patient():
    data = request.get_json()
    hashed_password = generate_password_hash(data["password"], method="sha256")
    new_patient = Patient(
        name=data["name"],
        age=data["age"],
        disease=data["disease"],
        email=data["email"],
        password=hashed_password,
    )
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({"message": "Patient registered successfully"}), 201


# registration for doctors
@auth.route("/api/register/doctor", methods=["POST"])
def register_doctor():
    data = request.get_json()
    hashed_password = generate_password_hash(data["password"], method="sha256")
    new_doctor = Doctor(
        name=data["name"],
        specialization=data["specialization"],
        email=data["email"],
        password=hashed_password,
    )
    db.session.add(new_doctor)
    db.session.commit()
    return jsonify({"message": "Doctor registered successfully"}), 201


# unified login for patients and doctors
@auth.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    role = data.get("role")  # either 'patient' or 'doctor'

    if authenticate_user(email, password, role):
        return jsonify({"message": f"{role.capitalize()} logged in successfully"}), 200
    return jsonify({"message": "Invalid credentials"}), 401
