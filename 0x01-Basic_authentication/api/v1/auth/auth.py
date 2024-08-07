#!/usr/bin/env python3

"""This module implements base class for Authentication mechanisms."""

from typing import List, TypeVar

User = TypeVar("User")


class Auth:
    """Auth class to manage the API authentication."""

    @staticmethod
    def require_auth(path: str, excluded_paths: List[str]) -> bool:
        """Require authentication for API paths except for excluded paths."""
        if not path or not excluded_paths:
            return True

        path = path.rstrip("/") + "/"

        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """Return the value of the Authorization header."""
        return None

    def current_user(self, request=None) -> User:
        """Return the current user."""
        return None
