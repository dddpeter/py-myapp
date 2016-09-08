# coding=utf-8
__author__ = 'lijinde-lhq'
from mongoengine import *

connect('mydb', host='localhost', port=27017)


class UserOrgan(Document):
    org_id = IntField(min_value=0, max_value=99999999999, required=True)
    org_name = StringField(max_length=100)
    vol_id = IntField(min_value=0, max_value=99999999999, required=True)
    system_code = IntField(min_value=0, max_value=99999999999)
