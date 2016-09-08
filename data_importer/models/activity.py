# coding=utf-8
__author__ = 'lijinde-lhq'
from mongoengine import *

connect('mydb', host='localhost', port=27017)


class Activity(Document):
    opp_id = IntField(min_value=0, max_value=99999999999, required=True)
    opp_name = StringField(max_length=200, required=True)
    org_name = StringField(max_length=200)
    org_ID = IntField(min_value=0, max_value=99999999999, required=True)
    opp_start_date = DateTimeField()
    opp_end_date = DateTimeField()
    opp_lng = DecimalField(min_value=-180.00, max_value=180.00, precision=6)
    opp_lat = DecimalField(min_value=-90.00, max_value=90.00, precision=6)
    opp_linkman = StringField(max_length=50, required=True)
    opp_linkman_mobile = IntField(min_value=10000000000, max_value=99999999999, required=True)
    opp_linkman_email = StringField(max_length=100, required=True)
    opp_province = IntField(min_value=0, max_value=99999999999, required=True)
    opp_city = IntField(min_value=0, max_value=99999999999, required=True)
    opp_district = IntField(min_value=0, max_value=99999999999, required=True)
    opp_street = IntField(min_value=0, max_value=99999999999, required=True)
    opp_committee = IntField(min_value=0, max_value=99999999999, required=True)
    opp_address = StringField(max_length=100, required=True)
    opp_memo = StringField(max_length=6000, required=True)
    opp_hour = DecimalField(min_value=0.00, max_value=999999999.99, precision=2, default=0.00)
    system_code = IntField(min_value=0, max_value=99999999999)
