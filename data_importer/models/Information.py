__author__ = 'lijinde-lhq'
import json
import datetime


class Information(object):
    def __init__(self, title, content, author='unknow', date=datetime.datetime.now()):
        self.title = title
        self.content = content
        self.author = author
        self.date = date


class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)