#!/usr/bin/env python3
"""Implementation of logout utility for the journaly app"""

from flask import redirect, g, session, Blueprint

logout_view = Blueprint('logout_view', __name__, url_prefix='/logout')

@logout_view.route('/', methods=['GET'])
def logout():
    """log the user out and return the login view"""
    session.clear()
    g.user = None
    return redirect(url_for('login'))
