from flask import redirect, session, url_for
from werkzeug.security import check_password_hash

from ..models import Doctor, Patient


def authenticate_user(email, password, role):
    """
    Authenticate a user (both patient and doctor).
    """
    if role == "patient":
        user = Patient.query.filter_by(email=email).first()
    elif role == "doctor":
        user = Doctor.query.filter_by(email=email).first()

    if user and check_password_hash(user.password, password):
        # store user session
        session["user_id"] = user.id
        session["role"] = role

        return True

    return False


# decorator to protect routes
def login_required(func):
    def wrap(*args, **kwargs):
        if not "user_id" in session:
            return redirect(url_for("main.login"))
        return func(*args, **kwargs)

    wrap.__name__ = func.__name__
    return wrap
