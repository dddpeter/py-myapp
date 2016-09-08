# coding=utf-8
__author__ = 'lijinde-lhq'
from mongoengine import *

connect('mydb', host='localhost', port=27017)


class UserActivity(Document):
    vol_id = IntField(min_value=0, max_value=99999999999, required=True)
    opp_id = IntField(min_value=0, max_value=99999999999, required=True)
    vol_Time = DecimalField(min_value=0.00, max_value=999999999.99, precision=2, default=0.00)
    gettype = StringField(max_length=50)
    system_code = IntField(min_value=0, max_value=99999999999)
