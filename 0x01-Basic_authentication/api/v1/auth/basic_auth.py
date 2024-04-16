#!/usr/bin/env python3
"""
Extend auth for basic authentication
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Extend basic authentication class"""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Extract the authentication string

        args:
            authorization_header: the auth string

        return: base64 authorization part
        """
        if authorization_header is None:
            return None
        if type(authorization_header) == "str":
            if authorization_header.startswith("Basic "):
                return authorization_header.lstrip("Basic ")
        else:
            return None
