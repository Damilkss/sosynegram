from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app.models import data_base

class User(data_base.Model, UserMixin):
    id = data_base.Column(data_base.Integer, primary_key=True)

    username = data_base.Column(data_base.String(20), nullable=True)
    password = data_base.Column(data_base.String(16), nullable=True)
    avatar = data_base.Column(data_base.String(40), nullable=True)

    posts = data_base.relationship('Post', backref='author', lazy=True)
    comments = data_base.relationship('Comment', backref='author', lazy=True)

    notifications = data_base.relationship(
        'Notification',
        foreign_keys='Notification.user_id',
        back_populates='user',
        lazy=True
    )
    sent_notifications = data_base.relationship(
        'Notification',
        foreign_keys='Notification.from_user_id',
        back_populates='from_user',
        lazy=True
    )

    following = data_base.relationship(
        'User',
        secondary='follows',
        primaryjoin="Follow.follower_id == User.id",
        secondaryjoin="Follow.followed_id == User.id",
        backref=data_base.backref('followers', lazy='dynamic'),
        lazy='dynamic'
    )

    def set_username(self, set_username: str):
        self.username = set_username

    def set_password(self, password: str):
        self.password = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password, password)