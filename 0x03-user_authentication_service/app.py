#!/usr/bin/env python3

"""App module."""
import os
from typing import Dict, Tuple

from flask import Flask, jsonify, request

from auth import Auth

AUTH = Auth()
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/", methods=["GET"])
def root():
    """API Root."""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def signup() -> Tuple[Dict[str, str], int]:
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=os.getenv("DEBUG") == "True")
