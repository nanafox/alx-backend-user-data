#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from typing import Dict, Tuple

from flask import Flask, jsonify
from flask_cors import CORS

from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.errorhandler(404)
def not_found(_) -> Tuple[Dict, int]:
    """Not found handler"""
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(_) -> Tuple[Dict, int]:
    """Unauthorized error handler."""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(_) -> Tuple[Dict, int]:
    """Forbidden API operation handler."""
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port, debug=getenv("DEBUG", False))
