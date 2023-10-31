#!/usr/bin/env python3
from flask import Flask
from .v1 import app_views

app = Flask(__name__)
app.config['SECRET_KEY'] = '4c3a3c07cbf2e61d51ec6803938e60de'

app.register_blueprint(app_views)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001', threaded=True, debug=True)

