__author__ = 'lijinde-lhq'
from data_importer.utils import mongo_util
import re


def check_email(email):
    if re.match(r'[^\._-][\w\.-]+@(?:[A-Za-z0-9]+\.)+[A-Za-z]+$', email):
        return True
    else:
        return False


def check_mobile(mobile):
    if re.match(r'^1\d{10}', mobile):
        return True
    else:
        return False

def check_dictionary(code):
    db = mongo_util.get_db('mydb')
    result = mongo_util.get(db, 'dictionary', {'_id': str(code)}).count()
    if result < 1:
        return False
    else:
        return True


def check_area(code):
    db = mongo_util.get_db('mydb')
    result = mongo_util.get(db, 'area', {'_id': str(code)}).count()
    if result < 1:
        return False
    else:
        return True