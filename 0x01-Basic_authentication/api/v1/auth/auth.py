#!/usr/bin/env python3
"""
Model for basic authentication
"""
from flask import Request
from typing import List, TypeVar


class Auth:
    """class for basic authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Validate if path requiers authentication

        args:
            path: path to validate
            excluded_paths: paths that don't require authentication

        return: True if path requires authentication else False
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        for url in excluded_paths:
            if path.rstrip("/") == url.rstrip("/"):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieve request header

        args:
            request: flask request object

        return: request authorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar("User"):
        """
        Retrieve request user

        args:
            request: flask request object

        return: user
        """
        return None
