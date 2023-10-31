#!/usr/bin/env python3
"""Implement utility functions required by the app views"""
from ...models import storage


def fetch_user(username_email):
    """fetch a user object from the database. 

    Args:
        username_email (str): A user's username or password that will be checked
            against the details of the users in the database.

    Returns (object): a user object, or None if user doesn't exist
    """
    all_users = storage.all('User') #storage.all return a list of dicts

    found = None
    for user in all_users:
        obj = list(user)[0]
        if obj.username == username_email or\
           obj.email == username_email:
            return obj
    return found
