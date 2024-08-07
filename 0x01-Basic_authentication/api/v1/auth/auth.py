#!/usr/bin/env python3

"""This module implements base class for Authentication mechanisms."""

from typing import List, TypeVar

User = TypeVar("User")


class Auth:
    """Auth class to manage the API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require authentication for API paths except for excluded paths."""
        return False

    def authorization_header(self, request=None) -> str:
        """Return the value of the Authorization header."""
        return None

    def current_user(self, request=None) -> User:
        """Return the current user."""
        return None
