#!/usr/bin/env python3

"""This module implements the Basic Authentication mechanism."""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth class to manage the API authentication."""

    @staticmethod
    def extract_base64_authorization_header(authorization_header: str):
        """Return the value of the Authorization header."""
        if not authorization_header or not isinstance(
            authorization_header, str
        ):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[6:]
