import os

from flask import Flask

from .config import Config

from .models import data_base
from .models import login_manager
from .models import csrf_protect

from .routes import feed_blueprint
from .routes import auth_blueprint

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    data_base.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page.'

    csrf_protect.init_app(app)

    app.register_blueprint(feed_blueprint)
    app.register_blueprint(auth_blueprint)

    with app.app_context():
        data_base.create_all()

        os.makedirs(app.config['STORAGE_PATH'], exist_ok=True)
        os.makedirs(app.config['MEDIAS_PATH'], exist_ok=True)
        os.makedirs(app.config['AVATARS_PATH'], exist_ok=True)

    return app