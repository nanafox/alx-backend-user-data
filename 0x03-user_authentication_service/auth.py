#!/usr/bin/env python3

"""Auth module."""

import bcrypt


def _hash_password(password: str) -> bytes:
    """Hash plaintext passwords."""
    return bcrypt.hashpw(password=password.encode(), salt=bcrypt.gensalt())
