# import os
# import datetime
# import asyncio
# import uvloop
# from aiopg.sa import create_engine
# import sqlalchemy as sa
# from aiomysql import create_engine


# database_name = 'asyncdb'
# database_host = '121.42.195.83'
# database_user = 'vibiu'
# database_password = '^6180339$'

# # connection = 'postgres://{0}:{1}@{2}/{3}'.format(
# #     database_user,
# #     database_password,
# #     database_host,
# #     database_name)
# connection = 'sqlite:///test.db'

# metadata = sa.MetaData()


# async def get_engine():
#     return await create_engine(connection)

# loop = asyncio.get_event_loop()
# engine = loop.run_until_complete(get_engine())

# polls = sa.Table(
#     'sanic_polls', metadata,
#     sa.Column('id', sa.Integer, primary_key=True),
#     sa.Column('question', sa.String(50)),
#     sa.Column("pub_date", sa.DateTime))


# async def prepare_db():
#     async with engine.acquire() as conn:
#         await conn.execute('DROP TABLE IF EXIST sanic_polls')
#         await conn.execute("""CREATE TABLE sanic_polls (
#                                         id serial primary key,
#                                         question varchar(50),
#                                         pub_date timestamp
#                                     );""")

#         for i in range(0, 100):
#             await conn.execute(
#                 poll.insert().values(question=i,
#                                      pub_date=datetime.datetime.now())
#             )


# >>>>>>>>>>>>>>

# import asyncio
# from aiomysql import create_pool

# name = 'asyncdb'
# host = '121.42.195.83'
# user = 'vibiu'
# password = '^6180339$'
# port = 3306

# loop = asyncio.get_event_loop()


# async def go():
#     # print('hello')
#     pool = await create_pool(
#         host=host,
#         port=port, user=user,
#         password=password,
#         db=name,
#         loop=loop)
#     # pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
#     #                                   user='root', password='',
#     #                                   db='mysql', loop=loop)
#     # import pdb;pdb.set_trace()
#     print('hi')
#     async with pool.acquire() as conn:
#         async with conn.cursor() as cur:
#             await cur.execute('SELECT 42;')
#             value = await cur.fetchone()
#             print(value)
#             assert value[0] == 42
#     pool.close()
#     await pool.wait_closed()


# loop.run_until_complete(go())

import asyncio
import uvloop
import sqlalchemy as sa
from aiomysql.sa import create_engine

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


# asyncio.set_event_loop(uvloop.get_event_loop())

name = 'asyncdb'
host = '121.42.195.83'
user = 'vibiu'
password = '^6180339$'
port = 3306
loop = asyncio.get_event_loop()


metadata = sa.MetaData()

tbl = sa.Table('tbl', metadata,
               sa.Column('id', sa.Integer, primary_key=True),
               sa.Column('val', sa.String(255)))


async def go():
    engine = await create_engine(host=host,
                                 port=port, user=user,
                                 password=password,
                                 db=name,
                                 loop=loop)
    async with engine.acquire() as conn:
        # await conn.execute('''CREATE TABLE tbl (
        #     id serial PRIMARY KEY,
        #     val varchar(255));''')
        await conn.execute(tbl.insert().values(val='abc'))
        await conn.execute(tbl.insert().values(val='xyz'))
        async for row in conn.execute(tbl.select()):
            print(row.id, row.val)
    engine.close()
    await engine.wait_closed()


# class enginer():

#     def __init__(self):

#         self.engine = await create_engine(
#             host=host,
#             port=port, user=user,
#             password=password,
#             db=name,
#             loop=loop)
#         # return self.engine

#     async def __aexit__(self):
#         self.engine.close()
#         await self.engine.wait_closed()


async def enginer():
    engine = await create_engine(host=host,
                                 port=port, user=user,
                                 password=password,
                                 db=name,
                                 loop=loop)
    return engine

if __name__ == '__main__':
    loop.run_until_complete(go())
