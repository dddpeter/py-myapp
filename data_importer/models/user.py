# coding=utf-8
__author__ = 'lijinde-lhq'
from mongoengine import *
from datetime import datetime

connect('mydb', host='localhost', port=27017)


class User(Document):
    vol_id = IntField(min_value=0, max_value=99999999999, required=True)
    idcard_number = StringField(max_length=20, required=True)
    vol_true_name = StringField(max_length=50, required=True)
    vol_province = IntField(min_value=0, max_value=99999999999, required=True)
    vol_city = IntField(min_value=0, max_value=99999999999, required=True)
    vol_district = IntField(min_value=0, max_value=99999999999, required=True)
    vol_street = IntField(min_value=0, max_value=99999999999, required=True)
    vol_committee = IntField(min_value=0, max_value=99999999999, required=True)
    vol_address = StringField(max_length=100, required=True)
    member_group_code = StringField(max_length=64)
    post_code = IntField(min_value=10000, max_value=9999999999)
    vol_gender = DictField()
    IntField(min_value=0, max_value=2, required=True)
    vol_birth_year = IntField(min_value=0, max_value=9999)
    vol_birth_month = IntField(min_value=1, max_value=12)
    vol_birth_day = IntField(min_value=1, max_value=31)
    vol_birth_date = DateTimeField()
    vol_political = IntField(min_value=0, max_value=999999, required=True)
    vol_ethnicity = IntField(min_value=0, max_value=999999, required=True)
    vol_hour = DecimalField(min_value=0.00, max_value=999999999.99, precision=2, default=0.00, required=True)
    native_place = StringField(max_length=100)
    domicile_place = IntField(min_value=0, max_value=9999999999)
    vol_edu = StringField(max_length=50, required=True)
    vol_univercity = StringField(max_length=50, required=True)
    profession = StringField(max_length=50)
    workunit = StringField(max_length=50)
    job_type = StringField(max_length=100)
    job_post = StringField(max_length=100)
    job_title = StringField(max_length=100)
    vol_religion = StringField(max_length=20)
    create_time = DateTimeField(default=datetime.datetime.now)
    login_time = DateTimeField()
    login_email = EmailField(required=True)
    login_mobile = IntField(min_value=10000000000, max_value=99999999999, required=True)
    vol_service_tag = IntField(min_value=0, max_value=999999, required=True)
    strong_point = StringField(max_length=50)
    hobby = StringField(max_length=50)
    system_code = IntField(min_value=0, max_value=99999999999)

