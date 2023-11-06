#!/usr/bin/env python3
"""Implementation of login utility the journaly app"""

from flask import request, render_template, g, session, Blueprint
from werkzeug.security import check_password_hash
from .utilities import fetch_user

login_view = Blueprint('login_view', __name__, url_prefix='/login')

@login_view.route('/', methods=['POST'])
def login():
    """return the login view or the journals area
    depending on the rquest type"""
    if request.method == 'POST':
        data = request.json
        username_email = data['username_email']
        password = data['password']
        error = None

        user = fetch_user(username_email) #fetch the user from database
        if not user:
            error = {'Error': 'Invalid username or email'}, 401
        elif not check_password_hash(user.password, password):
            error = {'Error': 'Invalid password'}, 401

        if not error:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('journal_area', username=user.username))

        return {'Error': 'There was an error'}, 405
