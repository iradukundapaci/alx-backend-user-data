#!/usr/bin/env python3
"""
Password Encryption
"""
import bcrypt


def hash_password(password: str) -> str:
    """
    Function to hash password

    arg:
        password: unhashed password

    return: hashed password byte string
    """
    return bcrypt.hashpw(bytes(password.encode("utf-8")), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Function to validate passed password

    arg:
        hashed_password: hashed password
        password: password to vlidate

    return: True if password is valid
    """
    if bcrypt.checkpw(bytes(password.encode("utf-8")), hashed_password):
        return True
    return False
