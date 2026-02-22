from datetime import datetime
from uuid import uuid4

from app.models import data_base

class Post(data_base.Model):
    id = data_base.Column(data_base.Integer, primary_key=True)
    uuid = data_base.Column(data_base.String(40), unique=True, nullable=False, default=lambda: str(uuid4()))

    user_id = data_base.Column(data_base.Integer, data_base.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    caption = data_base.Column(data_base.String(200))
    timestamp = data_base.Column(data_base.DateTime, default=datetime.now)

    medias = data_base.relationship('Media', backref='post', lazy=True, cascade='all, delete-orphan')

    likes = data_base.relationship('PostLike', back_populates='post', lazy='dynamic', cascade='all, delete-orphan')