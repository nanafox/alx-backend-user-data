#!/usr/bin/env python3

"""This module implements the Session Authentication mechanism."""
from typing import Union
from uuid import uuid4

from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """Implement Session Auth class."""

    user_id_by_session_id = {}  # keeps track of user sessions

    @staticmethod
    def create_session(user_id: str = None) -> Union[str, None]:
        """Create a session for the user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            None if the user ID is invalid, otherwise a session ID is returned.
        """
        if not user_id or not isinstance(user_id, str):
            return None

        session_id = str(uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id

        return session_id

    @staticmethod
    def user_id_for_session_id(session_id: str = None) -> Union[str, None]:
        """Return the User ID for the user who owns a give session ID.

        Args:
            session_id (str): The session ID presented by the user making
            the request.

        Returns:
            None if the session ID is invalid, or no such Session ID exists.
            Otherwise, the User ID for the given Session ID is returned.
        """
        if not session_id or not isinstance(session_id, str):
            return None

        return SessionAuth.user_id_by_session_id.get(session_id)
