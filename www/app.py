#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/6 0:05
# @Author  : 林漠
# @Site    : 
# @File    : app.py
# @Software: PyCharm

# __author__ = 'Willie Lin'
#
# async web application.

from datetime import datetime

import logging;

logging.basicConfig(level=logging.INFO)
import asyncio
from aiohttp import web


def index(request):
    return web.Response(body=b'<h5>I LOVE GAKKI</h5>')


@asyncio.coroutine
async def init(loop):
    app = web.Application(loop=loop)

    app.router.add_route('GET', '/', index)

    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)

    logging.info('server started at http://127.0.0.1:9000...')

    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
