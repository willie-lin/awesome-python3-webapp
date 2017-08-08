#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/7 23:33
# @Author  : 林漠
# @Site    : 
# @File    : config_default.py
# @Software: PyCharm
'''
Default configurations.
'''

configs = {
    'debug': True,
    'db': {
        'host':'127.0.0.1',
        'port': 3306,
        'user':'www',
        'password':'www',
        'db':'awesome'
    },
    'session':{
        'secret':'Awesome'
    }
}