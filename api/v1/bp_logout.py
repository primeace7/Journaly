#!/usr/bin/env python3
"""Implementation of logout utility for the journaly app"""

from flask import redirect, g, session, Blueprint, url_for

logout_handler = Blueprint('logout_handler', __name__, url_prefix='/logout')

@logout_handler.route('/', methods=['GET'])
def logout():
    """log the user out and return the login view"""
    session.clear()
    g.user = None
    return redirect(url_for('app_views.login_handler.login'))
