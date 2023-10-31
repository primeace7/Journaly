#!/usr/bin/env python3
"""Implementation a status view for checking the status of the API service"""

from flask import Blueprint

status_view = Blueprint('app_views', __name__, url_prefix='/status')

@status_view.route('/')
def status():
    """return the status of the API server"""
    return {'status': 'OK'}
