import os
import datetime
import asyncio
import uvloop
from aiopg.sa import create_engine
import sqlalchemy as sa


database_name = 'test'
database_host = '127.0.0.1'
database_user = 'vibiu'
database_password = 'password'

# connection = 'postgres://{0}:{1}@{2}/{3}'.format(
#     database_user,
#     database_password,
#     database_host,
#     database_name)
connection = 'sqlite:///test.db'

metadata = sa.MetaData()


async def get_engine():
    return await create_engine(connection)

loop = asyncio.get_event_loop()
engine = loop.run_until_complete(get_engine())

polls = sa.Table(
    'sanic_polls', metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('question', sa.String(50)),
    sa.Column("pub_date", sa.DateTime))


async def prepare_db():
    async with engine.acquire() as conn:
        await conn.execute('DROP TABLE IF EXIST sanic_polls')
        await conn.execute("""CREATE TABLE sanic_polls (
                                        id serial primary key,
                                        question varchar(50),
                                        pub_date timestamp
                                    );""")

        for i in range(0, 100):
            await conn.execute(
                poll.insert().values(question=i,
                                     pub_date=datetime.datetime.now())
            )
