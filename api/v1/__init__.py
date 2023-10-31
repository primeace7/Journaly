#!/usr/bin/env python3

from flask import Blueprint, session, g
from .bp_status import status_view
from .bp_login import login_view
from .bp_register import register_view
from ...models import storage
from .bp_journal_area import journal_area_view

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

app_views.register_blueprint(status_view)
app_views.register_blueprint(login_view)
app_views.register_blueprint(register_view)
app_views.register_blueprint(journal_area_view)

@app_views.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = storage.get('User', user_id)
