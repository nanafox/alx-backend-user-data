#!/usr/bin/env python3

"""DB module."""

from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

# noinspection PyCompatibility
from user import Base, User


class DB:
    """DB class."""

    def __init__(self) -> None:
        """Initialize a new DB instance."""
        echo = getenv("ECHO") == "True"

        self._engine = create_engine("sqlite:///a.db", echo=echo)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object."""
        if self.__session is None:
            db_session = sessionmaker(bind=self._engine)
            self.__session = db_session()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Create and save a new user to the database.

        Args:
            email (str): The email of the user.
            hashed_password (str): A secure and safe password for the user.

        Returns:
            User: A new user object is returned on success.
        """
        db_user = User(email=email, hashed_password=hashed_password)
        self._session.add(db_user)
        self._session.commit()
        return db_user
