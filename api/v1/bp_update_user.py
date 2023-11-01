#!/usr/bin/env python3
"""Implementation of /<username> endpoint that allows a user to modify
their data"""

from flask import request, g, session, Blueprint
from werkzeug.security import check_password_hash, generate_password_hash
from .utilities import fetch_user

update_user_view = Blueprint('update_user_view', __name__)

@update_user_view.route('/<username>', methods=['PATCH'])
def update_user(username):
    """update a user's data"""
    if not g.user:
        return redirect(url_for('login'))

    data = request.json

    user = g.user
    for item in data:
        if item == 'new_password':
            if not check_password_hash(user.password, data['old_password']):
                return {'Error': 'wrong old password'}, 400
            user.password = generate_password_hash(item)
        elif item in ['username', 'email', 'firstname', 'lastname']:
            setattr(user, item)

    session.clear()
    return redirect(url_for('login'))
