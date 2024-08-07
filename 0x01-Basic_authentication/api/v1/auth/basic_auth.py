#!/usr/bin/env python3

"""This module implements the Basic Authentication mechanism."""
import base64
import binascii
from typing import Tuple, Union

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

    @staticmethod
    def decode_base64_authorization_header(
        base64_authorization_header: str,
    ):
        """Decode a base64 string."""
        if not base64_authorization_header or not isinstance(
            base64_authorization_header, str
        ):
            return None

        try:
            return base64.b64decode(
                base64_authorization_header.encode("utf-8")
            ).decode("utf-8")
        except binascii.Error:
            return None

    @staticmethod
    def extract_user_credentials(
        user_credentials: str,
    ) -> Union[Tuple[None, None], Tuple[str, str]]:
        """Extract the user credentials."""
        if not user_credentials or not isinstance(user_credentials, str):
            return None, None

        if ":" not in user_credentials:
            return None, None

        username, password = user_credentials.split(":", 1)

        return username, password
