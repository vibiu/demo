from sanic import Blueprint
from sanic.response import json
import uvloop
from app.ext import enginer
from app import model
import asyncio
from aiomysql.sa import create_engine

name = 'asyncdb'
host = '121.42.195.83'
user = 'vibiu'
password = '^6180339$'
port = 3306

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

loop = asyncio.get_event_loop()
# from app import loop


main = Blueprint(__name__)


@main.route('/')
async def index(request):
    return json({'message': 'index'})


@main.route('/sql')
async def sql(request):
    print('helo')

    engine = loop.run_until_complete(enginer())
    # engine = await create_engine(host=host,
    #                              port=port, user=user,
    #                              password=password,
    #                              db=name,
    #                              loop=loop)
    # async with enginer() as engine:
    async with engine.acquire() as conn:
        print('helo')
        result = await conn.execute(model.tbl.select())
        print(result)
    return json({'message': 'execute sql'})
