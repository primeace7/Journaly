#!/usr/bin/env python3
"""Implementation of all views that support the journaly app"""

from flask import Blueprint

status_view = Blueprint('app_views', __name__, url_prefix='/status')

@status_view.route('/')
def status():
    """return the status of the API server"""
    return {'status': 'OK'}
