from flask import Blueprint, render_template, session
from .auth.config import login_required

# main blueprint routing
main = Blueprint("main", __name__)


# serve html template
@main.route("/")
def index():
    return render_template("login.html")


# Dashboard routes (protected)
@main.route("/patient-dashboard")
@login_required
def patient_dashboard():
    if "user_id" in session and session["role"] == "patient":
        return "Welcome to the Patient Dashboard!"  # load patient dashboard.
    return "Access Denied", 403


@main.route("/doctor-dashboard")
@login_required
def doctor_dashboard():
    if "user_id" in session and session["role"] == "doctor":
        return "Welcome to the Doctor Dashboard!"  # load doctor dashboard here
    return "Access Denied", 403
