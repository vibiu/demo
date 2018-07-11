import re
import json
import random
import asyncio
from urllib import parse

import websockets

# dict to save all connection object
socket_conns = dict()


async def heandler(websocket, path):
    await asyncio.sleep(3)
    parser = parse(path)
    query = parse.parse_qs(parser.query)
    token = query.get('token')

    if token:
        # Connection established
        socket_conns[token] = websocket
        print('connection: token={} established'.format(token))

        # Send msgs
        while 1:
            await asyncio.sleep(2)
            # Receive new message
            msg = get_new_message(token)

            if msg:
                print('get new message!')
                current_conn = socket_conns.get(token)
                if current_conn.open:
                    # Send message
                    await current_conn.send(json.dumps(msg))
                    print('message send.')
                else:
                    print('user not connected.')
            else:
                print('no new message.')
                socket_set = set()
                for token, conn in socket_conns.items():
                    if not conn.open:
                        conn.close()
                        socket_set.add(token)
                for conn in socket_set:
                    # Pop from socket dict
                    socket_conns.pop(conn, None)
                # All socket connection is closed
                if not socket_conns:
                    break
    else:
        websocket.close()
        print('No token in path.')
    print('websocket connection break...')


def get_new_message(token):
    mock_message = {'message': 'your token is {}'.format(token)}
    return random.choice([mock_message, None])


host = '0.0.0.0'
port = 8000
server = websockets.serve(heandler, host, port)

asyncio.get_event_loop().run_until_complete(server)
print('websocket server is running on host:{}, port: {}'.format(host, port))
asyncio.get_event_loop().run_forever()
