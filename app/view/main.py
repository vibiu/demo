from sanic import Blueprint
from sanic.response import json


main = Blueprint(__name__)


@main.route('/')
async def index(request):
    return json({'message': 'index'})
