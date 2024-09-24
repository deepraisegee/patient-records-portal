from flask import Blueprint, jsonify, request, render_template, session
from . import db
from .models import Patient, Doctor
from .auth.routes import authenticate_user
from werkzeug.security import generate_password_hash

# Create a Blueprint for routing
main = Blueprint("main", __name__)


# Serve the HTML template
@main.route("/")
def index():
    return render_template("index.html")


# Dashboard routes (protected)
@main.route("/patient-dashboard")
def patient_dashboard():
    if "user_id" in session and session["role"] == "patient":
        return "Welcome to the Patient Dashboard!"
    return "Access Denied", 403


@main.route("/doctor-dashboard")
def doctor_dashboard():
    if "user_id" in session and session["role"] == "doctor":
        return "Welcome to the Doctor Dashboard!"
    return "Access Denied", 403
