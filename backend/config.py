import datetime, os
from twopi_flask_utils.config import build_url

class Config(object):
    SECRET_KEY = 'development-only'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    AUTH_TOKEN_EXPIRE_AFTER = datetime.timedelta(days=90)

    TRELLO_APP_KEY = '1b6101fea3f9607e50f1171610d776ce'

class Development(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres@127.0.0.1/dev_trello_scheduled'
    AUTH_TOKEN_EXPIRE_AFTER = datetime.timedelta(days=365)


class Production(Config):
    PROPAGATE_EXCEPTIONS = True

    def __init__(self):
        self.SECRET_KEY = os.environ['SECRET_KEY']

        self.SQLALCHEMY_DATABASE_URI = build_url(
            os.environ['DATABASE_URL'], 
            scheme='postgres')


def get_config():
    import os
    cfg_cls = os.environ.get('CONFIG_CLASS', 'Development')
    if cfg_cls == 'Development':
        return Development()
    else:
        return Production()

