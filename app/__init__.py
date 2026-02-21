import os

from flask import Flask

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.update(os.environ.items())



    return app