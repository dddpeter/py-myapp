# coding:utf-8

from django.views.decorators.csrf import csrf_exempt
import json
import simplejson

# Create your views here.
from django.http import HttpResponse

from data_importer.models import information
from data_importer.utils import mongo_util

@csrf_exempt
def information_json(request):
    i = information.Information('test_tilte', 'test_content')
    db = mongo_util.get_db('mydb')
    print mongo_util.insert(db, 'informations', simplejson.loads(
        json.dumps(i.__dict__, cls=information.CJsonEncoder)))
    print json.dumps(i.__dict__, cls=information.CJsonEncoder)
    return HttpResponse(json.dumps(i.__dict__, cls=information.CJsonEncoder), content_type="application/json;charset=utf-8")