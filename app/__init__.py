"""Main entry."""

import os
from flask import Flask
from flask_restaction import Api, TokenAuth, abort
from .configs import configs
from .dependency import db, d
from . import views


class Test:

    def get_400(self):
        abort(400, "BadRequest", "bad request")

    def get_500(self):
        abort(500, "ServerError", "internal server error")

    def get_502(self):
        raise ValueError("test 502")

ALL_RESOURCE = [getattr(views, x) for x in dir(views) if x[:1].isupper()]
ALL_RESOURCE.append(Test)


def get_role(token):
    return 'guest'


def check_role(token, roles):
    token = d.auth.decode_token(token)
    role = get_role(token)
    return role in roles

d.check_role = check_role


def create_app(config=None):
    app = Flask(__name__)

    if config is None:
        config = os.environ.get('FLASK_CONFIG', 'default')
        config = configs[config]
        app.config.from_object(config)
        config_api(app)
        db.init_app(app)
        return app


def config_api(app):
    api = Api(app, metafile='meta.json', docs=__doc__)
    auth = TokenAuth(api)
    auth.get_role(get_role)
    d.auth = auth
    app.route('/')(api.meta_view)

    for x in ALL_RESOURCE:
        api.add_resource(x)
