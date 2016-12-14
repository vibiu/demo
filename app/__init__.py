from sanic import Sanic
from app.view import main


def create_app():
    app = Sanic(__name__)

    app.blueprint(main)
    return app
