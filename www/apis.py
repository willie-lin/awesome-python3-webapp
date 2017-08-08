#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/19 22:15
# @Author  : 林漠
# @Site    : 
# @File    : apis.py
# @Software: PyCharm

import json,logging,functools

class APIError(Exception):

    def __init__(self,error,data='',message=''):
        super(APIError,self).__init__(message)
        self.error = error
        self.data = data
        self.message = message


class APIValueRrror(APIError):

    def __init__(self,field,message=''):

        super(APIValueRrror,self).__init__('value:invalid',field,message)


class APIResourceNotFoundError(APIError):

        def __init__(self,field,message=''):
            super(APIResourceNotFoundError,self).__init__('value:notfound',field,message)


class APIPermissionError(APIError):

    def __init__(self,message=''):
        super(APIPermissionError,self).__init__('permission:forbidden','permission',message)
