from flask import Flask, jsonify, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from twopi_flask_utils.deployment_release import get_release
from lib.trello import TrelloClient

from .views import IndexView

import models

from models import User
from flask_login import LoginManager

from requests_oauthlib import OAuth1Session


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)

    app.db = SQLAlchemy(app)
    app.db.register_base(models.Base)

    login_manager = LoginManager(app)

    # Register a user loader
    @login_manager.user_loader
    def load_user(user_id):
        return app.db.session.query(User).get(user_id)

    # Flask Migrate
    Migrate(app, app.db)

    # Endpoints
    add_healthcheck(app)

    # App Version
    app.version = get_release()


    # Trello API
    app.trello = TrelloClient(api_key=app.config.get('TRELLO_APP_KEY'))

    # Register Views
    IndexView.register(app, route_base='/')


    return app


def add_healthcheck(app):
    @app.route('/healthcheck')
    def healthcheck():
        return jsonify({
            'status': 'running',
            'version': current_app.version,
        }), 200

