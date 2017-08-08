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
'''
async web application.
'''
import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web
from jinja2 import Environment, FileSystemLoader

from config import configs