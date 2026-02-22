from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import CSRFProtect

data_base = SQLAlchemy()
login_manager = LoginManager()
csrf_protect = CSRFProtect()

from .auth import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))