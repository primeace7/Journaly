#!/usr/bin/env python3

from flask import Blueprint
from .bp_status import status_view
from .bp_login import login_view

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

app_views.register_blueprint(status_view)
app_views.register_blueprint(login_view)
