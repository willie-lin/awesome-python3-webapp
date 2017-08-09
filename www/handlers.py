#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/7 23:03
# @Author  : 林漠
# @Site    : 
# @File    : handlers.py
# @Software: PyCharm
__author__ = 'Willie Lin'

import re,time,json,logging,hashlib,base64,asyncio

from www.coroweb import get,post
from www.models import User,Comment,Blog,next_id


@get('/')
def index(request):
    summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'

    blogs = [

        Blog(id='1',name='Test Blog',summary=summary,created_at = time.time()-120),
        Blog(id='2',name='Something New',summary = summary,created_at = time.time()-3600),
        Blog(id='3',name='Learn Switch',summary = summary,created_at = time.time()-7200)
    ]
    return {
        '__template__':'blogs.html',
        'blogs':blogs
    }

@get('/api/users')
def api_get_users():
    users = yield from User.findAll(orderBy='created_at desc')

    for u in users :
        u.passwd = '******'
    return dict(users=users)