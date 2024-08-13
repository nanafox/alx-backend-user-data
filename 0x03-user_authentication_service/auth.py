#!/usr/bin/env python3

"""Auth module."""

import bcrypt
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Hash plaintext passwords."""
    return bcrypt.hashpw(password=password.encode(), salt=bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        """Initialize the Auth object."""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user with the provided email and password.

        Args:
            email (str): The email address of the user to register.
            password (str): The plaintext password of the user to register.

        Raises:
            ValueError: If the email or password is missing, or if the user
             already exists.

        Returns:
            User: The newly registered user object.
        """
        if not email:
            raise ValueError("email missing")
        if not password:
            raise ValueError("password missing")

        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            pass
        else:
            raise ValueError(f"User {email} already exists")

        hashed_password = _hash_password(password=password).decode()
        return self._db.add_user(email=email, hashed_password=hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """Validate user login credentials.

        Args:
            email (str): The email address of the user attempting to log in.
            password (str): The plaintext password of the user attempting to
             log in.

        Returns:
            bool: True if the login credentials are valid, False otherwise.
        """
        try:
            db_user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        return bcrypt.checkpw(
            password=password.encode(),
            hashed_password=db_user.hashed_password.encode(),
        )
