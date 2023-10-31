#!/usr/bin/env python3
"""Implementation of login utility the journaly app"""

from flask import request, render_template, g, session, Blueprint
from werkzeug.security import check_password_hash
from .utilities import fetch_user

login_view = Blueprint('login_view', __name__, url_prefix='/login')

@login_view.route('/<username>/<password>', methods=['GET', 'POST'])
def login(username, password):
    """return the login view or the journals area depending on the rquest type"""
    if request.method == 'POST':
        #username_email = request.form['username']
        #password = request.form['password']
        error = None

        user = fetch_user(username) #fetch the user from database
        if not user:
            error = 'Invalid username or email. Please check and try again.'
        elif password != user.password: #not check_password_hash(user.password, password):
            error = 'Invalid password. Please check and try agina.'

        if not error:
            #session.clear()
            #session['user_id'] = user.id
            return 'User found' # redirect(url_for('journal_area'))

        #flash(error)
        return error

#    return render_template('login.html')
