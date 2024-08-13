#!/usr/bin/env python3

"""App module."""
import os
from typing import Tuple

from flask import Flask, Response, abort, jsonify, request

from auth import Auth

AUTH = Auth()
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/", methods=["GET"])
def root():
    """API Root."""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def signup() -> Tuple[Response, int]:
    """Register new user."""
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        AUTH.register_user(email=email, password=password)
    except ValueError as err:
        err_msg = str(err)
        if "already exists" in err_msg:
            return jsonify({"message": "email already registered"}), 400
        return jsonify({"message": err_msg}), 400

    return jsonify({"email": email, "message": "user created"}), 201


@app.route("/sessions", methods=["POST"])
def login():
    """User login endpoint.

    This endpoint accepts and logs user into the system if the credentials
    provided are valid. In the event of invalid data, the user receives an
    authorization error with the code 401.

    Upon successful login, a session is created for the authenticated user.
    """
    email = request.form.get("email")
    password = request.form.get("password")

    if not AUTH.valid_login(email=email, password=password):
        abort(401)

    session_id = AUTH.create_session(email=email)
    data = jsonify({"email": email, "message": "logged in"})
    data.set_cookie(key="session_id", value=session_id)

    return data


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=os.getenv("DEBUG") == "True")
