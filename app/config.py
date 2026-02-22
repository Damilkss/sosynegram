import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = '4b72ac4e-3972-44dd-816d-6d371e7b705f'

    STORAGE_PATH = os.path.join(basedir, 'storage')
    MEDIAS_PATH = os.path.join(STORAGE_PATH, 'medias')
    AVATARS_PATH = os.path.join(STORAGE_PATH, 'avatars')

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(STORAGE_PATH, 'storage.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False