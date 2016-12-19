from sanic import Sanic
from app.view import main
from app.ext import sa
import asyncio

# loop = asyncio.get_event_loop()
from app.ext import loop


def create_app():
    app = Sanic(__name__)
    app.loop = loop

    app.blueprint(main)
    return app
