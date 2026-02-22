from app import data_base

class Media(data_base.Model):
    id = data_base.Column(data_base.Integer, primary_key=True)
    post_id = data_base.Column(data_base.Integer, data_base.ForeignKey('post.id', ondelete='CASCADE'), nullable=False)

    type = data_base.Column(data_base.String(10), nullable=False)

    file_path = data_base.Column(data_base.String(200), nullable=False)
    order = data_base.Column(data_base.Integer, default=0)